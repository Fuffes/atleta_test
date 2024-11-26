from playwright.sync_api import Page

from page_factory.button import Button


class WalletConnectModal:
    def __init__(self, page: Page) -> None:
        self.page = page

    #     MM button

        self.mm_btn = Button(page=page,locator="page.get_by_role("button", name="MetaMask MetaMask")")

    def connect_mm(self):
