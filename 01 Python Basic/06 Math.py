# Calculation of Rectangular shape--> (base * height) * 0.5
base = float(input("Enter base: "))
height = float(input("Enter height: "))
rectangular_area = (base * height) * 0.5
print("Calculation of Area is: ", rectangular_area, "\n")

# Calculation of circular shape --> (pie - r - square)
radius = float(input("Enter radius: "))
circular_area = 3.1416 * radius ** 2  # pie=3.1416 a=p*r*r
print("Area of the circle is: ", circular_area)
