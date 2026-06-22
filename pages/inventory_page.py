# https://www.saucedemo.com/inventory.html
import logging

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class inventory(BasePage):
    
    #filter
    #product card
    #product name, descripiton,image, price
    #product add/remove
    #count update
    #product view

    #locators
    product_name = (By.CLASS_NAME,"inventory_item_name")
    product_desc = (By.CLASS_NAME,"inventory_item_desc")
    product_image = (By.CLASS_NAME,"inventory_item_img")
    product_price = (By.CLASS_NAME,"inventory_item_price")
    # Addtocart_btn = (By.CLASS_NAME,"add-to-cart-sauce-labs-backpack") #targetting specifc product
    removefromcart_btn = (By.CLASS_NAME,"")

    # def getAllProducts():
    #     return
    
    def isProductName(self):
        return self.isVisible(self.product_name)
    
    def isProductDesc(self):
        return self.isVisible(self.product_desc)
    
    def isProductImg(self):
        return self.isVisible(self.product_image)
    
    def isPricecorrect(self):
        return self.isVisible(self.product_price)
    
    # def addtocard(self):
    #     return self.isVisible(self.Addtocart_btn)
    
    # def removefromcard(self):
    #     self.click(self.Addtocart_btn)
    #     return self.isVisible(self.removefromcart_btn)

    # def getAllProducts(self):
    #     return self.isVisibleAll(self.product_name)
    
    def getAllProducts(self):
        products = self.findAll(self.product_name)
        print(f"Total products found: {len(products)}")
        return self.isVisibleAll(self.product_name)
    
    def getAllProductPrice(self):
        price = self.findAll(self.product_price)
        print("total price: ", {len(price)})
        return self.isVisibleAll(self.product_price)