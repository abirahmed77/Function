def circumference(r):
    return(2*3.1416*r) 

def area(r):
    return(3.1416*r*r)

radius = float(input("Enter the Radius : "))

cir = circumference(radius)
ar = area(radius)

print(f"Area is: {ar}")
print(f"Circumference is: {cir}")