from playwright.sync_api import Page, Response

from page_factory.button import Button


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://katleta-app.quark.blue/"


        # Header
        self.connect_btn = Button(page, locator='//button[text() = "Connect"]', name= 'Connect')
        self.wallet_connect_modal = WalletConnectModal


    def navigate(self, url: str) -> Response | None:
        return self.page.goto(self.base_url+url, wait_until='networkidle')

    def reload(self) -> Response | None:
        return self.page.reload(wait_until='domcontentloaded')
    #     self.address_icon = page.locator('//button[@class = "Connect_connectButton__U5Rst"]')
    #     self.mm_option_btn = page.get_by_role("button", name="MetaMask MetaMask")
    #
    #     #Staking subheader
    #     self.pool_tab = page.locator('//a[text() = "Pools"]')
    #     self.validators_tab = page.locator('//a[text() = "Validators"]')
    #     self.nominate_tab = page.locator('//a[text() = "Nominate"]')
    #
    # def connect_wallet(self):
    #     self.connect_btn.click()
    #     self.mm_option_btn.click()
    #
