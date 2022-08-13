# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 19:19:18 2022

@author: Krystian
"""

import sys

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
        if self.nameProduct in self.listProducts:
            self.listProducts.remove(self.nameProduct)
            print('Product removed from stock.')
        else:
            print('The specified product is not in stock.')
            
warehouse = Warehouse(['milk', 'water', 'eggs'])

while True:
    print('\n')
    print('Enter 1 to display the stock status.')
    print('Enter 2 to add a product.')
    print('Enter 3 to remove the product.')
    print('Enter 4 to finish.')
    userSelect = int(input('>>> '))
    if userSelect == 1:
        warehouse.displayAvailableProducts()
    elif userSelect == 2:
        warehouse.addProduct()
    elif userSelect == 3:
        warehouse.deleteProduct()
    elif userSelect == 4:
        sys.exit()

    