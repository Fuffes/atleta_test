from playwright.sync_api import Page

class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://katleta-app.quark.blue/"



        self.connect_btn = page.locator('//button[text() = "Connect"]')
        self.mm_option_btn = page.get_by_role("button", name="MetaMask MetaMask")

        #Staking subheader
        self.pool_tab = page.locator('//a[text() = "Pools"]')
        self.validators_tab = page.locator('//a[text() = "Validators"]')
        self.nominate_tab = page.locator('//a[text() = "Nominate"]')

    def connect_wallet(self):
        self.connect_btn.click()
        self.mm_option_btn.click()

    def navigate(self, url):
        self.page.goto(self.base_url+url)