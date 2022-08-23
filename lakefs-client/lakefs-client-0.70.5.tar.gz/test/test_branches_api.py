"""
    lakeFS API

    lakeFS HTTP API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import lakefs_client
from lakefs_client.api.branches_api import BranchesApi  # noqa: E501


class TestBranchesApi(unittest.TestCase):
    """BranchesApi unit test stubs"""

    def setUp(self):
        self.api = BranchesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_branch(self):
        """Test case for create_branch

        create branch  # noqa: E501
        """
        pass

    def test_delete_branch(self):
        """Test case for delete_branch

        delete branch  # noqa: E501
        """
        pass

    def test_diff_branch(self):
        """Test case for diff_branch

        diff branch  # noqa: E501
        """
        pass

    def test_get_branch(self):
        """Test case for get_branch

        get branch  # noqa: E501
        """
        pass

    def test_list_branches(self):
        """Test case for list_branches

        list branches  # noqa: E501
        """
        pass

    def test_reset_branch(self):
        """Test case for reset_branch

        reset branch  # noqa: E501
        """
        pass

    def test_revert_branch(self):
        """Test case for revert_branch

        revert  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
