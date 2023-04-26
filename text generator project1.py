import random 
adjectives = ["attractive", "brave", "calm", "elegant", "friendly", "honest", 
"joyful", "kind", "lively", "modest", "nervous", "optimistic", "powerful", 
"reliable", "sincere", "thoughtful", "witty"]
nouns = ["apple", "bear", "cat", "dog", "elephant", "fish", "girl", "horse", 
"jacket", "kite", "lamb", "monkey", "night", "owl", "pizza", "queen", "rainbow", 
"strawberry"]
adjective = random.choice(adjectives)
noun = random.choice(nouns)
random_text = adjective + " " + noun 
print(random_text)
