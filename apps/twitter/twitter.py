from typing import Union

from playwright.sync_api import Page as _Page, Browser as _Browser
# Use this main file as a starting point and import the pages into this file to extend as below
# There is no need to use the import in this file but it makes them available
from apps.twitter.functions import twitter_login_page as login_page


def launch(page_or_browser: Union[Union[_Page, _Browser], None] = None):
    page = page_or_browser
    if isinstance(page_or_browser, _Browser):
        page = page_or_browser.new_page()
    else:
        page.goto("https://twitter.com/?lang=en")
    return page

