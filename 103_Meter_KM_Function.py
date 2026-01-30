def meter_to_km(meter):
    km = meter / 1000
    return km

meter = float(input("Enter distance in meters: "))

kilometer = meter_to_km(meter)

print("Distance in kilometers:", kilometer)