def hotel_cost (num_nights):
    b = 200 * num_nights
    return b
    
def plane_cost (city_choice):
    if city_choice == 'A':
        c = 180, "Paris"
        return c
    elif city_choice == 'B':
        d = 100, "London"
        return d
    elif city_choice == 'C':
        e = 160, "Madrid"
        return e
    else:
        return 0
    
   
def car_rental (rental_days):
    y = 50 * rental_days
    return y
    
def holiday_cost (hotel_cost, plane_cost, car_rental):
    x = hotel_cost + plane_cost + car_rental
    return x


while True:
    city_choice = input("Using the letters, choose where you want to go for holiday"
                      "\nA Paris"
                      "\nB London"
                      "\nC Madrid"
                      "\n :")
    if city_choice in ('A', 'B', 'C'):
        break
    else:
        print("Invalid choice. Please select A, B, or C.")
    

num_nights = int(input("Please input how many nights you wish to stay: "))
rental_days = int(input("Please input how many days do you wish to rent a car: "))

flight_cost, city_name = plane_cost (city_choice)
total_hotel_cost = hotel_cost (num_nights)
car_rental_total = car_rental (rental_days)
total_cost_holiday = holiday_cost (total_hotel_cost, flight_cost, car_rental_total)
    
print (f" The Flight cost to {city_name} is: ${flight_cost}."
    f"\n The Hotel cost is: ${total_hotel_cost}."
    f"\n The car rental cost is: ${car_rental_total}."
    f"\n Total cost of your holiday to {city_name} is: ${total_cost_holiday}.")

