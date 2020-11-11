from playwright import sync_playwright

with sync_playwright() as pw:
    browser = pw.firefox.launch(headless=False)
    context = browser.newContext()
    page = context.newPage()

    page.goto("https://demoqa.com/menu")

    browser.close()

