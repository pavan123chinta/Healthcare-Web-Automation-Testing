from pages.google_page import GooglePage


def test_open_google(driver):
    google_page = GooglePage(driver)
    google_page.open()
    assert "Google" in google_page.get_title()