import pages
import time


def test_create_application(page):
    pages.index_page.open_index_page(page)
    pages.index_page.auth_manager(page)
    pages.base_page.create_applic(page)
    time.sleep(10)
    pages.application.clicked_button_life(page)
    page.get_by_test_id("btn-zhizn").click()
    page.get_by_test_id("btn-titul").click()
    pages.application.clicked_button_titul(page)
    page.get_by_test_id("btn-imushchestvo").click()
    pages.application.clicked_button_property(page)


class Create:
    pass
