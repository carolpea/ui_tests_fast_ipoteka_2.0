from playwright.sync_api import expect
import re

import pages
import time


def test_policyholder_validation(page):
    pages.index_page.open_index_page(page)
    pages.index_page.auth_manager(page)
    pages.base_page.create_applic(page)
    pages.application.add_a_new_policyholder(page)
    modal = page.get_by_test_id("modal-client")
    modal.get_by_test_id("btn-sokhranit").click()
    # Фамилия
    expect(modal.get_by_test_id("input-last_name")).to_have_class(re.compile(r"is-invalid"))
    # Имя
    expect(modal.get_by_test_id("input-first_name")).to_have_class(re.compile(r"is-invalid"))
    # Дата рождения
    expect(modal.get_by_test_id("date-input-birthdate_formatted")).to_have_class(re.compile(r"is-invalid"))
    # Место рождения
    expect(modal.get_by_test_id("input-birthplace")).to_have_class(re.compile(r"is-invalid"))
    # Мобильный телефон
    expect(modal.get_by_test_id("input-mobile_phone")).to_have_class(re.compile(r"is-invalid"))
    # Email
    expect(modal.get_by_test_id("input-email")).to_have_class(re.compile(r"is-invalid"))
    # Пол
    # expect(modal.get_by_test_id("rb-option-0-sex"))
    expect(modal.get_by_test_id("rb-sex")).to_have_class(re.compile(r"is-invalid"))
    # Паспорт
    # Серия
    expect(modal.get_by_test_id("input-passport_serial")).to_have_class(re.compile(r"is-invalid"))
    # Номер
    expect(modal.get_by_test_id("input-passport_number")).to_have_class(re.compile(r"is-invalid"))
    # Код подразделения
    expect(modal.get_by_test_id("input-passport_issued_code")).to_have_class(re.compile(r"is-invalid"))
    # Кем выдан
    expect(modal.get_by_test_id("input-passport_issued_by")).to_have_class(re.compile(r"is-invalid"))
    # Дата выдачи
    expect(modal.get_by_test_id("date-passport_issued_date_formatted")).to_have_class(re.compile(r"is-invalid"))
    # Адрес регистрации
    expect(modal.get_by_test_id("select-address_registration")).to_have_class(re.compile(r"is-invalid"))
    # Адрес фактический
    expect(modal.get_by_test_id("select-address_residence")).to_have_class(re.compile(r"is-invalid"))
    # modal.get_by_test_id("__BVID__13415").click()
    modal.get_by_text("Совпадает с фактическим адресом").click()
    expect(modal.get_by_test_id("select-address_residence")).to_have_class(re.compile(r"is-invalid"))
    expect(modal.get_by_test_id("input-middle_name")).to_have_class(re.compile(r"is-valid"))

