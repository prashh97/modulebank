#3a 
def check_object_id(N1, N2):
    if id(N1) == id(N2):
        print("N1 and N2 point to the same object.")
    else:
        print("N1 and N2 do NOT point to the same object.")

# Test the function
N1 = 100
N2 = 100
check_object_id(N1, N2)

#3b
import time

def traffic_signal():
    while True:
        print("Green Light - Go")
        time.sleep(20)  # Wait 20 seconds

        print("Yellow Light - Slow Down")
        time.sleep(5)  # Wait 5 seconds

        print("Red Light - Stop")
        time.sleep(20)  # Wait 20 seconds

# Run the function (press Ctrl+C to stop)
traffic_signal()

#3c
num = input("Enter phone number: ")

if num[0] == "9" and len(num) == 10:
    print("Valid phone number.")
else:
    print("Invalid phone number.")
