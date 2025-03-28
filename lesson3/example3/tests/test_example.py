from playwright.sync_api import Page, expect, sync_playwright


def test_visible_after_with_explicit_waits_with_playwright(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    expect(page.locator('//button[text()="Visible After 5 Seconds"]')).to_have_text('Visible After 5 Seconds')


def test_my_visible_after_with_explicit_waits_with_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://demoqa.com/dynamic-properties')
        expect(page.locator('//button[text()="Visible After 5 Seconds"]')).to_have_text('Visible After 5 Seconds',
                                                                                        timeout=15000)
        browser.close()
