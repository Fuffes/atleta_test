from playwright.sync_api import sync_playwright, Page

class MetamaskPage:

    def __init__(self, page: Page):
        self.page = page

        # locators
        self.connect_btn = page.locator('//button[text()="Connect"]')
        self.confirm_btn = page.locator('//button[text()="Confirm"]')



    def confirm(self):
        self.confirm_btn.click()

    def connect(self):
        self.connect_btn.click()

