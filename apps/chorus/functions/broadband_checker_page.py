from apps.chorus.functions.broadband_results_page import ResultsPage
from apps.chorus.selectors import broadband_checker as _sel
from playwright.sync_api import Page


class CheckerPage:

    page: Page

    def __init__(self, page: Page):
        self.page = page

    def enter_address(self, address: str):
        self.page.wait_for_load_state(state='domcontentloaded')
        self.page.wait_for_selector(_sel.address_input_field, state='attached').click()
        self.page.type(_sel.address_input_field, address, delay=50)
        return self

    def click_found_address(self):
        self.page.wait_for_selector("//div[@class='address-options-list-container']", state='attached', timeout=5000)
        self.page.wait_for_selector(_sel.address_option, state='attached').click()
        return ResultsPage(self.page)

