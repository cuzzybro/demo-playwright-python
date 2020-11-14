from playwright.sync_api import Page as _Page, Browser as _Browser
from apps.facebook.functions import facebook_login_page as login_page


def launch(page: _Page = None, browser: _Browser = None):

    if browser is not None:
        page = browser.newPage()

    page.goto("https://facebook.com")

    return page
