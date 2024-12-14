from playwright.sync_api import Page, expect

def test_visible_after_with_explicit_waits_with_playwright(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    expect(page.locator('//button[text()="Visible After 5 Seconds"]')).to_have_text('Visible After 5 Seconds')