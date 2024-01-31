from gladiator import Gladiator

# Define two gladiators for testing
attacker_tim = Gladiator(name="Tim", attack=3, defense=2, speed=4, cost=10)
defender_tom = Gladiator(name="Tom", attack=2, defense=3, speed=3, cost=8)

# Uncomment the code below if you want to run the combat when executing game.py
attacker_tim.initiate_combat(defender_tom)
