import math

def idol():
    angle = float(input("ihatag ang launch angle bi: "))
    if angle <= 0 or angle >= 90:
        print("i-enter ang angle.")
        return
    
    distance = float(input("Enter the distance (in meters): "))
    
    angle_rad = math.radians(angle)
    g = 9.81
    
    sin_2angle = math.sin(2 * angle_rad)
    # No need to check if zero now since input is limited
    
    velocity = math.sqrt((distance * g) / sin_2angle)
    
    print("The trebuchet's launch speed is about {:.2f} m/s".format(velocity))

if __name__ == "__main__":
    idol()

