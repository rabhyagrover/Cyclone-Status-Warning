def check_cyclone_status():
    print("CYCLONE WARNING STATUS ")
    
    try:
        # 1. User Inputs
        pressure = float(input("Enter Atmospheric Pressure (hPa): "))
        wind_speed = float(input("Enter Wind Speed (km/h): "))
        condition = input("Enter Weather Condition (Sunny/Windy/Rainy): ").strip().lower()

        # 2. Logical Evaluation
        # Primary check: Pressure and Wind Speed
        is_extreme_pressure = pressure < 995
        is_high_wind = wind_speed > 60
        
        # Secondary check: Qualitative conditions
        is_stormy_weather = (condition == "windy" or condition == "rainy")

        print("\n--STATUS--")
        
        # 3. Decision Tree Logic
        if is_extreme_pressure and is_high_wind:
            print("🚨 STATUS: CYCLONE WARNING!")
            print(f"Danger: High wind speeds ({wind_speed} km/h) and low pressure ({pressure} hPa).")
            if is_stormy_weather:
                print(f"Warning: Current {condition} conditions are accelerating the storm.")
            print("Action: Evacuate to high ground or a cyclone shelter immediately.")

        elif is_extreme_pressure or is_high_wind:
            print("⚠️ STATUS: WEATHER ALERT")
            print("Caution: One or more parameters are outside normal safety bounds.")
            print("Action: Stay indoors and monitor for further changes.")

        else:
            print("✅ STATUS: NORMAL")
            print(f"The current condition is {condition.capitalize()}. No cyclonic activity detected.")

    except ValueError:
        print("Error: Please enter numerical values for Pressure and Wind Speed.")

# Run the program
if __name__ == "__main__":
    check_cyclone_status()