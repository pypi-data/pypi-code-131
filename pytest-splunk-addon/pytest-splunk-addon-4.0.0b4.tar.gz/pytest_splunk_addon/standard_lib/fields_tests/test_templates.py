#
# Copyright 2021 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
"""
Includes the test scenarios to check the field extractions of an Add-on.
"""
import pprint
import logging
import pytest
from ..addon_parser import Field
import json

from .requirement_test_datamodel_tag_constants import dict_datamodel_tag

TOP_FIVE_STRUCTURALLY_UNIQUE_EVENTS_QUERY_PART = " | dedup punct | head 5"
COUNT_BY_SOURCE_TYPE_SEARCH_QUERY_PART = " | stats count by sourcetype"


class FieldTestTemplates(object):
    """
    Test templates to test the knowledge objects of an App
    """

    logger = logging.getLogger("pytest-splunk-addon")

    @pytest.mark.splunk_searchtime_fields
    @pytest.mark.splunk_searchtime_internal_errors
    def test_splunk_internal_errors(
        self, splunk_search_util, ignore_internal_errors, record_property, caplog
    ):
        """
        This test case checks that there are not any unexpected internal errors

        Args:
            splunk_search_util (SearchUtil): Object that helps to search on Splunk.
            ignore_internal_errors (fixture): common list of errors to be ignored
            record_property (fixture): Document facts of test cases.
            caplog (fixture): fixture to capture logs.
        """
        search = """
            search index=_internal log_level=ERROR
            sourcetype!=splunkd_ui_access
            AND sourcetype!=splunk_web_access
            AND sourcetype!=splunk_web_service
            AND sourcetype!=splunkd_access
            AND sourcetype!=splunkd
        """
        for each in ignore_internal_errors:
            search += " NOT " + json.dumps(each)
        search += " | table _raw"
        record_property("search", search)
        result, results = splunk_search_util.checkQueryCountIsZero(search)
        if not result:
            record_property("results", results.as_list)
            pp = pprint.PrettyPrinter(indent=4)
            result_str = pp.pformat(results.as_list[:10])
        assert result, (
            f"Query result greater than 0.\nsearch={search}\n"
            f"found result={result_str}"
        )

    @pytest.mark.splunk_searchtime_fields
    @pytest.mark.splunk_searchtime_fields_positive
    def test_props_fields(
        self,
        splunk_search_util,
        splunk_ingest_data,
        splunk_setup,
        splunk_searchtime_fields_positive,
        record_property,
    ):
        """
        This test case checks that a field value has the expected values.

        Args:
            splunk_search_util (SearchUtil): Object that helps to search on Splunk.
            splunk_searchtime_fields_positive (fixture): Test for stanza field.
            record_property (fixture): Document facts of test cases.
            caplog (fixture): fixture to capture logs.
        """

        # Search Query
        record_property("stanza_name", splunk_searchtime_fields_positive["stanza"])
        record_property("stanza_type", splunk_searchtime_fields_positive["stanza_type"])
        record_property("fields", splunk_searchtime_fields_positive["fields"])

        index_list = (
            "(index="
            + " OR index=".join(splunk_search_util.search_index.split(","))
            + ")"
        )
        search = (
            f"search {index_list}"
            f" {splunk_searchtime_fields_positive['stanza_type']}=\""
            f"{splunk_searchtime_fields_positive['stanza']}\""
        )
        for field_dict in splunk_searchtime_fields_positive["fields"]:
            field = Field(field_dict)
            expected_values = ", ".join([f'"{each}"' for each in field.expected_values])
            negative_values = ", ".join([f'"{each}"' for each in field.negative_values])

            search = (
                search + f" AND ({field} IN ({expected_values})"
                f" AND NOT {field} IN ({negative_values}))"
            )
        search += COUNT_BY_SOURCE_TYPE_SEARCH_QUERY_PART

        self.logger.info(f"Executing the search query: {search}")

        # run search
        result = splunk_search_util.checkQueryCountIsGreaterThanZero(
            search,
            interval=splunk_search_util.search_interval,
            retries=splunk_search_util.search_retry,
        )
        record_property("search", search)

        assert result, (
            f"No result found for the search.\nsearch={search}\n"
            f"interval={splunk_search_util.search_interval}, retries={splunk_search_util.search_retry}"
        )

    @pytest.mark.splunk_searchtime_fields
    @pytest.mark.splunk_requirements
    @pytest.mark.splunk_searchtime_fields_requirements
    def test_requirements_fields(
        self,
        splunk_search_util,
        splunk_ingest_data,
        splunk_setup,
        splunk_searchtime_fields_requirements,
        record_property,
    ):
        """
        This test case checks that a field value has the expected values.

        Args:
            splunk_search_util (SearchUtil): Object that helps to search on Splunk.
            splunk_searchtime_fields_positive (fixture): Test for stanza field.
            record_property (fixture): Document facts of test cases.
            caplog (fixture): fixture to capture logs.
        """

        # Search Query
        record_property(
            "stanza_name", splunk_searchtime_fields_requirements["escaped_event"]
        )
        record_property("fields", splunk_searchtime_fields_requirements["fields"])
        record_property(
            "modinput_params", splunk_searchtime_fields_requirements["modinput_params"]
        )

        escaped_event = splunk_searchtime_fields_requirements["escaped_event"]
        fields = splunk_searchtime_fields_requirements["fields"]
        modinput_params = splunk_searchtime_fields_requirements["modinput_params"]

        index_list = (
            "(index="
            + " OR index=".join(splunk_search_util.search_index.split(","))
            + ")"
        )

        basic_search = ""
        for param, param_value in modinput_params.items():
            if param_value is not None:
                basic_search += f" {param}={param_value}"

        search = f"search {index_list} {basic_search} {escaped_event} | fields *"

        self.logger.info(f"Executing the search query: {search}")

        fields_from_splunk = splunk_search_util.getFieldValuesDict(
            search,
            interval=splunk_search_util.search_interval,
            retries=splunk_search_util.search_retry,
        )

        missing_fields = []
        wrong_value_fields = {}

        for field, value in fields.items():
            if field not in fields_from_splunk:
                missing_fields.append(field)

            if value != fields_from_splunk.get(field):
                wrong_value_fields[field] = fields_from_splunk.get(field)

        failure_message = ""

        for field, value in wrong_value_fields.items():
            failure_message += (
                f"Field {field} has value {value} and should has {fields[field]}\n"
            )

        self.logger.error(f"Fields with wrong values: {failure_message}")

        assert (
            missing_fields == []
        ), f"Not all required fields found in Splunk. Missing fields: {', '.join(missing_fields)}"
        assert (
            wrong_value_fields == {}
        ), f"Not all required fields have correct values in Splunk. Wrong field values: {failure_message} Search string: {search}"

    @pytest.mark.splunk_searchtime_fields
    @pytest.mark.splunk_searchtime_fields_negative
    def test_props_fields_no_dash_not_empty(
        self,
        splunk_search_util,
        splunk_ingest_data,
        splunk_setup,
        splunk_searchtime_fields_negative,
        record_property,
    ):
        """
        This test case checks negative scenario for the field value.

        Args:
            splunk_search_util (SearchUtil):
                Object that helps to search on Splunk.
            splunk_searchtime_fields_negative (fixture):
                Test for stanza field.
            record_property (fixture):
                Document facts of test cases.
            caplog (fixture):
                fixture to capture logs.
        """

        # Search Query
        record_property("stanza_name", splunk_searchtime_fields_negative["stanza"])
        record_property("stanza_type", splunk_searchtime_fields_negative["stanza_type"])
        record_property("fields", splunk_searchtime_fields_negative["fields"])

        index_list = (
            "(index="
            + " OR index=".join(splunk_search_util.search_index.split(","))
            + ")"
        )
        base_search = (
            f"search {index_list}"
            f" {splunk_searchtime_fields_negative['stanza_type']}=\""
            f"{splunk_searchtime_fields_negative['stanza']}\""
        )

        fields_search = []
        for field_dict in splunk_searchtime_fields_negative["fields"]:
            field = Field(field_dict)
            negative_values = ", ".join([f'"{each}"' for each in field.negative_values])

            fields_search.append(f"({field} IN ({negative_values}))")
        base_search += " AND ({})".format(" OR ".join(fields_search))
        search = base_search + COUNT_BY_SOURCE_TYPE_SEARCH_QUERY_PART

        self.logger.info(f"Executing the search query: {search}")

        # run search
        result, results = splunk_search_util.checkQueryCountIsZero(search)
        record_property("search", search)
        if not result:
            record_property("results", results.as_list)
            pp = pprint.PrettyPrinter(indent=4)
            result_str = pp.pformat(results.as_list[:10])

            query_for_unique_events = (
                base_search + TOP_FIVE_STRUCTURALLY_UNIQUE_EVENTS_QUERY_PART
            )
            query_results = splunk_search_util.get_search_results(
                query_for_unique_events
            )
            results_formatted_str = pp.pformat(query_results.as_list)
        assert result, (
            f"Query result greater than 0.\nsearch={search}\n"
            f"found result={result_str}\n"
            " === STRUCTURALLY UNIQUE EVENTS:\n"
            f"query={query_for_unique_events}\n"
            f"events= {results_formatted_str}"
        )

    @pytest.mark.splunk_searchtime_fields
    @pytest.mark.splunk_searchtime_fields_tags
    def test_tags(
        self,
        splunk_search_util,
        splunk_ingest_data,
        splunk_setup,
        splunk_searchtime_fields_tags,
        record_property,
        caplog,
    ):
        """
        Test case to check tags mentioned in tags.conf

        This test case checks if a tag is assigned to the event if enabled,
        and also checks that a tag is not assigned to the event if disabled.

        Args:
            splunk_search_util (helmut_lib.SearchUtil.SearchUtil):
                object that helps to search on Splunk.
            splunk_searchtime_fields_tags (fixture): pytest parameters to test.
            record_property (fixture): pytest fixture to document facts of test cases.
            caplog (fixture): fixture to capture logs.
        """

        is_tag_enabled = splunk_searchtime_fields_tags.get("enabled", True)
        tag_query = splunk_searchtime_fields_tags["stanza"]
        tag = splunk_searchtime_fields_tags["tag"]
        self.logger.info(f"Testing for tag {tag} with tag_query {tag_query}")

        record_property("Event_with", tag_query)
        record_property("tag", tag)
        record_property("is_tag_enabled", is_tag_enabled)

        index_list = (
            "(index="
            + " OR index=".join(splunk_search_util.search_index.split(","))
            + ")"
        )
        search = f"search {index_list} {tag_query} AND tag={tag}"
        search += COUNT_BY_SOURCE_TYPE_SEARCH_QUERY_PART

        self.logger.info(f"Search: {search}")

        result = splunk_search_util.checkQueryCountIsGreaterThanZero(
            search,
            interval=splunk_search_util.search_interval,
            retries=splunk_search_util.search_retry,
        )

        record_property("search", search)

        if is_tag_enabled:
            assert result, (
                f"No events found for the enabled Tag={tag}."
                f"\nsearch={search}"
                f"\ninterval={splunk_search_util.search_interval}, retries={splunk_search_util.search_retry}"
            )
        else:
            assert not result, (
                f"Events found for the disabled Tag={tag}."
                f"\nsearch={search}"
                f"\ninterval={splunk_search_util.search_interval}, retries={splunk_search_util.search_retry}"
            )

    @pytest.mark.splunk_searchtime_fields
    @pytest.mark.splunk_requirements
    @pytest.mark.splunk_searchtime_fields_datamodels
    def test_datamodels(
        self,
        splunk_search_util,
        splunk_ingest_data,
        splunk_setup,
        splunk_searchtime_fields_datamodels,
        record_property,
        caplog,
    ):
        """
        Test case to check tags mentioned in tags.conf

        This test case checks if a tag is assigned to the event if enabled,
        and also checks that a tag is not assigned to the event if disabled.

        Args:
            splunk_search_util (helmut_lib.SearchUtil.SearchUtil):
                object that helps to search on Splunk.
            splunk_searchtime_fields_datamodels (fixture): pytest parameters to test.
            record_property (fixture): pytest fixture to document facts of test cases.
            caplog (fixture): fixture to capture logs.
        """
        esacaped_event = splunk_searchtime_fields_datamodels["stanza"]
        datamodels = splunk_searchtime_fields_datamodels["datamodels"]
        self.logger.info(
            f"Testing for tag {datamodels} with tag_query {esacaped_event}"
        )

        record_property("Event_with", esacaped_event)
        record_property("datamodels", datamodels)

        index_list = (
            "(index="
            + " OR index=".join(splunk_search_util.search_index.split(","))
            + ")"
        )
        search = f"search {index_list} {esacaped_event} | fields *"

        self.logger.info(f"Search: {search}")

        fields_from_splunk = splunk_search_util.getFieldValuesDict(
            search,
            interval=splunk_search_util.search_interval,
            retries=splunk_search_util.search_retry,
        )

        extracted_tags = fields_from_splunk.get("tag", "")
        extracted_tags = extracted_tags.strip("][").split(", ")
        extracted_tags = [tag.replace("'", "") for tag in extracted_tags]

        extracted_datamodels = []
        for datamodel, tags in dict_datamodel_tag.items():
            if all(tag in extracted_tags for tag in tags):
                extracted_datamodels.append(datamodel)

        self.logger.debug(f"Tags extracted from Splunk {extracted_tags}")

        record_property("search", search)

        missing_datamodels = [dm for dm in datamodels if dm not in extracted_datamodels]
        wrong_datamodels = [dm for dm in extracted_datamodels if dm not in datamodels]

        self.logger.debug(
            f"List of missing tags {missing_datamodels}. List of wrongly assigned tags {wrong_datamodels}"
        )

        assert (
            missing_datamodels == [] and wrong_datamodels == []
        ), f"Tags were not assigned to event - missing tags {missing_datamodels} and/or too many tags found in splunk {wrong_datamodels}"

    @pytest.mark.splunk_searchtime_fields
    @pytest.mark.splunk_searchtime_fields_eventtypes
    def test_eventtype(
        self,
        splunk_search_util,
        splunk_ingest_data,
        splunk_setup,
        splunk_searchtime_fields_eventtypes,
        record_property,
        caplog,
    ):
        """
        Tests if all eventtypes in eventtypes.conf are generated in Splunk.

        Args:
            splunk_search_util (fixture):
                Fixture to create a simple connection to Splunk via SplunkSDK
            splunk_searchtime_fields_eventtypes (fixture):
                Fixture containing list of eventtypes
            record_property (fixture):
                Used to add user properties to test report
            caplog (fixture):
                Access and control log capturing

        Returns:
            Asserts whether test case passes or fails.
        """
        record_property("eventtype", splunk_searchtime_fields_eventtypes["stanza"])
        index_list = (
            "(index="
            + " OR index=".join(splunk_search_util.search_index.split(","))
            + ")"
        )
        search = (
            f"search {index_list} AND "
            f"eventtype="
            f"\"{splunk_searchtime_fields_eventtypes['stanza']}\""
        )
        search += COUNT_BY_SOURCE_TYPE_SEARCH_QUERY_PART

        self.logger.info(
            "Testing eventtype =%s", splunk_searchtime_fields_eventtypes["stanza"]
        )

        self.logger.info("Search query for testing =%s", search)

        # run search
        result = splunk_search_util.checkQueryCountIsGreaterThanZero(
            search,
            interval=splunk_search_util.search_interval,
            retries=splunk_search_util.search_retry,
        )
        record_property("search", search)
        assert result, (
            f"No result found for the search.\nsearch={search}\n"
            f"interval={splunk_search_util.search_interval}, retries={splunk_search_util.search_retry}"
        )

    @pytest.mark.splunk_searchtime_fields
    @pytest.mark.splunk_searchtime_fields_savedsearches
    def test_savedsearches(
        self,
        splunk_search_util,
        splunk_ingest_data,
        splunk_setup,
        splunk_searchtime_fields_savedsearches,
        record_property,
        caplog,
    ):
        """
        Tests if all savedsearches in savedsearches.conf are being executed properly to generate proper results.

        Args:
            splunk_search_util (fixture):
                Fixture to create a simple connection to Splunk via SplunkSDK
            splunk_searchtime_fields_savedsearches (fixture):
                Fixture containing list of savedsearches
            record_property (fixture):
                Used to add user properties to test report
            caplog (fixture):
                Access and control log capturing

        Returns:
            Asserts whether test case passes or fails.
        """
        search_query = splunk_searchtime_fields_savedsearches["search"]
        earliest_time = splunk_searchtime_fields_savedsearches["dispatch.earliest_time"]
        latest_time = splunk_searchtime_fields_savedsearches["dispatch.latest_time"]

        temp_search_query = search_query.split("|")
        if temp_search_query[0].find("savedsearch") == -1 and (
            len(temp_search_query) < 2 or temp_search_query[1].find("savedsearch") == -1
        ):
            temp_search_query[0] += " earliest_time = {0} latest_time = {1} ".format(
                earliest_time, latest_time
            )
            search_query = "|".join(temp_search_query)
            search = f"search {search_query}"
        else:
            search = "|".join(temp_search_query)

        self.logger.info(f"Search: {search}")

        result = splunk_search_util.checkQueryCountIsGreaterThanZero(
            search,
            interval=splunk_search_util.search_interval,
            retries=splunk_search_util.search_retry,
        )

        record_property("search", search)
        assert result, (
            f"No result found for the search.\nsearch={search}\n"
            f"interval={splunk_search_util.search_interval}, retries={splunk_search_util.search_retry}"
        )
