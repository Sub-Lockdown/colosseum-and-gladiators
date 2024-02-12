import random

class Gladiator:
    def __init__(self, name, attack, defense, speed, cost):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.cost = cost

        # Define maximum values for each attribute
        self.max_attack = attack
        self.max_defense = defense
        self.max_speed = speed

    def roll_initiative(self):
        return sum([self.roll_dice() for _ in range(self.speed)])

    def roll_dice(self, num_rolls=1):
        if num_rolls == 1:
            return random.randint(1, 6)
        else:
            return [random.randint(1, 6) for _ in range(num_rolls)]

    def modify_attribute(self, action):
        attribute_name = ""
        if action == 'gain_wound':
            attribute_name = 'gain a wound'
        elif action == 'heal':
            attribute_name = 'heal'

        print(f"{self.name}'s current attributes:")
        print(f"1. Attack: {self.attack}")
        print(f"2. Defense: {self.defense}")
        print(f"3. Speed: {self.speed}")

        choice = input(f"Choose which attribute to {attribute_name} (enter 1, 2, or 3): ")

        if choice == '1':
            if action == 'gain_wound':
                self.attack -= 1
            elif action == 'heal':
                self.attack = min(self.attack + 1, self.max_attack)
        elif choice == '2':
            if action == 'gain_wound':
                self.defense -= 1
            elif action == 'heal':
                self.defense = min(self.defense + 1, self.max_defense)
        elif choice == '3':
            if action == 'gain_wound':
                self.speed -= 1
            elif action == 'heal':
                self.speed = min(self.speed + 1, self.max_speed)
        else:
            print("Invalid choice. No action taken.")

        # Ensure attributes do not go below 1
        self.attack = max(self.attack, 1)
        self.defense = max(self.defense, 1)
        self.speed = max(self.speed, 1)

    def initiate_combat(self, defender):
        attacker_initiative = self.roll_initiative()
        defender_initiative = defender.roll_initiative()

        print(f"{self.name}'s initiative: {attacker_initiative}")
        print(f"{defender.name}'s initiative: {defender_initiative}")

        if attacker_initiative > defender_initiative:
            print(f"{self.name} goes first!")
            self.resolve_combat(defender)
            defender.resolve_combat(self)  # Follow-up attack
            # Add your additional combat resolution logic here for the attacker going first
        else:
            print(f"{defender.name} goes first!")
            defender.resolve_combat(self)
            self.resolve_combat(defender)  # Follow-up attack
            # Add your additional combat resolution logic here for the defender going first
    
    def resolve_combat(self, attacker):
        attacker_attack_dice = sorted(attacker.roll_dice(attacker.attack), reverse=True)
        defender_defense_dice = sorted(self.roll_dice(self.defense), reverse=True)
    
        print(f"{attacker.name}'s Attack Dice: {attacker_attack_dice}")
        print(f"{self.name}'s Defense Dice: {defender_defense_dice}")
    
        min_dice_count = min(len(attacker_attack_dice), len(defender_defense_dice))
    
        for i in range(min_dice_count):
            if attacker_attack_dice[i] > 2:  # Check if the attack succeeded (greater than 2)
                if attacker_attack_dice[i] > defender_defense_dice[i]:
                    print(f"{attacker.name}'s die {i + 1} beats {self.name}'s die {i + 1}")
                elif attacker_attack_dice[i] < defender_defense_dice[i]:
                    print(f"{attacker.name}'s die {i + 1} loses to {self.name}'s die {i + 1}")
                    self.modify_attribute('gain_wound')
            else:
                print(f"{attacker.name}'s die {i + 1} failed to attack.")
    
        if len(attacker_attack_dice) > len(defender_defense_dice):
            unopposed_dice = attacker_attack_dice[len(defender_defense_dice):]
            for die in unopposed_dice:
                if die >= 3:
                    print(f"{attacker.name}'s unopposed die {die} causes a wound to {self.name}")
                    self.modify_attribute('gain_wound')


if __name__ == "__main__":
    print("This is the gladiator and combat mechanics used by the main game.")
    quit()
