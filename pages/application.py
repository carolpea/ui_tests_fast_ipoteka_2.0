from playwright.sync_api import Page, Locator


class ApplicationStepOne:
    @staticmethod
    def check_buttom_life(self, page: Page) -> Locator:
        return page.locator('.btn mb-3 btn-blue btn-sm btn-block')
