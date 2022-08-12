# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 19:19:18 2022

@author: Krystian
"""

class Warehouse:
    
    def __init__(self, listProducts):
        self.listProducts = listProducts
        
    def displayAvailableProducts(self):
        print('Available products:')
        for product in self.listProducts:
            print(product)
            
    def addProduct(self):
        self.nameProduct = input('Enter the names of the product: >>>')
        if self.nameProduct not in self.listProducts:
           self.listProducts.append(self.nameProduct)
           print(f'Product {self.nameProduct} added to warehouse.')
        else:
            print('The product is already on the list.')
        
    def deleteProduct(self):
        self.nameProduct = input('Enter the names of the products you want to remove from the list: >>> ')
        if self.nameProduct in self.nameProduct:
            self.listProducts.remove(self.nameProduct)
            print('Product removed from stock.')
        else:
            print('The specified product is not in stock.')
    