from playwright.sync_api import Page
from apps.twitter.selectors import twitter_login_selectors as _sel
from common.methods import ClientData


def register(page: Page):
    client = ClientData()
    page.wait_for_selector(_sel.signup_button).click()
    page.wait_for_selector(_sel.signup_modal_use_email_instead_link).click()
    page.fill(_sel.signup_modal_name, f"{client.first_name} {client.last_name}")
    page.fill(_sel.signup_modal_email, f"{client.email}")
    page.select_option(_sel.signup_modal_dob[1], "12")
    page.select_option(_sel.signup_modal_dob[0], "20")
    page.select_option(_sel.signup_modal_dob[2], "1990")
    page.wait_for_selector(_sel.hidden_next_btn, state='hidden', timeout=2000)
    page.click(_sel.signup_modal_next_button)

