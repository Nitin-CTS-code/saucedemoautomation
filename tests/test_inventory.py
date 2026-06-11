import pytest
from conftest import performLogin
from data.testdata import TestData
from pages.inventory_page import inventory


def test_load(driver, performLogin):
    # assert "inventory" in driver.title, f"Expected title not found. Got: {driver.title}"
    filename = "inven.png"
    file_path = TestData.folder_path + "\\" + filename  # manual path join
    driver.save_screenshot(file_path)


    assert "inventory" in driver.current_url