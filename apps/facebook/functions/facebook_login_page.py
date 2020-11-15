from playwright.sync_api import Page
from apps.facebook.selectors import facebook_login_selectors as _sel
from common.methods import random_string, random_email, get_date_offset_years


def register_new_account(page: Page):
    email = random_email()
    dob = str(get_date_offset_years(-27))
    (page.waitForSelector(_sel.create_new_account_button)).click()
    (page.waitForSelector(_sel.signup_modal_firstname_input)).fill(random_string(8))
    (page.waitForSelector(_sel.signup_modal_surname_input)).fill(random_string(8))
    page.type(_sel.signup_modal_mobile_email, email)
    (page.waitForSelector(_sel.signup_modal_confirm_email)).fill(email)
    page.fill(_sel.signup_modal_password, "Password0!")
    page.selectOption(_sel.signup_modal_dob[0], dob[0:2])
    page.selectOption(_sel.signup_modal_dob[1], dob[3:5])
    page.selectOption(_sel.signup_modal_dob[2], dob[6:10])
    page.click(_sel.signup_modal_gender())
    page.click(_sel.signup_modal_signup_button)
