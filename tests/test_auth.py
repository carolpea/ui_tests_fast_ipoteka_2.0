import pages


class TestFooter:

    def test_auth(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.auth_manager(page)
        page.get_by_role("button", name="АМ Анастасия Менеджер Менеджер").click()
        text_on_buttomm = pages.index_page.text_on_buttom(page)
        assert text_on_buttomm == 'Менеджер', 'error manager auth'
        page.get_by_role("button", name="Выход").click()
        pages.index_page.auth_admin(page)
        page.get_by_role("button", name="АА Анастасия Админ Администратор системы").click()
        text_on_buttomm = pages.index_page.text_on_buttom(page)
        assert text_on_buttomm == 'Администратор системы', 'error admin auth'
        page.get_by_role("button", name="Выход").click()
        pages.index_page.auth_super_admin(page)
        page.get_by_role("button", name="АС Админ Супер Администратор системы").click()
        text_on_buttomm = pages.index_page.text_on_buttom(page)
        assert text_on_buttomm == 'Администратор системы', 'error super_admin auth'
        page.get_by_role("button", name="Выход").click()


