# This is a mad lib using a function.

def madlib(adj_1, noun_1, noun_2, verb_1, adj_2, noun_3, verb_3, adj_3):
    '''madlib function'''

    template = f'''
    One day, on a {adj_1} afternoon, a {noun_1} was chasing a {noun_2}. 
    The {noun_2} was eventually caught, but not by the {noun_1}. 
    Instead, a policeman who was {verb_1} nearby, heard the commotion and caught the {noun_2}. 
    Fortunately for the {noun_2}, a {adj_2} {noun_3} was passing by, saw the commotion,
    and decided to help set the {noun_2} free. 
    Years passed and together they lived their lives {verb_3}. 
    {adj_3} ever after!
'''
    return template

print(madlib('muddy', 'tornado', 'man', 'falling', 'stinky', 'wizard', 'eating', 'Smelly'))