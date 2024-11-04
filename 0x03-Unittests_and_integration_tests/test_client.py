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
            url = "https://api.github.com/users/google/repos",
            get_github_attrr.return_value = url

            self.assertEqual(GithubOrgClient("google")._public_repos_url, url)

    def test_public_repos(self):
        """Implement TestGithubOrgClient.test_public_repos to
        unit-test GithubOrgClient.public_repos.
        Use @patch as a decorator to mock get_json and make it
        return a payload of your choice.

        Use patch as a context manager to mock GithubOrgClient
        ._public_repos_url and return a value of your choice.
        Test that the list of repos is what you expect from the
        chosen payload.

        Test that the mocked property and the mocked get_json
        was called once.
        """

        with patch.object(GithubOrgClient, "public_repos") as method_get_json:
            result = GithubOrgClient("google")

            method_get_json.return_value = result._public_repos_url
            url = "https://api.github.com/orgs/google/repos"
            ans = result.public_repos()

            self.assertEqual(ans, url)
            method_get_json.assert_called_once()
