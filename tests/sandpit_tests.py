import logging
from apps.chorus import chorus
from apps.chorus.chorus import Chorus
from playwright.sync_api import sync_playwright


def test_verify_field_empty(page):
    page.goto("https://demoqa.com/automation-practice-form")
    field_content: str = page.text_content("//div[contains(@class, 'subjects-auto-complete__placeholder ')]")
    logging.info(f"the text content in the subjects field = '{field_content}'")
    assert field_content == ""


def test_chorus(page):
    page.goto("https://www.chorus.co.nz/broadband-map")
    page.click("//h3[text()='Broadband checker']")
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_selector("//input[@placeholder='Enter your address here']", state='attached', timeout=1000).click()
    with page.expect_response("") as resp:
        page.type("//input[@placeholder='Enter your address here']", "220 Tinakori Road", delay=20)
    page.wait_for_selector("//div[@class='address-options-list-container']//li", state='attached', timeout=1000).click()
    page.wait_for_load_state('networkidle')

    # breakpoint()


def test_chorus_functions(page):
    Chorus.open_checker_map(page)
    checker = Chorus.go_to_broadband_checker(page)
    options = checker.enter_address("220 Tinakori Road, Thorndon, Wellington").click_found_address().get_available_options()
    print(options)


def test_generated_code():
    with sync_playwright() as playwright:
        run2(playwright)


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.chorus.co.nz/broadband-map
    page.goto("https://www.chorus.co.nz/broadband-map")

    # Click h3:has-text("Broadband checker")
    page.click("h3:has-text(\"Broadband checker\")")
    # assert page.url == "https://www.chorus.co.nz/tools-support/broadband-tools/broadband-checker"

    # Click [placeholder="Enter your address here"]
    page.click("[placeholder=\"Enter your address here\"]")

    # Fill [placeholder="Enter your address here"]
    page.fill("[placeholder='Enter your address here']", "223 tinakori road")

    # Click text=223 Tinakori Road, Thorndon, Wellington
    page.click("text=223 Tinakori Road, Thorndon, Wellington")

    page.wait_for_timeout(5000)

    # ---------------------
    context.close()
    browser.close()


def run2(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    # Subscribe to "request" and "response" events.
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))

    with page.expect_response("https://www.google.co.nz/") as response_info:
        page.goto("https://google.co.nz")
    print(response_info.value.headers)
    print(response_info.value.body())
    browser.close()

