# Identify frame using height ang width

height = float(input("Enter Height : "))
width = float(input("Enter Width :"))

if height > width :
    print("Frame is Portrait")
if height < width :
    print("Frame is Landscape")
if height == width :
    print("Frame is Square")