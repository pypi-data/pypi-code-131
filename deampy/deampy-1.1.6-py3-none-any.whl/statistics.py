import math
import sys
import warnings

import numpy as np
import scipy.stats as stat
import statsmodels.api as sm
from scipy.stats import pearsonr
from statsmodels.stats.proportion import proportion_confint

import deampy.format_functions as F

NUM_BOOTSTRAP_SAMPLES = 1000


def get_sterr_from_half_length(confidence_interval, n, alpha=0.05):
    """
    :param confidence_interval: a t-based confidence interval
    :param n: number of observations
    :param alpha: significance level
    :return: the standard err (st_dev / sqrt(n))
    """
    half_length = (confidence_interval[1] - confidence_interval[0]) / 2
    t = stat.t.ppf(1 - alpha / 2, n - 1)
    return half_length / t


def partial_corr(x, y, z):
    """
    :param x: (list) of values for the input variable
    :param y: (list) of values for the output variable
    :param z: (list of list) list of values for the controlling variables
                [[z11, z12, ..., z1n],  # values of first controlling variable
                 [z21, z22, ..., z2n],  # values of second controlling variable
                 ...
                ]
    :return: partial correlation between x and y given the set of controlling variables z
    """

    np_z = np.array(z).T
    
    Z = sm.add_constant(np_z)
    # fit f(z) to x
    fitted_xz = sm.OLS(x, Z).fit()
    # fit f(z) to y
    fitted_yz = sm.OLS(y, Z).fit()
    # residuals f(z) - x
    x_residuals = fitted_xz.predict() - x
    # residuals f(z) - y
    y_residuals = fitted_yz.predict() - y
    # correlation between residuals
    coef, p = pearsonr(x_residuals, y_residuals)
    return coef, p


class _Statistics(object):
    def __init__(self, name=None):
        """ abstract method to be overridden in derived classes"""
        self.name = name        # name of this statistics
        self._n = 0              # number of data points
        self._mean = 0           # sample mean
        self._stDev = 0          # sample standard deviation
        self._max = -sys.float_info.max  # maximum
        self._min = sys.float_info.max   # minimum

    def get_n(self):
        """ abstract method to be overridden in derived classes
        :returns mean (to be calculated in the subclass) """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_mean(self):
        """ abstract method to be overridden in derived classes
        :returns mean (to be calculated in the subclass) """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_stdev(self):
        """ abstract method to be overridden in derived classes
        :returns standard deviation (to be calculated in the subclass) """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_var(self):
        return self.get_stdev()**2

    def get_min(self):
        """ abstract method to be overridden in derived classes
        :returns minimum (to be calculated in the subclass) """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_max(self):
        """ abstract method to be overridden in derived classes
        :returns maximum (to be calculated in the subclass) """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_percentile(self, q):
        """ abstract method to be overridden in derived classes
        :param q: percentile to compute (q in range [0, 100])
        :returns percentile (to be calculated in the subclass) """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_t_half_length(self, alpha):
        """
        :param alpha: significance level (between 0 and 1)
        :returns half-length of 100(1-alpha)% t-confidence interval """

        if self._n > 1:
            return stat.t.ppf(1 - alpha / 2, self.get_n() - 1) * self.get_stdev() / np.sqrt(self.get_n())
        else:
            return math.nan

    def get_t_CI(self, alpha):
        """ calculates t-based confidence interval for population mean
        :param alpha: significance level (between 0 and 1)
        :return: a list [l, u]
        """

        if self._n > 1:
            mean = self.get_mean()
            hl = self.get_t_half_length(alpha)
            return [mean - hl, mean + hl]
        else:
            return [math.nan, math.nan]

    def _get_proportion_CI(self, n_of_successes, n_of_trials, alpha):
        """
        :param n_of_successes: number of successes
        :param n_of_trials: number of trials
        :param alpha: significance level (between 0 and 1)
        :return: Wilon score interval in the format of list [l, u]
        """

        return proportion_confint(count=n_of_successes, nobs=n_of_trials, alpha=alpha, method='wilson')

    def get_bootstrap_CI(self, alpha, num_samples):
        """ calculates empirical bootstrap confidence interval (abstract method to be overridden in derived classes)
        :param alpha: significance level
        :param num_samples: number of bootstrap samples
        :returns a list [L, U] """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_PI(self, alpha):
        """ calculates percentile interval (abstract method to be overridden in derived classes)
        :param alpha: significance level (between 0 and 1)
        :returns a list [L, U]
         """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_summary(self, alpha, digits):
        """
        :param alpha: significance level
        :param digits: digits to round the numbers to
        :return: a list ['name', 'mean', 'confidence interval', 'percentile interval', 'st dev', 'min', 'max']
        """
        return [self.name,
                F.format_number(self.get_mean(), digits),
                F.format_interval(self.get_t_CI(alpha), digits),
                F.format_interval(self.get_PI(alpha), digits),
                F.format_number(self.get_stdev(), digits),
                F.format_number(self.get_min(), digits),
                F.format_number(self.get_max(), digits)]

    def get_interval(self, interval_type='c', alpha=0.05, multiplier=1):
        """
        :param interval_type: (string) 'c' for t-based confidence interval,
                                       'cb' for bootstrap confidence interval, and
                                       'p' for percentile interval
        :param alpha: significance level
        :param multiplier: to multiply the estimate and the interval by the provided value
        :return: a list [L, U]
        """

        if interval_type == 'c':
            interval = self.get_t_CI(alpha)
        elif interval_type == 'cb':
            interval = self.get_bootstrap_CI(alpha, NUM_BOOTSTRAP_SAMPLES)
        elif interval_type == 'p':
            interval = self.get_PI(alpha)
        elif interval_type == 'n' or None:
            interval = None
        else:
            raise ValueError('Invalid interval type.')
        if interval is not None:
            if multiplier > 0:
                return [v * multiplier for v in interval]
            else:
                return [interval[1]*multiplier, interval[0]*multiplier]
        else:
            return None

    def get_formatted_mean_and_interval(self, interval_type='c',
                                        alpha=0.05, deci=None, sig_digits=None, form=None, multiplier=1):
        """
        :param interval_type: (string) 'c' for t-based confidence interval,
                                       'cb' for bootstrap confidence interval, and
                                       'p' for percentile interval
        :param alpha: significance level
        :param deci: digits to round the numbers to
        :param sig_digits: number of significant digits
        :param form: ',' to format as number, '%' to format as percentage, and '$' to format as currency
        :param multiplier: to multiply the estimate and the interval by the provided value
        :return: (string) estimate and interval formatted as specified
        """

        estimate = self.get_mean()*multiplier
        interval = self.get_interval(interval_type=interval_type, alpha=alpha, multiplier=multiplier)

        return F.format_estimate_interval(estimate=estimate,
                                          interval=interval,
                                          deci=deci,
                                          sig_digits=sig_digits,
                                          format=form)

    def get_formatted_interval(self, interval_type='c',
                               alpha=0.05, deci=None, sig_digits=None, form=None, multiplier=1):
        """
        :param interval_type: (string) 'c' for t-based confidence interval,
                                       'cb' for bootstrap confidence interval, and
                                       'p' for percentile interval
        :param alpha: significance level
        :param deci: digits to round the numbers to
        :param sig_digits: number of significant digits
        :param form: ',' to format as number, '%' to format as percentage, and '$' to format as currency
        :param multiplier: to multiply the estimate and the interval by the provided value
        :return: (string) interval formatted as specified
        """

        interval = self.get_interval(interval_type=interval_type, alpha=alpha, multiplier=multiplier)

        return F.format_interval(interval=interval,
                                 deci=deci,
                                 sig_digits=sig_digits,
                                 format=form)


class SummaryStat(_Statistics):
    def __init__(self, data, name=None):
        """:param data: a list or numpy.array of data points"""

        _Statistics.__init__(self, name)
        # convert data to numpy array if needed
        if type(data) is list:
            self._data = np.array(data)
        elif type(data) is np.ndarray:
            self._data = data
        else:
            raise ValueError("The argument data can be either a list of numbers or a numpy.array.")

        if len(data) == 0:
            raise ValueError("The data provided for summary statistics '" + name + "' is empty.")

        self._n = len(self._data)
        self._total = np.sum(self._data)
        self._mean = np.mean(self._data)
        if self._n > 1:
            self._stDev = np.std(self._data, ddof=1)  # unbiased estimator of the standard deviation
        else:
            self._stDev = math.nan

    def get_n(self):
        return self._n

    def get_total(self):
        return self._total

    def get_mean(self):
        return self._mean

    def get_stdev(self):
        return self._stDev

    def get_min(self):
        return np.min(self._data)

    def get_max(self):
        return np.max(self._data)

    def get_percentile(self, q):
        """
        :param q: percentile to compute (q in range [0, 100])
        :returns: qth percentile """

        return np.percentile(self._data, q)

    def get_bootstrap_CI(self, alpha, num_samples):
        """ calculates the empirical bootstrap confidence interval
        :param alpha: significance level (between 0 and 1)
        :param num_samples: number of bootstrap samples
        :return: a list [l, u]
        """

        # set random number generator seed
        np.random.seed(1)

        # initialize delta array
        delta = np.zeros(num_samples)

        # obtain bootstrap samples
        for i in range(num_samples):
            sample_i = np.random.choice(self._data, size=self._n, replace=True)
            delta[i] = sample_i.mean() - self.get_mean()

        # return [l, u]
        return self.get_mean() - np.percentile(delta, [100 * (1 - alpha / 2.0), 100 * alpha / 2.0])

    def get_proportion_CI(self, alpha):
        """
        :param alpha: significance level (between 0 and 1)
        :return: Wilson score interval in the format of list [l, u]
        """

        # observations should be either 0 or 1
        for d in self._data:
            if d not in (0, 1):
                raise ValueError('Wilson score interval can only be calculated for binary (0 or 1) outcomes.')

        return self._get_proportion_CI(n_of_successes=sum(self._data), n_of_trials=self._n, alpha=alpha)

    def get_PI(self, alpha):
        """
        :param alpha: significance level (between 0 and 1)
        :return: percentile interval in the format of list [l, u]
        """
        return [self.get_percentile(100*alpha/2), self.get_percentile(100*(1-alpha/2))]

    @staticmethod
    def get_array_from_formatted_interval(interval):
        """
        :param interval: (string) of form '[a, b]'
        :return: (np.array) [a, b]
        """
        str_range = interval[1:-1].split(',')
        return np.array(str_range).astype(float)


class DiscreteTimeStat(_Statistics):
    """ to calculate statistics on observations accumulating over time """
    def __init__(self, name=None):
        _Statistics.__init__(self, name)
        self._total = 0
        self._sumSquared = 0

    def record(self, obs):
        """ gets the next observation and update the current information"""
        self._total += obs
        self._sumSquared += obs ** 2
        self._n += 1
        if obs > self._max:
            self._max = obs
        if obs < self._min:
            self._min = obs

    def get_n(self):
        return self._n

    def get_total(self):
        return self._total

    def get_mean(self):
        if self._n > 0:
            return self._total / self._n
        else:
            return 0

    def get_stdev(self):
        if self._n>1:
            return math.sqrt(
                (self._sumSquared - self._total ** 2 / self._n)
                / (self._n - 1)
            )
        else:
            return 0

    def get_min(self):
        return self._min

    def get_max(self):
        return self._max

    def get_percentile(self, q):
        """ percentiles cannot be calculated for this statistics """
        return None

    def get_bootstrap_CI(self, alpha, num_samples):
        """ bootstrap confidence intervals cannot be calculated for this statistics """
        return None

    def get_PI(self, alpha):
        """ percentile intervals cannot be calculated for this statistics """
        return None


class ContinuousTimeStat(_Statistics):
    """ to calculate statistics on the area-under-the-curve for observations accumulating over time """
    def __init__(self, initial_time, ave_method='step', name=None):
        """
        :param initial_time: it is assumed that the value of this sample path is zero at the initial time
        :param ave_method: to calculate the area under the curve,
            'step' assumes that changes occurred at the time where observations are recorded,
            'linear' assumes uses trapezoid approach to calculate the area under the curve
                    (v2 + v2 ) * deltaT / 2
        """
        _Statistics.__init__(self, name)
        self._initialTime = initial_time

        if ave_method not in ('step', 'linear'):
            raise ValueError('ave_method should be either step or linear.')
        self._aveMethod = ave_method
        self._area = 0
        self._areaSquared = 0
        self._lastObsTime = initial_time
        self._lastObsValue = 0

    def record(self, time, increment):
        """ gets the next observation and update the current information
        :param time: time of this change in the sample path
        :param increment: the amount of change (can be positive or negative) in the sample path
        """

        if time < self._initialTime:
            self._lastObsTime = time
            self._lastObsValue += increment
            return
        else:
            self._lastObsTime = max(self._lastObsTime, self._initialTime)

        if self._lastObsValue > self._max:
            self._max = self._lastObsValue
        if time == self._initialTime:
            self._min = self._lastObsValue
        elif self._lastObsValue < self._min:
            self._min = self._lastObsValue

        self._n += 1
        if self._aveMethod == 'step':
            self._area += self._lastObsValue * (time - self._lastObsTime)
            self._areaSquared += (self._lastObsValue ** 2) * (time - self._lastObsTime)
        else:
            self._area += (self._lastObsValue + increment/2) * (time - self._lastObsTime)
            self._areaSquared += ((self._lastObsValue + increment/2) ** 2) * (time - self._lastObsTime)

        self._lastObsTime = time
        self._lastObsValue += increment

    def get_n(self):
        return self._n

    def get_mean(self):
        if self._lastObsTime - self._initialTime > 0:
            return self._area / (self._lastObsTime - self._initialTime)
        else:
            return 0

    def get_stdev(self):
        var = 0
        if self._lastObsTime - self._initialTime > 0:
            var = self._areaSquared / (self._lastObsTime - self._initialTime) - self.get_mean() ** 2

        return math.sqrt(var)

    def get_min(self):
        return self._min

    def get_max(self):
        return self._max

    def get_percentile(self, q):
        """ percentiles cannot be calculated for this statistics """
        return None

    def get_bootstrap_CI(self, alpha, num_samples):
        """ bootstrap confidence intervals cannot be calculated for this statistics """
        return None

    def get_PI(self, alpha):
        """ percentile intervals cannot be calculated for this statistics """
        return None


class _ComparativeStat(_Statistics):
    def __init__(self, x, y_ref, name=None):
        """
        :param x: list or numpy.array of first set of observations
        :param y_ref: list or numpy.array of second set of observations (the reference) 
        """
        _Statistics.__init__(self, name)

        if type(x) == list:
            self._x = np.array(x)
        elif type(x) == np.ndarray:
            self._x = x
        else:
            raise ValueError("The argument x can be either a list of numbers or a numpy.array.")

        if type(y_ref) == list:
            self._y_ref = np.array(y_ref)
        elif type(y_ref) == np.ndarray:
            self._y_ref = y_ref
        else:
            raise ValueError("The argument y_ref can be either a list of numbers or a numpy.array.")

        if len(self._x) == 0:
            raise ValueError("x is empty for the comparative statistics '" + name + "'.")
        if len(self._y_ref) == 0:
            raise ValueError("y_ref is empty for the comparative statistics '" + name + "'.")

        self._x_n = len(self._x)        # number of observations for x
        self._y_n = len(self._y_ref)    # number of observations for y_ref


class _DifferenceStat(_ComparativeStat):

    def __init__(self, x, y_ref, name=None):
        """
        :param x: list or numpy.array of first set of observations
        :param y_ref: list or numpy.array of second set of observations
        """
        _ComparativeStat.__init__(self, x, y_ref, name)


class DifferenceStatPaired(_DifferenceStat):

    def __init__(self, x, y_ref, name=None):
        """
        :param x: list or numpy.array of first set of observations
        :param y_ref: list or numpy.array of second set of observations
        """
        _DifferenceStat.__init__(self,  x, y_ref, name)
        # create a summary statistics for the element-wise difference

        if len(self._x) != len(self._y_ref):
            raise ValueError('Two samples (x and y_ref) should have the same size.')

        self._dStat = SummaryStat(self._x - self._y_ref, name)

    def get_n(self):
        return self._dStat.get_n()

    def get_mean(self):
        return self._dStat.get_mean()

    def get_stdev(self):
        return self._dStat.get_stdev()

    def get_min(self):
        return self._dStat.get_min()

    def get_max(self):
        return self._dStat.get_max()

    def get_percentile(self, q):
        return self._dStat.get_percentile(q)

    def get_t_CI(self, alpha):
        return self._dStat.get_t_CI(alpha)

    def get_bootstrap_CI(self, alpha, num_samples):
        return self._dStat.get_bootstrap_CI(alpha, num_samples)

    def get_PI(self, alpha):
        return self._dStat.get_PI(alpha)


class DifferenceStatIndp(_DifferenceStat):

    def __init__(self, x, y_ref, name=None):
        """
        :param x: list or numpy.array of first set of observations
        :param y_ref: list or numpy.array of second set of observations
        """
        _DifferenceStat.__init__(self, x, y_ref, name)

        self._XMinusYSimulated = False

    def _simulate_x_minus_y(self):

        # generate random realizations for random variable X - Y
        # this will be used for calculating the projection interval
        np.random.seed(1)
        # find the maximum of the number of observations
        max_n = max(self._x_n, self._y_n, NUM_BOOTSTRAP_SAMPLES)
        x_i = np.random.choice(self._x, size=max_n, replace=True)
        y_i = np.random.choice(self._y_ref, size=max_n, replace=True)
        self._sum_stat_sample_delta = SummaryStat(x_i - y_i, self.name)

        self._XMinusYSimulated = True

    def get_mean(self):
        """
        for independent variable x and y, E(x-y) = E(x) - E(y)
        :return: sample mean of (x-y)
        """
        return np.mean(self._x) - np.mean(self._y_ref)

    def get_stdev(self):
        """
        for independent variable x and y, var(x-y) = var_x + var_y
        :returns: sample standard deviation
        """
        var_x = np.var(self._x)
        var_y = np.var(self._y_ref)
        return np.sqrt(var_x + var_y)

    def get_min(self):

        if not self._XMinusYSimulated:
            self._simulate_x_minus_y()
        return self._sum_stat_sample_delta.get_min()

    def get_max(self):

        if not self._XMinusYSimulated:
            self._simulate_x_minus_y()
        return self._sum_stat_sample_delta.get_max()

    def get_percentile(self, q):
        """
        for independent variable x and y, percentiles are given after re-sampling
        :param q: the percentile want to return, in [0, 100]
        :return: qth percentile of sample (x-y)
        """

        if not self._XMinusYSimulated:
            self._simulate_x_minus_y()

        return self._sum_stat_sample_delta.get_percentile(q)

    def get_bootstrap_CI(self, alpha, num_samples=None):
        """
        :param alpha: confidence level
        :param num_samples: number of bootstrap samples
        :return: empirical bootstrap confidence interval
        """

        n = NUM_BOOTSTRAP_SAMPLES if num_samples is None else num_samples

        # set random number generator seed
        np.random.seed(1)

        # find number of bootstrap samples
        n = max(self._x_n, self._y_n, n)

        # initialize difference array
        diff = np.zeros(n)

        # obtain bootstrap samples
        for i in range(n):
            x_i = np.random.choice(self._x, size=n, replace=True)
            y_i = np.random.choice(self._y_ref, size=n, replace=True)
            d_temp = x_i - y_i
            diff[i] = np.mean(d_temp)

        return np.percentile(diff, [100 * alpha / 2.0, 100 * (1 - alpha / 2.0)])

    def get_t_half_length(self, alpha):
        """
        Independent x_bar - y_bar is t distribution
        ref: https://onlinecourses.science.psu.edu/stat414/node/203
        :param alpha: confidence level
        :return: confidence interval of x_bar - y_bar
        """

        sig_x = np.std(self._x)
        sig_y = np.std(self._y_ref)

        alpha = alpha / 100.0

        # calculate CI using formula: Welch's t-interval
        df_n = (sig_x ** 2.0 / self._x_n + sig_y ** 2.0 / self._y_n) ** 2.0
        df_d = (sig_x ** 2.0 / self._x_n) ** 2 / (self._x_n - 1) \
               + (sig_y ** 2.0 / self._y_n) ** 2 / (self._y_n - 1)
        df = round(df_n / df_d, 0)

        # t distribution quantile
        t_q = stat.t.ppf(1 - (alpha / 2), df)
        st_dev = (sig_x ** 2.0 / self._x_n + sig_y ** 2.0 / self._y_n) ** 0.5

        return t_q*st_dev

    def get_t_CI(self, alpha):

        interval = self.get_t_half_length(alpha)
        diff = np.mean(self._x) - np.mean(self._y_ref)

        return [diff - interval, diff + interval]

    def get_PI(self, alpha):

        if not self._XMinusYSimulated:
            self._simulate_x_minus_y()

        return self._sum_stat_sample_delta.get_PI(alpha)


class _RatioStat(_ComparativeStat):

    def __init__(self, x, y_ref, name=None):
        """
        :param x: list or numpy.array of first set of observations
        :param y_ref: list or numpy.array of second set of observations
        """
        _ComparativeStat.__init__(self, x, y_ref, name)

        self._ifComputable = True  # if any element of the denominator is 0, ratio is not computable


class RatioStatPaired(_RatioStat):

    def __init__(self, x, y_ref, name=None):
        """
        :param x: list or numpy.array of first set of observations
        :param y_ref: list or numpy.array of second set of observations
        """
        _RatioStat.__init__(self, x, y_ref, name)

        if len(self._x) != len(self._y_ref):
            raise ValueError('Two samples (x and y_ref) should have the same size.')

        # add element-wise ratio
        ratio = np.zeros(len(self._x))
        for i in range(len(self._x)):
            # for 0 in the denominator variable, check whether numerator is also 0
            if self._y_ref[i] == 0:
                ratio[i] = math.nan
                warnings.warn("For ratio statistics '{}', "
                              "the denominator of ratio with index {} is 0."
                              "The ratio is not computable.".format(name, i))
                self._ifComputable = False
            else:
                # for non-zero denominators, calculate ratio
                ratio[i] = 1.0*self._x[i] / self._y_ref[i]

        # create summary stat for element-wise ratio
        self._ratioStat = SummaryStat(ratio, name)

    def get_n(self):
        return self._ratioStat.get_n()

    def get_mean(self):
        if self._ifComputable:
            return self._ratioStat.get_mean()
        else:
            return math.nan

    def get_stdev(self):
        if self._ifComputable:
            return self._ratioStat.get_stdev()
        else:
            return math.nan

    def get_min(self):
        return self._ratioStat.get_min()

    def get_max(self):
        return self._ratioStat.get_max()

    def get_percentile(self, q):
        if self._ifComputable:
            return self._ratioStat.get_percentile(q)
        else:
            return math.nan

    def get_t_CI(self, alpha):
        if self._ifComputable:
            return self._ratioStat.get_t_CI(alpha)
        else:
            return math.nan

    def get_bootstrap_CI(self, alpha, num_samples):
        if self._ifComputable:
            return self._ratioStat.get_bootstrap_CI(alpha, num_samples)
        else:
            return math.nan

    def get_PI(self, alpha):
        if self._ifComputable:
            return self._ratioStat.get_PI(alpha)
        else:
            return [math.nan, math.nan]


class RatioStatIndp(_RatioStat):

    def __init__(self, x, y_ref, name=None):
        """
        :param x: list or numpy.array of first set of observations
        :param y_ref: list or numpy.array of second set of observations (reference)

        https://en.wikipedia.org/wiki/Ratio_distribution
        """

        _RatioStat.__init__(self, x, y_ref, name)

        self._XOverYSimulated = False

    def _simulate_x_over_y(self):

        # generate random realizations for random variable X/Y
        np.random.seed(1)
        # find the maximum of the number of observations
        max_n = max(self._x_n, self._y_n, NUM_BOOTSTRAP_SAMPLES)
        x_resample = np.random.choice(self._x, size=max_n, replace=True)
        y_resample = np.random.choice(self._y_ref, size=max_n, replace=True)

        self._XOverYSimulated = True
        self._ifComputable = True
        try:
            self._sum_stat_sample_ratio = SummaryStat(
                data=np.divide(x_resample, y_resample), name=self.name)
        except ZeroDivisionError:
            warnings.warn("For ratio statistics '{}', "
                          "one element of y_ref is 0.".format(self.name))
            self._ifComputable = False

    def get_mean(self):
        """
        for independent variable x and y, E(x/y) = E(x)*E(1/y)
        :return: E(x/y)
        """

        return np.average(self._x)*np.average(1/self._y_ref)

    def get_stdev(self):
        """
        for independent variable x and y, var(x/y) = E(x^2)*E(1/y^2)-E(x)^2*(E(1/y)^2)
        :return: std(x/y)
        """
        var = np.mean(self._x ** 2) * np.mean(1.0 / self._y_ref ** 2) - \
              (np.mean(self._x) ** 2) * (np.mean(1.0 / self._y_ref) ** 2)
        return np.sqrt(var)

    def get_min(self):

        if not self._XOverYSimulated:
            self._simulate_x_over_y()
        if self._ifComputable:
            return self._sum_stat_sample_ratio.get_min()
        else:
            return math.nan

    def get_max(self):

        if not self._XOverYSimulated:
            self._simulate_x_over_y()
        if self._ifComputable:
            return self._sum_stat_sample_ratio.get_max()
        else:
            return math.nan

    def get_percentile(self, q):
        """
        for independent variable x and y, percentiles are given after re-sampling
        :param q: the percentile want to return, in [0,100]
        :return: qth percentile of sample (x/y)
        """

        if not self._XOverYSimulated:
            self._simulate_x_over_y()
        if self._ifComputable:
            return self._sum_stat_sample_ratio.get_percentile(q)
        else:
            return math.nan

    def get_t_half_length(self, alpha):

        if not self._XOverYSimulated:
            self._simulate_x_over_y()
        if self._ifComputable:
            return self._sum_stat_sample_ratio.get_t_half_length(alpha)
        else:
            return math.nan

    def get_t_CI(self, alpha):

        if self._x_n > 1 and self._y_n>1:
            mean = self.get_mean()
            hl = self.get_t_half_length(alpha)
            return [mean - hl, mean + hl]
        else:
            return [math.nan, math.nan]

    def get_bootstrap_CI(self, alpha, num_samples):
        """
        :param alpha: confidence level
        :param num_samples: number of samples
        :return: empirical bootstrap confidence interval
        """

        # set random number generator seed
        np.random.seed(1)

        # initialize ratio array
        ratio = np.zeros(num_samples)

        # obtain bootstrap samples
        n = max(self._x_n, self._y_n)
        for i in range(num_samples):
            x_i = np.random.choice(self._x, size=n, replace=True)
            y_i = np.random.choice(self._y_ref, size=n, replace=True)
            r_temp = np.divide(x_i, y_i)
            ratio[i] = np.mean(r_temp)

        return np.percentile(ratio, [100 * alpha / 2.0, 100 * (1 - alpha / 2.0)])

    def get_PI(self, alpha):

        if not self._XOverYSimulated:
            self._simulate_x_over_y()

        if self._ifComputable:
            return self._sum_stat_sample_ratio.get_PI(alpha)
        else:
            return [math.nan, math.nan]


class _RelativeDifference(_ComparativeStat):
    """ class to make inference about (X-Y_ref)/Y_ref or (Y_ref-X)/Y_ref"""

    def __init__(self, x, y_ref, order=0, name=None):
        """
        :param x: list or numpy.array of first set of observations
        :param y_ref: list or numpy.array of second set of observations used as the reference values
        :param order: set to 0 to calculate (X-Y_ref)/Y and to 1 to calculate (Y_ref-X)/Y_ref
        """
        _ComparativeStat.__init__(self, x, y_ref, name)
        self._order = order
        self._ifComputable = True  # if any element of the denominator is 0, ratio is not computable


class RelativeDifferencePaired(_RelativeDifference):

    def __init__(self, x, y_ref, order=0, name=None):
        """
        :param x: list or numpy.array of first set of observations
        :param y_ref: list or numpy.array of second set of observations
        :param order: set to 0 to calculate (X-Y_ref)/Y_ref and to 1 to calculate (Y_ref-X)/Y_ref
        """
        _RelativeDifference.__init__(self, x, y_ref, order, name)

        if len(self._x) != len(self._y_ref):
            raise ValueError('Two samples should have the same size.')

        # add element-wise ratio
        ratio = np.zeros(len(self._x))

        for i in range(len(self._x)):
            # for 0 in the denominator variable, check whether numerator is also 0
            if self._y_ref[i] == 0:
                ratio[i] = math.nan
                warnings.warn("For ratio statistics '{}', "
                              "the denominator of ratio with index {} is 0."
                              "The ratio is not computable.".format(name, i))
                self._ifComputable = False
            # for non-zero denominators, calculate ratio
            else:
                ratio[i] = 1.0*self._x[i] / self._y_ref[i]

        # create summary stat for element-wise ratio
        if self._order == 0:
            self._relativeDiffStat = SummaryStat(ratio - 1, name)
        else:
            self._relativeDiffStat = SummaryStat(1 - ratio, name)

    def get_n(self):
        return self._relativeDiffStat.get_n()

    def get_mean(self):
        if self._ifComputable:
            return self._relativeDiffStat.get_mean()
        else:
            return math.nan

    def get_stdev(self):
        if self._ifComputable:
            return self._relativeDiffStat.get_stdev()
        else:
            return math.nan

    def get_min(self):
        return self._relativeDiffStat.get_min()

    def get_max(self):
        return self._relativeDiffStat.get_max()

    def get_percentile(self, q):
        if self._ifComputable:
            return self._relativeDiffStat.get_percentile(q)
        else:
            return math.nan

    def get_t_CI(self, alpha):
        if self._ifComputable:
            return self._relativeDiffStat.get_t_CI(alpha)
        else:
            return [math.nan, math.nan]

    def get_bootstrap_CI(self, alpha, num_samples):
        if self._ifComputable:
            return self._relativeDiffStat.get_bootstrap_CI(alpha, num_samples)
        else:
            return [math.nan, math.nan]

    def get_PI(self, alpha):
        if self._ifComputable:
            return self._relativeDiffStat.get_PI(alpha)
        else:
            return [math.nan, math.nan]


class RelativeDifferenceIndp(_RelativeDifference):
    def __init__(self, x, y_ref, order=0, name=None):
        """
        :param x: list or numpy.array of first set of observations
        :param y_ref: list or numpy.array of second set of observations
        :param order: set to 0 to calculate (X-Y_ref)/Y_ref and to 1 to calculate (Y_ref-X)/Y_ref
        """
        _RelativeDifference.__init__(self, x, y_ref, order, name)

        self._XMinusYOverYSimulated = False

    def _simulate_x_minus_y_over_y(self):

        # generate random realizations for random variable (X-Y)/Y
        np.random.seed(1)
        # find the maximum of the number of observations
        max_n = max(self._x_n, self._y_n, NUM_BOOTSTRAP_SAMPLES)
        x_resample = np.random.choice(self._x, size=max_n, replace=True)
        y_resample = np.random.choice(self._y_ref, size=max_n, replace=True)

        self._XMinusYOverYSimulated = True
        self._ifComputable = True
        if self._order == 0:
            try:
                self._sum_stat_sample_relativeRatio = SummaryStat(
                    np.divide(x_resample-y_resample, y_resample), self.name)
            except ZeroDivisionError:
                warnings.warn("For ratio statistics '{}', "
                              "one element of y_ref is 0.".format(self.name))
                self._ifComputable = False
        else:
            try:
                self._sum_stat_sample_relativeRatio = SummaryStat(
                    np.divide(y_resample-x_resample, y_resample), self.name)
            except ZeroDivisionError:
                warnings.warn("For ratio statistics '{}', "
                              "one element of y_ref is 0.".format(self.name))
                self._ifComputable = False

    def get_mean(self):
        """
        for independent variable x and y, E((x-y)/y) = E(x)*E(1/y) - 1
        :return: E((x-y)/y) or E((y-x)/y)
        """
        if self._order == 0:
            return np.average(self._x) * np.average(1 / self._y_ref) - 1
        else:
            return 1 - np.average(self._x) * np.average(1 / self._y_ref)

    def get_stdev(self):
        """
        for independent variable x and y, var(x/y) = E(x^2)*E(1/y^2)-E(x)^2*(E(1/y)^2)
        and var(x/y - 1) = var(x/y)
        :return: std(x/y - 1)
        """
        if self._ifComputable:
            var = np.mean(self._x ** 2) * np.mean(1.0 / self._y_ref ** 2) - \
                  (np.mean(self._x) ** 2) * (np.mean(1.0 / self._y_ref) ** 2)
            return np.sqrt(var)
        else:
            return math.nan

    def get_min(self):

        if not self._XMinusYOverYSimulated:
            self._simulate_x_minus_y_over_y()
        if self._ifComputable:
            return self._sum_stat_sample_relativeRatio.get_min()
        else:
            return math.nan

    def get_max(self):

        if not self._XMinusYOverYSimulated:
            self._simulate_x_minus_y_over_y()
        if self._ifComputable:
            return self._sum_stat_sample_relativeRatio.get_max()
        else:
            return math.nan

    def get_percentile(self, q):
        """
        for independent variable x and y, percentiles are given after re-sampling
        :param q: the percentile want to return, in [0,100]
        :return: qth percentile of sample (x-y)/y
        """

        if not self._XMinusYOverYSimulated:
            self._simulate_x_minus_y_over_y()
        if self._ifComputable:
            return self._sum_stat_sample_relativeRatio.get_percentile(q)
        else:
            return [math.nan, math.nan]

    def get_t_half_length(self, alpha):

        if not self._XMinusYOverYSimulated:
            self._simulate_x_minus_y_over_y()
        if self._ifComputable:
            return self._sum_stat_sample_relativeRatio.get_t_half_length(alpha)
        else:
            return math.nan

    def get_t_CI(self, alpha):

        if self._x_n > 1 and self._y_n>1:
            mean = self.get_mean()
            hl = self.get_t_half_length(alpha)
            return [mean - hl, mean + hl]
        else:
            return [math.nan, math.nan]

    def get_bootstrap_CI(self, alpha, num_samples):
        """
        :param alpha: confidence level
        :param num_samples: number of samples
        :return: empirical bootstrap confidence interval
        """

        # set random number generator seed
        np.random.seed(1)

        # initialize ratio array
        ratio = np.zeros(num_samples)

        # obtain bootstrap samples
        n = max(self._x_n, self._y_n)
        for i in range(num_samples):
            x_i = np.random.choice(self._x, size=n, replace=True)
            y_i = np.random.choice(self._y_ref, size=n, replace=True)
            r_temp = np.divide(x_i, y_i) - 1
            ratio[i] = np.mean(r_temp)

        return np.percentile(ratio, [100 * alpha / 2.0, 100 * (1 - alpha / 2.0)])

    def get_PI(self, alpha):

        if not self._XMinusYOverYSimulated:
            self._simulate_x_minus_y_over_y()
        if self._ifComputable:
            return self._sum_stat_sample_relativeRatio.get_PI(alpha)
        else:
            return [math.nan, math.nan]
