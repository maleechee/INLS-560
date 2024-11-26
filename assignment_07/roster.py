# Roster Webpage Link: https://goheels.com/sports/mens-basketball/roster
import pandas as pd

roster = ['Brown', 'Davis', 'Tyson']
print(roster)

for name in roster:
    print(name)

player = {'Last Name': roster,
          'First Name': ['James', 'RJ', 'Cade'],
          'height': [82, 72, 79],
          'weight': [215, 180, 200]}

data = pd.DataFrame(player)
print(data)