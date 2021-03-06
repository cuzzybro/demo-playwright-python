from playwright.sync_api import Page as _Page, Browser as _Browser
# Use this main file as a starting point and import the pages into this file to extend as below
# There is no need to use the import in this file but it makes them available
from apps.twitter.functions import twitter_login_page as login_page


# this function optionally takes in either a Page or Browser object from the playwright sync api
# it also return the page object that is either passed or built in this function
def launch(page: _Page = None, browser: _Browser = None):
    if browser is not None:
        page = browser.newPage()

    page.goto("https://twitter.com/?lang=en")
    return page

