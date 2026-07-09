#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:29:59 2026

@author: faaiz
"""

user_money = 15
final_buyable_item = [
    #[item, price, id]
    ["Stick", 1, 1],
    ["Bread", 5, 2],
    ["Sword", 10, 3],
    ["Shield", 14, 4]    
]

def list_shop():
    global user_money
    while True:
        for item, price, ids in final_buyable_item:
            print(f"[{ids}] {item} --- ${price}")

        selection = int(input("\n> "))
        
        for item, price, ids in final_buyable_item:
            if selection == ids:
                user_money -= price
                print(f"You purchased {item} for ${price}")
                print(f"Balance: {user_money}")
                break
            
        else:
            print("Goodbye!")        
        
            
list_shop()