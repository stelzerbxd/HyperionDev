import datetime

print('Hello, World!')

# Asking for the user's name once
name = input("Enter your name: ")

# Determining the current hour
current_hour = datetime.datetime.now().hour

# Determining the part of the day
if 5 <= current_hour < 12:
    part_of_day = 'morning'
elif 12 <= current_hour < 18:
    part_of_day = 'afternoon'
else:
    part_of_day = 'evening'

# Printing a personalized greeting based on the time of day
print(f'Good {part_of_day}, {name}!')