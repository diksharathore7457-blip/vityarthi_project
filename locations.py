# locations.py
import time
from art import BUILDING_ART, SUPERMARKET_ART, GAS_STATION_ART, ZOMBIES_ART

def handle_combat(player):
    if len(player.weapons) == 0:
        print("\nYOU HAVE NO WEAPONS!! You fought with bare hands...")
        player.take_damage(60, "Zombie Attack")
        return

    print("\nChoose your weapon:")
    for i, w in enumerate(player.weapons, 1):
        print(f"{i}. {w}")
    
    choice = input("Enter your weapon choice: ")
    if choice.isdigit() and 1 <= int(choice) <= len(player.weapons):
        weapon = player.weapons[int(choice) - 1]
        print(f"\nYou chose the {weapon}!")
        
        if weapon == 'Baseball bat':
            player.take_damage(45, "Zombie Scratches")
        elif weapon == 'Pistol' and player.pistol_ammo > 0:
            player.pistol_ammo -= 1
            player.take_damage(10, "Minor Scratches")
        elif weapon == 'Shotgun' and player.shotgun_ammo > 0:
            player.shotgun_ammo -= 1
            player.take_damage(5, "Minor Scratches")
        else:
            print("Out of ammo! The zombie attacked you!")
            player.take_damage(45, "Zombie Attack")
    else:
        print("Invalid choice. The zombie bit you!")
        player.take_damage(30, "Zombie Attack")

def search_building(player):
    print("You entered an abandoned building...")
    print(BUILDING_ART)
    print("1. Search the rooms\n2. Search the basement\n3. Leave")
    
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        print("You found some food and water!")
        player.food += 2
        player.water += 2
    elif choice == '2':
        print("You entered the basement... A zombie appeared!")
        action = input("Fight or flight? (1/2): ")
        if action == '1':
            handle_combat(player)
        else:
            print("You ran away safely, but twisted your ankle.")
            player.take_damage(30, "Falling while running")
    elif choice == '3':
        player.take_damage(10, "Exhaustion")
    else:
        print("Invalid choice, time wasted.")

def search_supermarket(player):
    print("You entered a supermarket...")
    print(SUPERMARKET_ART)
    print("1. Search food section\n2. Look for survivors\n3. Search storage")
    
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        player.food += 2
        player.water += 3
    elif choice == '2':
        trust = input("Found survivors! Trust them? (y/n): ").lower()
        if trust == 'y':
            print("They betrayed you!")
            player.health = 0
        else:
            print("You walked away safely.")
    elif choice == '3':
        print("You found a hidden lab! Secret ending unlocked!")
        player.medkits += 2
        player.food += 2
        player.water += 2

def search_gas_station(player):
    print("You entered a gas station...")
    print(GAS_STATION_ART)
    print("1. Search shelves\n2. Search hallways\n3. Walk around")
    
    choice = input("Enter your choice (1-3): ")
    if choice == '2':
        investigate = input("Heard a noise, investigate? (y/n): ").lower()
        if investigate == 'y':
            print("Jackpot! Found weapons and supplies!")
            player.add_weapon('Pistol')
            player.add_weapon('Shotgun')
            player.pistol_ammo += 6
            player.shotgun_ammo += 3
            player.medkits += 3
    elif choice == '3':
        print("ZOMBIES!")
        print(ZOMBIES_ART)
        handle_combat(player)
