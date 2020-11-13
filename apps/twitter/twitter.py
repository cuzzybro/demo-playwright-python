from playwright.sync_api import Page, Browser
from apps.twitter.functions import twitter_login_page as login_page


def launch(page: Page = None, browser: Browser = None):

    if browser is not None:
        page = browser.newPage()

    page.goto("https://twitter.com/?lang=en")
    return page

