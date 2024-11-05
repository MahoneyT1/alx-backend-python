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

from client import GithubOrgClient, get_json
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
from unittest.mock import patch, PropertyMock, Mock
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
            url_to_verify = "https://api.github.com/orgs/google/repos"
            call_public_repos = result.public_repos()

            self.assertEqual(call_public_repos, url_to_verify)
            method_get_json.assert_called_once()

    @parameterized.expand([
        ({"repo": {"license": {"key": "my_license"}},
          "license_key": "my_license"}, True),
        ({"repo": {"license": {"key": "other_license"}},
          "license_key": "my_license"}, False)
    ])
    def test_has_license(self, repo_key, expected):
        """Implement TestGithubOrgClient.test_has_license to unit-test
        GithubOrgClient.has_license. Parametrize the test with the
        following inputs
        """
        # testing instance
        client = GithubOrgClient("google")

        # verify if args has license
        ans = client.has_license(repo_key['repo'], repo_key['license_key'])

        # assert that ans returns false
        self.assertEqual(ans, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """_summary_

    Args:
            unittest (_type_): _description_

    Returns:
            _type_: _description_
    """
    @classmethod
    def setUpClass(cls) -> None:
        """_summary_

        Returns:
                _type_: _description_
        """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """_summary_
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """_summary_
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """_summary_
        """
        cls.get_patcher.stop()
