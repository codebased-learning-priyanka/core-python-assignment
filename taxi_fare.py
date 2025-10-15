def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare
def total_fare(trips):
    total = 0
    for i, d in enumerate(trips, start=1):
        fare = calculate_fare(d)
        total += fare
        print(f"Trip {i}: ${fare}")
    print(f"Total Fare: ${total}")
trips = [5, 10, 3]
total_fare(trips)
