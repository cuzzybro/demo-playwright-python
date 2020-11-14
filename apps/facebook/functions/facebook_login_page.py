from playwright.sync_api import Page
from apps.facebook.selectors import facebook_login_selectors as _sel


def register_new_account(page: Page):
    (page.waitForSelector(_sel.create_new_account_button)).click()
    (page.waitForSelector(_sel.signup_modal_firstname_input)).fill("Automation firstname")
    (page.waitForSelector(_sel.signup_modal_surname_input)).fill("Automation lastname")
    page.type(_sel.signup_modal_mobile_email, "automation.test@msd.govt.nz")
    (page.waitForSelector(_sel.signup_modal_confirm_email)).fill("automation.test@msd.govt.nz")
    page.fill(_sel.signup_modal_password, "Password0!")
    page.selectOption(_sel.signup_modal_dob[0], "20")
    page.selectOption(_sel.signup_modal_dob[1], "12")
    page.selectOption(_sel.signup_modal_dob[2], "1988")
    page.click(_sel.signup_modal_gender("male"))
    page.click(_sel.signup_modal_signup_button)
