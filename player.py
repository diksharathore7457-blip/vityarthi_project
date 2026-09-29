# player.py

class Player:
    def __init__(self):
        self.health = 100
        self.food = 5
        self.water = 5
        self.medkits = 0
        self.weapons = []
        self.pistol_ammo = 0
        self.shotgun_ammo = 0

    def is_alive(self):
        return self.health > 0

    def consume_daily_resources(self):
        self.food -= 1
        self.water -= 1
        
        if self.food < 0:
            self.food = 0
            self.take_damage(40, "Starvation")
            
        if self.water < 0:
            self.water = 0
            self.take_damage(55, "Dehydration")

    def take_damage(self, amount, reason=""):
        self.health -= amount
        if reason:
            print(f"You took {amount} damage from {reason}!")
        if self.health < 0:
            self.health = 0

    def heal(self):
        if self.medkits > 0:
            self.health = min(100, self.health + 30)
            self.medkits -= 1
            print(f"You used a medkit! Health restored to {self.health}/100.")
            return True
        else:
            print("You don't have any medkits!")
            return False

    def add_weapon(self, weapon_name):
        if weapon_name not in self.weapons:
            self.weapons.append(weapon_name)
            print(f"{weapon_name} added to your inventory!")

    def display_status(self):
        weapon_display = ', '.join(self.weapons) if self.weapons else 'None'
        print('\n ╔════════════════════════════════════════════╗')
        print(' ║              SURVIVOR STATUS               ║')
        print(' ╠════════════════════════════════════════════╣')
        print(f' ║ ❤️  Health : {self.health}/100                        ║')                           
        print(f' ║ 🍖  Food   : {self.food}                            ║')
        print(f' ║ 💧  Water  : {self.water}                             ║')
        print(f' ║ 🩹  Medkits: {self.medkits}                             ║')
        print(f' ║ 🔫  Weapon : {weapon_display:<29}║')
        print(' ╚════════════════════════════════════════════╝\n')
