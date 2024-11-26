# Roster Webpage Link: https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player = {'Last Name': ['Brown', 'Davis', 'Tyson', 'Cadaeu', 'Trimble', 
                        'Powell', 'Jackson', 'Washington', 'Hawkins', 'Holbrook'],
          'First Name': ['James', 'RJ', 'Cade', 'Elliot', 'Seth', 
                         'Drake', 'Ian', 'Jalen', 'Russell', 'John'],
          'height': [82, 72, 79, 73, 75, 78, 76, 82, 73, 80],
          'weight': [215, 180, 200, 180, 195, 195, 190, 235, 175, 230]}

data = pd.DataFrame(player)

# BMI = weight in kg/height in meters^2
data['bmi'] = round((data['weight']/2.205)/((data['height']/39.37)**2), 2)

print(data)

data.to_csv('bmi.csv')