from datetime import datetime, timedelta

def display_current_datetime():

   current_datetime = datetime.now()

   current_date = current_datetime.date()

   formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

   print("Current Date and Time:", formatted_datetime)

   return current_datetime

def calculate_future_date(current_datetime, days):
   
   future_date = current_datetime + timedelta(days=days)

   formatted_future_date = future_date.strftime("%Y-%m-%d")

   print("Future date:", formatted_future_date)

current_datetime = display_current_datetime()

try:
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    calculate_future_date(current_datetime, number_of_days)

except ValueError:

    print("Please enter a valid integer.")