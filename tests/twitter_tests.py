from apps.twitter import twitter
from apps.facebook import facebook


def test_twitter_register(browser):
    page = twitter.launch(None, browser)
    twitter.login_page.register(page)


def test_twitter_register_another_way(browser):
    page = browser.newPage()
    twitter.launch(page)
    twitter.login_page.register(page)


def test_twitter_register_using_page(page):
    twitter.launch(page)
    twitter.login_page.register(page)
    facebook.launch(page)
    facebook.login_page.register_new_account(page)
    page.waitForTimeout(10000)
