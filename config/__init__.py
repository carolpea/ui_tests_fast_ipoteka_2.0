from config.url import Url
from config.expectations import Expectations
from config.playwright import Playwright
from pages import BasePage, ApplicationStepOne
from pages.index_page import IndexPage


url = Url()
playwright = Playwright()
expectations = Expectations()
index_page = IndexPage()
base_page = BasePage()
application = ApplicationStepOne()
