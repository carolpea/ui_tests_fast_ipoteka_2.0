import pages


class Create:

    def test_create_application(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.auth_manager(page)
        pages.base_page.create_applic(page)
        life_buttom = pages.application.check_buttom_life(page)
        assert life_buttom == 'sdhfkj', 'errior'
