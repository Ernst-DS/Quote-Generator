import random
Things = ["Poop", "Horse", 'String', "Indication", "Lawyer", "Insuring Agent", "Screen", "Zombie", "Pooper"]
Quote = ["You know what they say, " + "You're either a " + random. choice(Things) + " or a " + random. choice(Things) + ".", "You know what they say: " + random. choice(Things) + ", " + random. choice(Things) + ", " + random. choice(Things), "What's the difference between a(n) " + random. choice(Things) + " and a(n) " + random. choice(Things) + "? " + random. choice(Things) + "!"]
print(random. choice(Quote))