import os
from graphlib import TopologicalSorter
from typing import Generator

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from pages.mm import MetamaskPage
from pages.pool_page import PoolPage
from .configurations import extension_id_conf

MM_EXTENSION_PATH = "./MetaMask"
USER_DATA_DIR =  "./user_data"


@pytest.fixture(scope="session")
def context():
    """
    Fixture for launch browser with MetaMask installed
    """
    metamask_extension_path = os.path.abspath(MM_EXTENSION_PATH)
    user_data_dir = os.path.abspath(USER_DATA_DIR)


    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir,
            headless=False,
            args=[
                f"--disable-extensions-except={metamask_extension_path}",
                f"--load-extension={metamask_extension_path}",
            ],
        )
        yield browser
        browser.close()







# Metamask setup
@pytest.fixture(scope="session")
def extension_id(context) -> Generator[str, None, None]:
    background = context.service_workers[0]
    if not background:
        background = context.wait_for_event("serviceworker")

    extension_id = background.url.split("/")[2]
    yield extension_id



@pytest.fixture(scope="session")
def setup_MM(context, extension_id):
    load_dotenv()

    password = os.getenv('METAMASK_PASSWORD')
    key = os.getenv('METAMASK_KEY').split()

    # page = MetamaskPage(context.new_page())
    #
    # page.navigate(extension_id)

    page = context.new_page()
    page.goto(f"chrome-extension://{extension_id}/home.html")

    try:
        title = page.locator('//h1[text()= "Welcome back!"]')
        title.wait_for(timeout=3000)
        if title:
            page.locator('//input[@id = "password"]').fill(password)
            page.locator('//button[text() = "Unlock"]').click()
    except:
        print("not the setup")
        page.locator('//label[@for = "onboarding__terms-checkbox"]').click()
        page.locator('//button[text() = "Import an existing wallet"]').click()
        page.locator('//button[text() = "I agree"]').click()
        for enum in range(12):
            page.locator(f'.MuiInputBase-root >> input >> nth={enum}').fill(key[enum])
        page.locator('//button[text() = "Confirm Secret Recovery Phrase"]').click()
        page.locator('//*[@data-testid = "create-password-new"]').fill(password)
        page.locator('//*[@data-testid = "create-password-confirm"]').fill(password)
        page.locator('//span[@class = "mm-checkbox__input-wrapper"]').click()
        page.locator('//button[text() = "Import my wallet"]').click()
        page.locator('//button[text() = "Done"]').click()
        page.locator('//button[text() = "Next"]').click()
        page.locator('//button[text() = "Done"]').click()

    # finally: print("Done")
    print("Done")
    yield extension_id




# TODO add pages
@pytest.fixture(scope='function')
def pool_page(context) -> PoolPage:
    page = context.new_page()
    return PoolPage(page)


# @pytest.fixture(scope='function')
# def validators_page(context) -> ValidatorsPage:
#     page = context.new_page()
#     return PoolPage(page)