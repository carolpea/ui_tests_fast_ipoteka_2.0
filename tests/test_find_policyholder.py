from playwright.sync_api import expect
import re
import pages
import time


def test_find_policyholder(page):
    pages.index_page.open_index_page(page)
    pages.index_page.auth_manager(page)
    pages.base_page.create_applic(page)
    policyholder = page.get_by_test_id("policyholder")
    client = policyholder.get_by_test_id("sh-input-client_id")
    client_box = client.get_by_test_id("select-box-tags-client_id")
    client.get_by_test_id("select-box-tags-client_id").click()
    client.get_by_test_id("select-input-client_id").fill("Ошибков")
    rows = client.locator(".multiselect__content .multiselect__element")
    rows.first.click()
    modal_confirm = page.locator(".js-modal-confirm-content")
    expect(modal_confirm).to_be_visible()
    modal_confirm.get_by_role("button", name="нет").click()
    assert client_box.get_by_test_id("select-input-client_id").is_disabled(), 'object is not disabled'
    # assert client_box.get_by_label("123Ошибков**"), 'client not find' КАК СДЕЛАТЬ???


