import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_plus(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.Button[@content-desc="plus"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

    def test_minus(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.Button[@content-desc="minus"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

    def test_multiplication(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.Button[@content-desc="×"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

    def test_divide(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.Button[@content-desc="divide"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

if __name__ == '__main__':
    unittest.main()