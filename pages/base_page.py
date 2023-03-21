from playwright.sync_api import Page
import config


class BasePage:
    @staticmethod
    def create_applic(page: Page) -> None:
        page.get_by_test_id("btn-sozdat").click()
        page.get_by_test_id("btn-podtverdit").click()
