def convert_f_to_c(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def convert_k_to_c(kelvin):
    """Converts Kelvin to Celsius."""
    return kelvin - 273.15

def get_temperature_status(celsius):
    """Determines the temperature status based on Celsius."""
    if celsius < 0:
        return "Too cold!"
    elif 0 <= celsius <= 35:
        return "Safe temperature."
    else:
        return "Too hot!"

def main():
    """Main function to run the temperature checker program."""
    print("Choose a unit of measurement: C, F, or K")
    unit = input().upper()

    if unit not in ['C', 'F', 'K']:
        print("Invalid")
        exit()

    try:
        temp_input = float(input("Enter the temperature: "))
    except ValueError:
        print("Invalid temperature value.")
        exit()
    
    if unit == 'F':
        celsius_temp = convert_f_to_c(temp_input)
    elif unit == 'K':
        celsius_temp = convert_k_to_c(temp_input)
    else:
        celsius_temp = temp_input

    status = get_temperature_status(celsius_temp)
    print(status)

if __name__ == "__main__":
    main()
