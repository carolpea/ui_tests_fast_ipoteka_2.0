from playwright.sync_api import Page, expect


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
    def add_a_new_policyholder(page: Page) -> None:
        policyholder = page.get_by_test_id("policyholder")
        policyholder.get_by_test_id("btn-dobavit_novogo").click()

