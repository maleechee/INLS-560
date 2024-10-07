cars = ['audi', 'bmw', 'toyota', 'subaru']

for car in cars: 
    if car == 'bmw':
        print(car.upper())
    else: 
        # 'Capitalize' and 'title' methods capitalize the first letter of a string.
        print(car.capitalize())

cars_string = "audi bmw subaru toyota"
print(f"{cars_string[0:5]}")

i = 0

for car in cars:
    i += 1
print(f"There are {i} car brands in this list.")