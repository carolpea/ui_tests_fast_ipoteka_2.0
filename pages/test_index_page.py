import time
import pytest
import pages

class TestFooter:

    def test_user_should_be_auth(self, page):
        pages.index_page.open_index_page(page)
        time.sleep(10)
