def marathon_time_calculator():
    """
    Calculates the time to complete a marathon based on a runner's average speed.
    """
   
    marathon_distance_km = 42.195

   
    average_speed_kmh = float(input("Enter your average running speed in km/h: "))

   
    total_time_hours = marathon_distance_km / average_speed_kmh

 
    hours = int(total_time_hours)

    
    minutes = int((total_time_hours - hours) * 60)

   
    print("\n--- Result ---")
    print(f"To finish a marathon ({marathon_distance_km} km) at an average speed of {average_speed_kmh} km/h,")
    print(f"it will take approximately {hours} hours and {minutes} minutes.")


marathon_time_calculator()