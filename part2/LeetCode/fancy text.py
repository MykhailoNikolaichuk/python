import random
regular_string = 'Hello guys what are you doin, hope you doin well'
print(''.join([str(random.choice([ch.upper(), ch.lower()])) for ch in regular_string]))