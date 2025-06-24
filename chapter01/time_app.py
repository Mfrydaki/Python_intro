SECOND_IN_A_MINUTE = 60
SECOND_IN_AN_HOUR = 3600
SECOND_IN_A_DAY = 86400

total_seconds = int(input("Enter the number of seconds: ")) 

days = total_seconds // SECOND_IN_A_DAY
seconds_remaining = total_seconds % SECOND_IN_A_DAY

hours = seconds_remaining // SECOND_IN_AN_HOUR
seconds_remaining %= SECOND_IN_AN_HOUR

minutes = seconds_remaining // SECOND_IN_A_MINUTE
seconds_remaining %= SECOND_IN_A_MINUTE

seconds = seconds_remaining 

print (f"{total_seconds} seconds is equal to ")
print (f"{days} days,{hours} hours, {seconds} seconds" )