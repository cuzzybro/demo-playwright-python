from playwright.sync_api import Page
from apps.twitter.selectors import twitter_login_selectors as _sel


def register(page: Page):
    (page.waitForSelector(_sel.signup_button)).click()
    (page.waitForSelector(_sel.signup_modal_use_email_instead_link)).click()
    page.fill(_sel.signup_modal_name, "Automation")
    page.fill(_sel.signup_modal_email, "my.email@automation.com")
    page.selectOption(_sel.signup_modal_dob[1], "12")
    page.selectOption(_sel.signup_modal_dob[0], "20")
    page.selectOption(_sel.signup_modal_dob[2], "1990")
    (page.waitForSelector(_sel.signup_modal_next_button)).click()

