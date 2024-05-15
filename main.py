import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'language': 'en',
    'locale': 'US'
}

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.driver:
            cls.driver.quit()

    def click_button(self, by, value) -> None:
        el = self.driver.find_element(by=by, value=value)
        el.click()

    def delete_all(self) -> None:
        for _ in range(3):
            self.click_button(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="delete"]')

    def test_plus(self) -> None:
        self.click_button(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        self.click_button(AppiumBy.XPATH, '//android.widget.Button[@content-desc="plus"]')
        self.click_button(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        self.delete_all()

    def test_minus(self) -> None:
        self.click_button(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        self.click_button(AppiumBy.XPATH, '//android.widget.Button[@content-desc="minus"]')
        self.click_button(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        self.delete_all()

    def test_multiplication(self) -> None:
        self.click_button(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        self.click_button(AppiumBy.XPATH, '//android.widget.Button[@content-desc="×"]')
        self.click_button(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        self.delete_all()

    def test_divide(self) -> None:
        self.click_button(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        self.click_button(AppiumBy.XPATH, '//android.widget.Button[@content-desc="divide"]')
        self.click_button(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        self.delete_all()

if __name__ == '__main__':
    unittest.main()
