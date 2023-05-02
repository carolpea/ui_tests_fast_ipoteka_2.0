import time
from playwright.sync_api import expect
import pages
import re


def test_check_validation_all_risks_sber(page):
    pages.index_page.open_index_page(page)
    pages.index_page.auth_manager(page)
    pages.base_page.create_applic(page)
    page.get_by_test_id("btn-rasschitat").click()
    credit_contract = page.get_by_test_id("credit-contract")
    policyholder = page.get_by_test_id("policyholder")
    #проверяем первичную валидацию
    expect(credit_contract.get_by_test_id("input-mortgage_amount")).to_have_class(re.compile(r"is-invalid"))
    expect(credit_contract.get_by_test_id("select-bank_code")).to_have_class(re.compile(r"is-invalid"))
    expect(credit_contract.get_by_test_id("select-locality")).to_have_class(re.compile(r"is-invalid"))
    expect(page.get_by_test_id("input-interest_rate")).to_have_class(re.compile(r"is-invalid"))
    expect(credit_contract.get_by_test_id("sh-input-insurance_term")).to_have_class(re.compile(r"is-invalid"))
    expect(credit_contract.get_by_test_id("date-input-mortgage_agreement_date")).to_have_class(re.compile(r"is-valid"))
    expect(credit_contract.get_by_test_id("date-input-insurance_start_date")).to_have_class(re.compile(r"is-valid"))
    expect(credit_contract.get_by_test_id("date-input-insurance_end_date")).to_have_class(re.compile(r"is-valid"))
    expect(policyholder.get_by_test_id("select-client_id")).to_have_class(re.compile(r"is-invalid"))
    # работа со сбером
    #заполняем поля, которые выше были не валидны
    pages.application.choose_bank_sber(page)
    pages.application.fill_credit_contract_block_sber(page)
    client = policyholder.get_by_test_id("sh-input-client_id")
    pages.application.find_policyholder_without_anketa(page)
    page.get_by_test_id("btn-imushchestvo").click()
    page.get_by_test_id("btn-titul").click()
    page.get_by_test_id("btn-rasschitat").click()
    life = page.get_by_test_id("life")
    expect(life.get_by_test_id("input-height")).to_have_class(re.compile(r"is-invalid"))
    expect(life.get_by_test_id("input-weight")).to_have_class(re.compile(r"is-invalid"))
    expect(life.get_by_test_id("input-part")).to_be_disabled()
    expect(life.get_by_test_id("input-total_area")).to_have_class(re.compile(r"is-invalid"))
    expect(life.get_by_test_id("select-raw_address")).to_have_class(re.compile(r"is-invalid"))
    expect(life.get_by_test_id("input-insurance_term")).to_have_class(re.compile(r"is-invalid"))
    expect(life.get_by_test_id("input-cadastral_number")).to_have_class(re.compile(r"is-invalid"))


