from playwright.sync_api import Page

from apps.chorus import functions as _func

CheckerPage = _func.CheckerPage
ResultsPage = _func.ResultsPage

broadband_checker: str = "//h3[text()='Broadband checker']"


class Chorus:

    @staticmethod
    def open_checker_map(page: Page):
        page.goto("https://www.chorus.co.nz/broadband-map")

    @staticmethod
    def go_to_broadband_checker(page: Page):
        page.wait_for_selector(broadband_checker, state='attached', timeout=5000).click()
        return CheckerPage(page)