from playwright.sync_api import expect
import pages
import time


def test_policyholder_fill_and_save(page):
    pages.index_page.open_index_page(page)
    pages.index_page.auth_manager(page)
    pages.base_page.create_applic(page)
    pages.application.policyholder_fill(page)
    modal = page.get_by_test_id("modal-client")
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    modal.page.get_by_test_id("btn-sokhranit").click()




