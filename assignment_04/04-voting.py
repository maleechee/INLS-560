# Requirements to vote
MIN_AGE = 18
COUNTY = 'Orange'

# User's provided data:
user_age = int(input('Enter your age: '))
user_county = str(input('Are you a resident of Orange County? Y or N: ')) # any error would be user error in this case.

# Determining if user can vote in Orange County
if user_age >= MIN_AGE and user_county == "Y":
    print("You may vote in this county!")
else:
    print(f'''
You are not eligible to vote in {COUNTY} County.
    
In order to vote, you must: 
    - Be at least 18 years of age
    - Be registered to vote in that same county
        ''')