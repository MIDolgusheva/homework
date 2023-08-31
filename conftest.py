import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="module")
def context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    yield context
    context.close()
    browser.close()