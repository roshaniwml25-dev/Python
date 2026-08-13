car = {"brand": "BMW", "model": "X SUVs", "year": 2022, "color": "black"}

del car["color"]

print("Key-value pairs:", car.items())

if "model" in car:
    print("The key 'model' exists.")
else:
    print("The key 'model' does not exist.")