from apps.twitter import twitter


def test_twitter_register(browser):
    page = twitter.launch(None, browser)
    twitter.login_page.register(page)
