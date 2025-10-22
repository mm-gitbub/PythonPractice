test_var = (((1+2)*4)**5)
print(test_var)
# Update to include the leap years
days_per_year = 365.25
sec_per_min = 60
min_per_hour = 60
hour_per_day = 24
num_years = 4
# Calculate the number of seconds per four years
total_sec = sec_per_min * min_per_hour * hour_per_day * days_per_year * num_years
print(f'the total seconds is {total_sec}')