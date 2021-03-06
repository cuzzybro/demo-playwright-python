from apps.twitter import twitter
from apps.facebook import facebook
from playwright import sync_playwright


def test_twitter_register(browser):  # browser argument is pytest fixture
    page = twitter.launch(None, browser)
    twitter.login_page.register(page)


def test_twitter_register_another_way(browser):
    page = browser.newPage()
    twitter.launch(page)
    twitter.login_page.register(page)


def test_twitter_register_using_page(page):  # page argument is pytest fixture
    twitter.launch(page)
    twitter.login_page.register(page)
    facebook.launch(page)
    facebook.login_page.register_new_account(page)
    page.waitForTimeout(10000)


def test_multi(browser):
    for each in range(2):
        page = browser.newPage()
        twitter.launch(page)
        twitter.login_page.register(page)
        page.close()


def test_stuff():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False)
    page = browser.newPage()
    twitter.launch(page)
    twitter.login_page.register(page)
    facebook.launch(page)
    facebook.login_page.register_new_account(page)
    page.waitForTimeout(10000)


