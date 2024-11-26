import time

from playwright.sync_api import expect

from pages.pool_page import PoolPage
from pages.mm import MetamaskPage



def test_first_connect(context, pool_page, setup_MM):
    pool_page.navigate(pool_page.url)
    pool_page.connect_btn.click()

    # dapp_page.navigate(dapp_page.url)
    # dapp_page.connect_wallet()

    with context.expect_page() as new_page_info:
        mm_page = MetamaskPage(new_page_info.value)
        try: mm_page.connect()
        finally: mm_page.confirm()

    print("ffff")
    expect(dapp_page.address_icon).to_be_visible()


    time.sleep(120000)