#!/usr/bin/env python3
"""Familiarize yourself with the client.GithubOrgClient class.
In a new test_client.py file, declare the TestGithubOrgClient
(unittest.TestCase) class and implement the test_org method.

This method should test that GithubOrgClient.org returns the
correct value.Use @patch as a decorator to make sure get_json
is called once with the expected argument but make sure it is
not executed.

Use @parameterized.expand as a decorator to parametrize the
test with a couple of org examples to pass to GithubOrgClient,
in this order:
google
abc
Of course, no external HTTP calls should be made.
"""

from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""
    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': "abc"})
    ])
    @patch.object(GithubOrgClient, 'org')
    def test_org(self, attribute_org, expected, mock_instance):
        """Tests if GithubOrgClient.org method returns the expected
        return value which is calling the get_json in utils file
        """

        mock_instance.return_value = expected
        my_instance = GithubOrgClient(org_name=attribute_org)

        result = my_instance.org()

        self.assertEqual(result, expected)
        mock_instance.assert_called_once()

    def test_public_repos_url(self):
        """ memoize turns methods into properties. Read up on how
        to mock a property (see resource).

        Implement the test_public_repos_url method to unit-test
        GithubOrgClient._public_repos_url. Use patch as a context
        manager to patch GithubOrgClient.org and make it return a
        known payload. Test that the result of _public_repos_url
        is the expected one based on the mocked payload.
        """

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock)\
                as get_github_attrr:
            url = 'https://api.github.com/orgs/google/repos'
            get_github_attrr.return_value = url

            instance_of_GithClient = GithubOrgClient("google")
            result = instance_of_GithClient._public_repos_url
            self.assertEqual(result, url)
