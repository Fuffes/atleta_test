import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from src.parced_config import MM_EXTENSION_PATH, USER_DATA_DIR, MM_PASSWORD, MM_KEY



@pytest.fixture(scope="session")
def context():
    """
    Fixture for launch browser with MetaMask installed
    """
    metamask_extension_path = MM_EXTENSION_PATH.value
    user_data_dir = USER_DATA_DIR.value

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            args=[
                f"--disable-extensions-except={metamask_extension_path}",
                f"--load-extension={metamask_extension_path}",
            ],
        )
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def setup_MM(context):
    load_dotenv()
    password = MM_PASSWORD
    key = MM_KEY

    page = context.new_page()
    background = context.service_workers[0]
    if not background:
        background = context.wait_for_event("serviceworker")

    extension_id = background.url.split("/")[2]

    page.goto(f"chrome-extension://{extension_id}/home.html")

    try:
        title = page.locator('//h1[text()= "Welcome back!"]')
        title.wait_for(timeout=3000)
        if title:
            page.locator('//input[@id = "password"]').fill(password)
            page.locator('//button[text() = "Unlock"]').click()
    except: print("not the setup")

    finally:
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
