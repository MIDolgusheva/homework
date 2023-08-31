def test_homework(context):
    page = context.new_page()
    page.goto("https://cloud.ru/ru")
    page.locator("//li[@data-qa='header_nav_item'][text()='Сервисы']").click()
    page.locator("//div[contains(@class,'Products_menuItem')][text()='Инфраструктура']").click()
    page.locator('//h2[contains(@class,"Products_title")][text()="Инфраструктура"]/..//a['
                 '@href="/ru/products/oblachnyj-api-gateway-hosting"]').click()
    page.wait_for_selector("img[class*='Hero_shape']")
    current_url = page.url
    assert current_url == "https://cloud.ru/ru/products/oblachnyj-api-gateway-hosting", "страница не открылась"
