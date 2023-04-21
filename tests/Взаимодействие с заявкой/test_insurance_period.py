from playwright.sync_api import expect
import pages
import re


def test_insurance_period(page):
    pages.index_page.open_index_page(page)
    pages.index_page.auth_manager(page)
    pages.base_page.create_applic(page)
    #работа со сбером
    pages.application.choose_bank_sber(page)
    expect(page.get_by_test_id("date-insurance_end_date")).to_have_class(re.compile(r"mx-datepicker disabled is-valid"))
    # работа с втб
    pages.application.choose_bank_vtb(page)
    expect(page.get_by_test_id("date-insurance_end_date")).to_have_class(re.compile(r"mx-datepicker disabled is-valid"))

