import pages
import time


def test_create_application(page):
    pages.index_page.open_index_page(page)
    pages.index_page.auth_manager(page)
    pages.base_page.create_applic(page)
    time.sleep(10)
    life_button = pages.application.check_buttom_life(page)
    assert life_button == 'sdhfkj', 'errior'



class Create:
    pass
