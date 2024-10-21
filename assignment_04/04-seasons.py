# Requirements for Spring
MIN_TEMP = 60
MAX_TEMP = 80

# User's provided data:
current_temp = int(input('Enter the temperature: '))

if current_temp >= MIN_TEMP and current_temp <= MAX_TEMP:
    print('The season is spring.')
else:
    print(f'''
    It is not spring.

    The temperature must be: 
        - At least {MIN_TEMP}
        - No more than {MAX_TEMP} 
    ''')

current_month = int(input('Enter the current month as an integer'))