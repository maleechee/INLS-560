sales = 60000
bonus = sales * .03

if sales > 50000:
    print(f"You get a bonus of: {bonus}")
    
prompt = "What is today's temperature?"
degrees_f = int(input(prompt))

is_cold = degrees_f < 60

if degrees_f == is_cold:
    print("Wear a jacket!")
else: 
    print("The weather is not cold today!")