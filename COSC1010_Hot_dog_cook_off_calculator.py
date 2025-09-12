#
# VictorByrd
# 9-11-2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import math

#constants
Hot_Dogs_Per_package = 10
Buns_Per_package = 8

#input
people = int(input("Enter the number of people attending: "))
Hot_Dogs_Per_person = int(input("Enter the number of hot dogs per person: "))

#total number of hot dogs needed
Total_hot_Dogs = people * Hot_Dogs_Per_person

# packages needed
Hot_Dog_packages = math.ceil(Total_hot_Dogs/Hot_Dogs_Per_package)
Bun_packages = math.ceil(Total_hot_Dogs/Buns_Per_package)

#leftovers
Leftovers_Hot_Dogs = Hot_Dog_packages * Hot_Dogs_Per_package-Total_hot_Dogs
Leftovers_Buns = Bun_packages * Buns_Per_package -Total_hot_Dogs

#output
print("\nResults:")
print(f"total hot dogs needed: {Total_hot_Dogs}")
print(f"hot dog packages needed: {Hot_Dog_packages}")
print(f"Buns packages needed: {Bun_packages}")
print(f"leftover hot dogs: {Leftovers_Hot_Dogs}")
print(f"levfover buns: {Leftovers_Buns}")