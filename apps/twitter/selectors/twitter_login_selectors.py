username_input: str = "//input[@name='session[username_or_email]']"
password_input: str = "//input[@name='session[password]']"
login_button: str = "//div[@data-testid='LoginForm_Login_Button']"
signup_button: str = "//a[@data-testid='signupButton']"
signup_modal_name: str = "//input[@name='name']"
signup_modal_phone: str = "//input[@name='phone_number']"
signup_modal_email: str = "//input[@name='email']"
signup_modal_dob: list[str] = [
    "//select[@aria-label='Day']",
    "//select[@aria-label='Month']",
    "//select[@aria-label='Year']"
]
signup_modal_use_email_instead_link: str = "//span[text()='Use email instead']"
signup_modal_next_button: str = "//span[text()='Next']//ancestor::div[@role='button' and @data-focusable='true']"
