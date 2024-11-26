from playwright.sync_api import sync_playwright, Page, Browser
from tests.configurations import extension_id_conf

class MetamaskPage:

    def __init__(self, page: Page ):
        self.page = page

        # locators
        #     btn
        self.connect_btn = page.locator('//button[text()="Connect"]')
        self.confirm_btn = page.locator('//button[text()="Confirm"]')
        self.password_btn = page.locator('//button[text() = "Unlock"]')

        self.onbording_checkBox = page.locator('//label[@for = "onboarding__terms-checkbox"]')
        self.welcom_back_title = page.locator('//h1[text()= "Welcome back!"]')




    def navigate(self, extension_id):
        self.page.goto(f"chrome-extension://{extension_id}/home.html")

    def confirm(self):
        self.confirm_btn.click()

    def connect(self):
        self.connect_btn.click()

    def fill_in_password(self, password):
        self.password_btn.fill(password)


