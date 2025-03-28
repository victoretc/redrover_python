from selene import browser, have


def test_visible_after_with_explicit_waits_with_selene():
    browser.open('https://demoqa.com/dynamic-properties')
    browser.element('//button[text()="Visible After 5 Seconds"]'). \
        should(have.exact_text('Visible After 5 Seconds'))
