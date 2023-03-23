import pages
import time


def test_create_policyholder(page):
    pages.index_page.open_index_page(page)
    pages.index_page.auth_manager(page)
    pages.base_page.create_applic(page)
    time.sleep(10)
    pages.application.add_a_new_policyholder(page)
    modal = page.get_by_test_id("modal-client")


class Create:
    pass
