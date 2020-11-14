username_input: str = "#email"
password_input: str = "#pass"
login_button: str = "#u_0_b"
forgot_password_link: str = "//a[text()='Forgotten password?']"
create_new_account_button: str = "//a[@data-testid='open-registration-form-button']"

signup_modal_firstname_input: str = "//input[@name='firstname']"
signup_modal_surname_input: str = "//input[@name='lastname']"
signup_modal_mobile_email: str = "//input[@name='reg_email__']"
signup_modal_confirm_email: str = "//input[@name='reg_email_confirmation__']"
signup_modal_password: str = "//input[@name='reg_passwd__']"

signup_modal_dob: list[str] = [
    "//select[@aria-label='Day']",
    "//select[@aria-label='Month']",
    "//select[@aria-label='Year']"
]


def signup_modal_gender(male_female_custom: str = "male"):
    if male_female_custom.lower() == "female":
        return "//label[text()='Female']/following-sibling::input"
    elif male_female_custom.lower() == "male":
        return "//label[text()='Male']/following-sibling::input"
    elif male_female_custom.lower() == "custom":
        return "//label[text()='Custom']/following-sibling::input"


signup_modal_signup_button: str = "//button[@name='websubmit']"
