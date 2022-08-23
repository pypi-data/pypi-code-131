
def format_ax(ax,
              x_range=None, x_delta=None,
              y_range=None, y_delta=None, if_y_axis_prob=True,
              if_format_y_numbers=True, y_axis_decimal=1):

    # the range of x and y-axis are set so that we can get the
    # tick values and label
    if y_range is None and if_y_axis_prob:
        ax.set_ylim((-0.01, 1.01))
    if y_range:
        ax.set_ylim(y_range)
    if x_range:
        ax.set_xlim(x_range)

    # get x ticks
    if x_delta is None:
        vals_x = ax.get_xticks()
    else:
        vals_x = []
        x = x_range[0]
        while x <= x_range[1]:
            vals_x.append(x)
            x += x_delta

    # get y ticks
    if y_delta is None:
        vals_y = ax.get_yticks()
    else:
        vals_y = []
        y = y_range[0]
        while y <= y_range[1]:
            vals_y.append(y)
            y += y_delta

    # format x-axis
    ax.set_xticks(vals_x)
    ax.set_xticklabels(['{:,.{prec}f}'.format(x, prec=0) for x in vals_x])

    d = 2 * (x_range[1] - x_range[0]) / 200
    ax.set_xlim([x_range[0] - d, x_range[1] + d])

    # format y-axis
    if y_range is None:
        ax.set_yticks(vals_y)
    if if_y_axis_prob:
        ax.set_yticklabels(['{:.{prec}f}'.format(x, prec=1) for x in vals_y])
    elif if_format_y_numbers:
        ax.set_yticklabels(['{:,.{prec}f}'.format(x, prec=y_axis_decimal) for x in vals_y])

    if y_range is None and if_y_axis_prob:
        ax.set_ylim((-0.01, 1.01))
    if y_range:
        ax.set_ylim(y_range)

    if not if_y_axis_prob:
        ax.axhline(y=0, c='k', ls='--', linewidth=0.5)


def add_curves_to_ax(ax, curves, title=None,
                     x_range=None, x_label=None, y_label=None, y_range=None,
                     y_axis_multiplier=1, y_axis_decimal=1,
                     x_delta=None,
                     transparency_lines=0.5,
                     transparency_intervals=0.2,
                     legends=None,
                     show_legend=False,
                     show_frontier=True,
                     show_labels_on_frontier=False,
                     curve_line_width=1.0, frontier_line_width=4.0,
                     if_y_axis_prob=False,
                     if_format_y_numbers=True,
                     legend_font_size=7,
                     frontier_label_shift_x=-0.01,
                     frontier_label_shift_y=0.01):

    for i, curve in enumerate(curves):

        label = curve.label if legends is None else legends
        # plot line
        ax.plot(curve.xs, curve.ys * y_axis_multiplier,
                c=curve.color, alpha=transparency_lines,
                linewidth=curve_line_width, linestyle=curve.linestyle, label=label)

        # plot intervals
        if curve.l_errs is not None and curve.u_errs is not None:
            ax.fill_between(curve.xs,
                            (curve.ys - curve.l_errs) * y_axis_multiplier,
                            (curve.ys + curve.u_errs) * y_axis_multiplier,
                            color=curve.color, alpha=transparency_intervals)
        # plot frontier
        if show_frontier:
            # check if this strategy is not dominated
            if curve.frontierXs is not None and len(curve.frontierXs) > 0:
                y = [y*y_axis_multiplier if y is not None else None for y in curve.frontierYs]
                ax.plot(curve.frontierXs, y,
                        c=curve.color, alpha=1, linewidth=frontier_line_width)

    if show_legend:
        ax.legend(loc=2, fontsize=legend_font_size)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_ylim(y_range)

    # add labels on the frontier
    if show_labels_on_frontier:
        y_min, y_max = ax.get_ylim()
        y_axis_length = y_max - y_min
        for curve in curves:
            if curve.frontierXs is not None and len(curve.frontierXs) > 0:
                if curve.frontierYs[0] is not None and curve.frontierYs[-1] is not None:
                    x_axis_length = x_range[1] - x_range[0]
                    x = 0.5 * (curve.frontierXs[0] + curve.frontierXs[-1]) + frontier_label_shift_x * x_axis_length
                    y = 0.5 * (curve.frontierYs[0] + curve.frontierYs[-1]) * y_axis_multiplier \
                        + frontier_label_shift_y * y_axis_length
                    ax.text(x=x, y=y, s=curve.label, fontsize=legend_font_size+1, c=curve.color)

    # do the other formatting
    format_ax(ax=ax, y_range=y_range,
              x_range=x_range, x_delta=x_delta,
              if_y_axis_prob=if_y_axis_prob,
              if_format_y_numbers=if_format_y_numbers,
              y_axis_decimal=y_axis_decimal)