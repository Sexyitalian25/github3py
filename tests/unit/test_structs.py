from .helper import UnitHelper
from github3.structs import GitHubIterator

import mock


class TestGitHubIterator(UnitHelper):
    described_class = GitHubIterator

    def create_instance_of_described_class(self):
        self.url = 'https://api.github.com/users'
        klass = lambda *args: args
        instance = self.described_class(count=-1, url=self.url, cls=klass,
                                        session=self.session)
        return instance

    def test_sets_per_page_to_100(self):
        """Test that the Iterator defaults the per_page parameter to 100"""
        self.session.get.return_value = mock.Mock(status_code=200,
                                                  json=lambda: [],
                                                  links={})

        for i in self.instance:
            break

        self.session.get.assert_called_once_with(
            self.url, params={'per_page': 100}, headers={}
            )
