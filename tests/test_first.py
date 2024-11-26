import time

from playwright.sync_api import expect

from pages.pool_page import PoolPage
from src.mm import MetamaskPage



def test_first_connect(context, setup_MM):

    dapp_page = PoolPage(context.new_page())
    dapp_page.navigate(dapp_page.url)


    with context.expect_page() as new_page_info:


        mm_page = MetamaskPage(new_page_info.value)
        mm_page.connect()
        mm_page.confirm()

    expect(dapp_page.locator('//button[@class = "Connect_connectButton__U5Rst"]')).to_be_visible()


    time.sleep(120000)