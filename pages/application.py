import time

from playwright.sync_api import Page, expect
import random


def generate_phone_number():
    area_code = 999
    prefix = random.randint(100, 999)
    suffix = random.randint(1000, 9999)
    return f"({area_code}) {prefix}-{suffix}"


def generate_email():
    domains = ["example.com", "test.com", "sample.com"]
    username = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))
    domain = random.choice(domains)
    return f"{username}@{domain}"


def generate_int_series(num):
    b = 10 * 10 ** (num - 1)
    c = 10*10**num - 1
    return f"{random.randint(b, c)}"


class ApplicationStepOne:
    @staticmethod
    def clicked_button_life(page: Page) -> None:
        value = 0
        expect(page.get_by_test_id("btn-zhizn")).to_have_class('btn mb-3 btn-blue btn-sm btn-block')

    @staticmethod
    def clicked_button_property(page: Page) -> None:
        expect(page.get_by_test_id("btn-imushchestvo")).to_have_class('btn mb-3 btn-orange btn-sm btn-block')

    @staticmethod
    def clicked_button_titul(page: Page) -> None:
        expect(page.get_by_test_id("btn-titul")).to_have_class('btn mb-3 btn-outline-gray btn-sm btn-block')

    @staticmethod
    def button_add_a_new_policyholder(page: Page) -> None:
        policyholder = page.get_by_test_id("policyholder")
        policyholder.get_by_test_id("btn-dobavit_novogo").click()

    @staticmethod
    def policyholder_fill(page: Page) -> None:
        policyholder = page.get_by_test_id("policyholder")
        policyholder.get_by_test_id("btn-dobavit_novogo").click()
        modal = page.get_by_test_id("modal-client")
        modal.get_by_test_id("input-last_name").click()
        modal.get_by_test_id("input-last_name").fill("Иванов")
        modal.get_by_test_id("input-first_name").click()
        modal.get_by_test_id("input-first_name").fill("Иван")
        modal.get_by_test_id("input-middle_name").click()
        modal.get_by_test_id("input-middle_name").fill("Иванович")
        modal.get_by_test_id("date-input-birthdate_formatted").click()
        modal.get_by_test_id("date-input-birthdate_formatted").fill("24121997")
        modal.get_by_test_id("input-birthplace").click()
        modal.get_by_test_id("input-birthplace").fill("Москва")
        modal.get_by_test_id("input-mobile_phone").click()
        modal.get_by_test_id("input-mobile_phone").fill(generate_phone_number())
        modal.get_by_test_id("input-email").click()
        modal.get_by_test_id("input-email").fill(generate_email())
        modal.get_by_test_id("rb-option-0-sex").click()
        modal.get_by_test_id("input-passport_serial").click()
        modal.get_by_test_id("input-passport_serial").fill(generate_int_series(4))
        modal.get_by_test_id("input-passport_number").click()
        modal.get_by_test_id("input-passport_number").fill(generate_int_series(6))
        modal.get_by_test_id("input-passport_issued_code").click()
        modal.get_by_test_id("input-passport_issued_code").fill(generate_int_series(6))
        modal.get_by_test_id("input-passport_issued_by").click()
        modal.get_by_test_id("input-passport_issued_by").fill("УВД города Москвы")
        modal.get_by_test_id("date-input-passport_issued_date_formatted").click()
        modal.get_by_test_id("date-input-passport_issued_date_formatted").fill("02.03.2018")
        modal.get_by_test_id("select-address_registration").click()
        modal.page.get_by_test_id("select-input-address_registration").fill("красная пресня 24 5")
        modal.page.get_by_text("г Москва, ул Красная Пресня, д 24, кв 5").click()
        modal.get_by_text("Совпадает с фактическим адресом").click()
        modal.get_by_text("Совпадает с фактическим адресом").click()



    @staticmethod
    def choose_bank_vtb(page: Page) -> None:
        page.get_by_test_id("select-bank_code").click()
        page.get_by_test_id("select-option-bank_code-vtb").click()


    @staticmethod
    def choose_bank_sber(page: Page) -> None:
        page.get_by_test_id("select-bank_code").click()
        page.get_by_test_id("select-option-bank_code-sber").click()


    @staticmethod
    def find_policyholder_without_anketa(page: Page) -> None:
        policyholder = page.get_by_test_id("policyholder")
        client = policyholder.get_by_test_id("sh-input-client_id")
        client.get_by_test_id("select-box-tags-client_id").click()
        client.get_by_test_id("select-input-client_id").fill("Ошибков")
        rows = client.locator(".multiselect__content .multiselect__element")
        oshibka = page.locator("xpath=//ul[@class='multiselect__content']//*[contains(text(), 'Ошибков')])[1]")
        oshibka.hover()
        oshibka.click()
        # time.sleep(5)
        # assert rows == 1, rows
        # elements = page.query_selector_all(".multiselect__content .multiselect__element")
        # count = elements.count()
        # assert count == -1, count
        # count = rows.count()
        # assert count > 0
        # rows.first.click()
        modal_confirm = page.locator(".js-modal-confirm-content")
        modal_confirm.get_by_role("button", name="нет").click()

    @staticmethod
    def fill_credit_contract_block_sber(page: Page) -> None:
        credit_contract = page.get_by_test_id("credit-contract")
        credit_contract.get_by_test_id("input-mortgage_amount").fill("1234567.78")
        page.get_by_test_id("select-box-tags-locality").get_by_text("Выберите значение").click()
        # locality = credit_contract.page.get_by_test_id("select-input-locality")
        page.get_by_test_id("select-input-locality").fill("Москва")
        # rows = locality.locator(".multiselect__content .multiselect__element")
        # rows.first.click()
        credit_contract.get_by_test_id("select-input-locality").fill("москва")
        credit_contract.get_by_test_id("select-option-locality-0").click()

