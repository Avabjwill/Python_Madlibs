# # String concatenation (aka how to put strings Together)

dog1 = input("Dog:")
dog2 = input("Dog:")
dog3 = input("Dog:")
dog4 = input("Dog:")

adj1 = input("Adjective:")
adj2 = input("Adjective:")
adj3 = input("Adjective:")
adj4 = input("Adjective:")

verb1 = input("Verb:")
verb2 = input("Verb:")
verb3 = input("Verb:")
verb4 = input("Verb:")

random_word1 = input("Random Word:")
random_word2 = input("Random Word:")
random_word3 = input("Random Word:")
random_word4 = input("Random Word:")

madlib = f" I am a {dog1},who likes to {verb2}, but not {verb1}.  I have a friend who is a {dog2} who doesnt \
like {random_word1}.They are very {adj3}, but also very {adj1}. Me on the other hand I'm {adj2}. \
My Other pals {dog4} and {dog3} well their like me,they're all {random_word4} and {verb4}.\
When we're at the park we like to play with {random_word2} and {random_word3}"

print(madlib)