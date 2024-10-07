games = ['The Sims 3', 'Dead by Daylight', 'Minecraft', 'Horizon: Zero Dawn']

i = 0

for game in games:
    i += 1
print(f"There are {i} games in this list.")


print(f"These are my favorite games: ")
for game in games:
    print(game)

for game in games: 
    if game == "Minecraft":
        print(game.upper())
    else: 
        print(game.title())