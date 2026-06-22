import pytest
# from conftest import performLogin
from data.testdata import TestData
from pages.inventory_page import inventory


# def test_load(driver, performLogin):
#     inventoryPage - inventory(driver)
#     # assert "inventory" in driver.title, f"Expected title not found. Got: {driver.title}"
    # filename = "inven.png"
    # file_path = TestData.folder_path + "\\" + filename  # manual path join
    # driver.save_screenshot(file_path)

#     assert inventoryPage.isProductName()
#     assert inventoryPage.isPricecorrect()
#     assert inventoryPage.isProductDesc()
#     assert inventoryPage.isProductImg()


#     assert "inventory" in driver.current_url

# inventory.isProductName()
# inventory.isPricecorrect()
# inventory.isProductDesc()
# inventory.isProductImg
# inventory.addtocard()

def test_load(driver, performLogin):

    inventory_page = inventory(driver)

    
    if "inventory" not in driver.current_url:
            filename = "inven.png"
            file_path = TestData.folder_path + "\\" + filename  # manual path join
            driver.save_screenshot(file_path)
            pytest.fail("Inventory not loaded")

    else:
          assert "inventory" in driver.current_url

    assert inventory_page.getAllProducts()
    assert inventory_page.getAllProductPrice()
    assert inventory_page.isProductDesc()
    assert inventory_page.isProductImg()