def test_abre_saucedemo(driver):
    driver.get("https://www.saucedemo.com")
    assert driver.title == "Swag Labs"