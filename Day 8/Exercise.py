                                                #    Excersice 2: Good Morning Sir

# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. 
# Your program should use time module to get the current hour.
import time
timestamp=time.strftime("%H:%M:%S %p")
current_time = time.strftime("%I:%M:%S %p")

h=int(time.strftime("%H"))
hour=int(input("Enter the time in hour(use 24 hour format):"))

print("Current time in 24-hour format:",timestamp)
print("Current time in 12-hour format:", current_time)

if hour >=0 and hour <= 11:
    print("Good Morning Sir")
elif hour >=12 and hour <= 16:
    print("Good Afternoon Sir")
elif hour >=17 and hour <= 23:
    print("Good Evening Sir")
else:
    print("Invalid time")