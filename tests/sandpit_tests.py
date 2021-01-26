import logging


def test_verify_field_empty(page):
    page.goto("https://demoqa.com/automation-practice-form")
    field_content: str = page.textContent("//div[contains(@class, 'subjects-auto-complete__placeholder ')]")
    logging.info(f"the text content in the subjects field = '{field_content}'")
    assert field_content == ""

