from gladiator import Gladiator

# Define two gladiators for testing
attacker_spartacus = Gladiator(name="spartacus", attack=3, defense=2, speed=4, cost=10)
defender_crixus = Gladiator(name="Crixus", attack=2, defense=3, speed=3, cost=8)

# Uncomment the code below if you want to run the combat when executing game.py
attacker_spartacus.initiate_combat(defender_crixus)
