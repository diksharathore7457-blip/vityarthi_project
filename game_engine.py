# game_engine.py
import time
from player import Player
from locations import search_building, search_supermarket, search_gas_station, handle_combat
from art import TITLE_ART, HELICOPTER_ART

class SurvivalGame:
    def __init__(self):
        self.player = Player()
        self.total_days = 7

    def start_game(self):
        print(TITLE_ART)
        play = input('Welcome to the zombie apocalypse! Play? (y/n): ').lower()
        if play != 'y':
            print("Exiting...")
            return

        print("The city has fallen... Survive for 7 days.")
        
        for day in range(1, self.total_days + 1):
            if not self.play_day(day):
                break
            
        if self.player.is_alive():
            self.win_game()
        else:
            self.game_over()

    def play_day(self, day):
        print(f'\n{"="*45}\n                🌅 Day {day} 🌅\n{"="*45}')
        self.player.display_status()
        
        print("Choose an action:")
        print("1. Search abandoned building")
        print("2. Search supermarket")
        print("3. Search gas station")
        print("4. Rest for the day")
        print("5. Fight roaming zombies")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            search_building(self.player)
        elif choice == '2':
            search_supermarket(self.player)
        elif choice == '3':
            search_gas_station(self.player)
        elif choice == '4':
            print("You rested and recovered health.")
            self.player.health = min(100, self.player.health + 20)
            if self.player.medkits > 0:
                use = input("Use a medkit? (y/n): ").lower()
                if use == 'y': self.player.heal()
        elif choice == '5':
            print("You went out to hunt zombies!")
            handle_combat(self.player)
        else:
            print("Invalid choice. You wasted the day.")

        self.player.consume_daily_resources()
        # input('\nPress ENTER to end the day...')
        return self.player.is_alive()

    def win_game(self):
        print("\n*** YOU SURVIVED! ***")
        print(HELICOPTER_ART)
        print("The rescue helicopter arrived! You won!")

    def game_over(self):
        print("\n☠ YOU DIED ☠")
        print("The apocalypse won. Game Over.")
