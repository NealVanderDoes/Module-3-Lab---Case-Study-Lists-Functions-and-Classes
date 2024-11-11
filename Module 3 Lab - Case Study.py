"""
Title: Module 3 Case Study.py
Author: Neal Vander Does
Date: 11/9/2024
Class: SDEV220-50P-IO-202420-I-82X
GitHub Link: 
Description: 

Input:

Process:

Output:

"""
# NEED TO DO DESCRIPTIONS AND IMPROVE POTENTIALLY. ADD SETTERS FOR THE GETTERS?

class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def car(self):
        return self.vehicle_type

class Automobile(Vehicle):

    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def get_year(self):
        return self.year
    
    def get_make(self):
        return self.make 
    
    def get_model(self):
        return self.model
    
    def get_doors(self):
        return self.doors
    
    def get_roof(self):
        return self.roof
    

def all_info():
    info_dict = {"Vehicle Type": info.car(), 
                 "Year": car_info.get_year(), 
                 "Make": car_info.get_make(), 
                 "Model": car_info.get_model(), 
                 "Number of doors": car_info.get_doors(), 
                 "Type of roof": car_info.get_roof()}
    return info_dict


info = Vehicle(input("Enter the name of a vehicle: "))

year_info = input("Enter the year of your car: ")
make_info = input("Enter the make of your car: ")
model_info = input("Enter the model of your car: ")
doors_info = input("Does your car have 2 or 4 doors?: ")
roof_info = input("Is your roof solid or a sun roof?: ")

car_info = Automobile(str(year_info), str(make_info), str(model_info), str(doors_info), str(roof_info))

for keys, values in all_info().items():
    print(f"{keys}: {values}")
