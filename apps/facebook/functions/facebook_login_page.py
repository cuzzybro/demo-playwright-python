from playwright.sync_api import Page
from apps.facebook.selectors import facebook_login_selectors as _sel
from common.methods import random_string, random_email, get_date_offset_years, ClientData


def register_new_account(page: Page):
    client = ClientData()
    dob = str(get_date_offset_years(-27))
    (page.wait_for_selector(_sel.create_new_account_button)).click()
    (page.wait_for_selector(_sel.signup_modal_firstname_input)).fill(client.first_name)
    (page.wait_for_selector(_sel.signup_modal_surname_input)).fill(client.last_name)
    page.type(_sel.signup_modal_mobile_email, client.email)
    page.wait_for_selector(_sel.signup_modal_confirm_email).fill(client.email)
    page.fill(_sel.signup_modal_password, "Password0!")
    page.select_option(_sel.signup_modal_dob[0], dob[0:2])
    page.select_option(_sel.signup_modal_dob[1], dob[3:5])
    page.select_option(_sel.signup_modal_dob[2], dob[6:10])
    page.click(_sel.signup_modal_gender())
    page.click(_sel.signup_modal_signup_button)
