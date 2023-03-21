from playwright.sync_api import Page
import config


class IndexPage:
    @staticmethod
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN_TEST)

    @staticmethod
    def text_on_buttom(self, page: Page) -> None:
        return page.locator('.layout-navbar-footer__info__role').text_content()

    @staticmethod
    def auth_manager(self, page: Page) -> None:
        page.get_by_test_id("input-email").click()
        page.get_by_test_id("input-email").fill("ManagerKA@test.test")
        page.get_by_test_id("input-loginform-password").click()
        page.get_by_test_id("input-loginform-password").fill("3mTh7XNcu")
        page.get_by_role("button", name="Войти").click()

    @staticmethod
    def auth_admin(self, page: Page) -> None:
        page.get_by_test_id("input-email").click()
        page.get_by_test_id("input-email").fill("AdminKA@test.test")
        page.get_by_test_id("input-loginform-password").click()
        page.get_by_test_id("input-loginform-password").fill("DBl7ytqOb")
        page.get_by_role("button", name="Войти").click()

    @staticmethod
    def auth_super_admin(self, page: Page) -> None:
        page.get_by_test_id("input-email").click()
        page.get_by_test_id("input-email").fill("admin@admin.com")
        page.get_by_test_id("input-loginform-password").click()
        page.get_by_test_id("input-loginform-password").fill("165Deploy")
        page.get_by_role("button", name="Войти").click()


