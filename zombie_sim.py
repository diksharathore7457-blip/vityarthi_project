
import time

print('███████╗ ██████╗ ███╗   ███╗██████╗ ██╗███████╗')
print('╚══███╔╝██╔═══██╗████╗ ████║██╔══██╗██║██╔════╝')
print('  ███╔╝ ██║   ██║██╔████╔██║██████╔╝██║█████╗')
print(' ███╔╝  ██║   ██║██║╚██╔╝██║██╔══██╗██║██╔══╝')
print('███████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██║███████╗')
print('╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝╚══════╝')          
print('              ☠ SURVIVAL ☠'                   )
print()

play_game = input('welcome to the zombie apocalypse! do you want to play? (y/n): ').lower()

while True:
    if play_game == 'y':
        print('the city has fallen ')
        print('you are one of the few survivors left')
        print('survive for 7 days....')
        print('manage your resources and make the right choices to stay alive')
        print('good luck!')
        input('\npress ENTER to start......')
        break
    elif play_game == 'n':
        print('exiting game...')
        exit()
    else:
        print('invalid input, please enter y or n')
        play_game = input('do you want to play? (y/n): ').lower()

health = 100
food = 5
water = 5 
medkits = 0
weapons = []
pistol_ammo = 0
shotgun_ammo = 0

days = 7

if weapons:
    weapon_display = ', '.join(weapons)
else:
    weapon_display = 'None'

print(' you have 7 days to survive')

for day in range(1, days + 1):
    print()
    print('=' * 45) 
    print(f'                🌅 Day {day} 🌅')
    print('=' * 45)

    print(f'Days left: {days - day+1}')

    print()

    if day ==1:
        print('The city has fallen to chaos....')
        time.sleep(0.5)
        print('All the connections to the world are wrecked..')
        time.sleep(0.5)
        print('Survive and escape........')
    elif day ==2:
        print('you hear some strange noises coming from the street..')
        time.sleep(0.5)
        print('you looked out of the window..')
        time.sleep(0.5)
        print('people have all turned into zombies....')
    elif day ==3:
        print('food and water are becoming harder and harder to find..')
    elif day ==4:
        print('you hear some radio transition..')
        time.sleep(0.5)
        print('the voice is all mixed up and the signals are getting weak..')
        time.sleep(0.5)
        print('is help coming?....')
    elif day ==5:
        print('Are you the sole survivor in the city?....')
    elif day ==6:
        print('you hear another announcement about the city...')
        time.sleep(0.5)
        print('the announcement says...that....') 
        time.sleep(0.5)
        print('military rescue shelters are camped out of the city.. ')
    elif day ==7:
        print('you have reached the final day..')
        time.sleep(0.5)
        print('military helicopters are all over the city..')       

    print()
    print(' ╔════════════════════════════════════════════╗')
    print(' ║              SURVIVOR STATUS               ║')
    print(' ╠════════════════════════════════════════════╣')
    print(f' ║ ❤️  Health : {health}/100                        ║')                           
    print(f' ║  🍖  Food   : {food}                            ║')
    print(f' ║ 💧  Water  : {water}                             ║')
    print(f' ║ 🩹  Medkits: {medkits}                             ║')
    print(f' ║ 🔫  Weapon : {weapon_display}                          ║')
    print(' ╚════════════════════════════════════════════╝')

    print()
    print('choose an action:')
    print('1. search an abandoned building')
    print('2. search a supermarket')
    print('3. search a gas station')
    print('4. rest for the day')
    print('5. fight the zombies')
    choice = input('enter your choice (1-5): ')

    if choice == '1':
        print()
        print('you entered an abandoned building...')
        time.sleep(2)
        print(r"""
                 ☁                 ☁
        .              ☁
              .   .         ☁

             /\
            /  \
           /____\
          |      |
          |  []  |        ┌───────────────┐
          |      |        │  ABANDONED    │
          | [] [] |        │    BUILDING   │
     _____|      |_________│_______________│
    /     |      |         |               \
   /      |  []  |         |   broken      \
  /_______|______|_________|________________\
  |       |      |         |                |
  |  []   |  ██  |    []   |      []        |
  |       |      |         |                |
  |_______|______|_________|________________|
       ||                         ||
       ||                         ||
      _||_                       _||_
     /____\                     /____\

        ~ ~ ~  dead grass & fog  ~ ~ ~
""")
        print()
        print('WHAT DO YOU WANT TO DO?')
        print('1. search the rooms')
        print('2. search the basement')
        print('3. leave the building')

        building_choice = input('enter you choice (1-3):')
        if building_choice == '1':
            print('you are searching the rooms.....')
            time.sleep(0.5)
            print('you found some food and water!')
            time.sleep(0.5)
            food += 2
            water += 2
        elif building_choice == '2':
            print('you entered the basement...')
            time.sleep(0.5)
            print('voices coming from the hallway of the basement..')
            time.sleep(0.5)
            basement = input('you want to turn left or right? (left/right):').lower()
            time.sleep(0.5)
            if basement == 'left':
                print('you were attacked by a zombie!')
                time.sleep(0.5)
                print()
                print('what do you want to do?')
                print('1. fight')
                print('2. flight')
                zombie_choice = input('\n Enter your choice (1-2):')
                if zombie_choice == '1':
                    if len(weapons) == 0:
                        print()
                        print('YOU HAVE NO WEAPONS!!')
                        print('You fought the zombie with your bare hands..')
                        print('You got saved but you are injured')
                        health -= 60
                    else:
                        print()
                        print('choose your weapon:')
                        for i in range(len(weapons)):
                            print(f'{i+1}.{weapons[i]}')
                            weapon_choice = input('\nEnter your weapon choice')
                        if weapon_choice.isdigit():
                            weapon_number = int(weapon_choice)
                            if 1 <= weapon_number <= len(weapons):
                                selected_weapon = weapons[weapon_number - 1]
                                print()
                                print(f'you chose the {selected_weapon}!')
                                time.sleep(0.5)
                                if selected_weapon == 'Baseball Bat':
                                    print('you defeated the zombie!')
                                    health -= 45
                                elif selected_weapon == 'Pistol':
                                    if pistol_ammo > 0:
                                        print('BANG!')
                                        print('you defeated the zombie!')
                                        pistol_ammo -= 1
                                        health -= 10
                                    else:
                                        print('you are out of pistol ammo!')
                                        print('the zombie attacked you!')
                                        health -= 45
                                elif selected_weapon == 'Shotgun':
                                    if shotgun_ammo > 0:
                                        print('BOOM!!!')
                                        print('you defeated the zombie!')
                                        shotgun_ammo -= 1
                                        health -= 5
                                    else:
                                        print('you are out of shotgun ammo!')
                                        print('the zombie attacked you!')
                                        health -= 45
                            else:
                                print('invalid weapon choice.')
                                health -= 30
                        else:
                            print('invalid weapon choice.')
                            health -= 30
                elif zombie_choice  == '2':
                    print()
                    print('You ran away from the zombies!')
                    health -= 30
                else:
                    print()
                    print('you froze in fear!!...')
                    health -= 50
            else:
                print('you turned right...')
                time.sleep(0.5)
                print('you found a baseball bat and some medical supplies!!')
                time.sleep(0.5)
                weapons.append('Baseball bat')
                medkits+= 3
                print('Baseball bat added to you inventory!')
                print('you found 3 medkits!!')
        elif building_choice == '3':
            print('you left the building safely.')
            health -= 10
        else:
            print('invalid choice. you wasted your time..')

        input('\n press ENTER to continue... ')
    elif choice == '2':
        print('you entered a supermarket...')
        time.sleep(2)
        print(r"""
                 ______________________________
                /                              \
               /     ☠  SUPERMARKET  ☠        \
              /________________________________\
              |                                |
              |   ███       BROKEN       ███   |
              |   █  |      WINDOWS      |  █   |
              |      |                    |      |
              |  🥫  |     _________      | 🍎   |
              |      |    |         |     |      |
              |______|____|  ENTRY  |_____|______|
              |          |_________|             |
              |                                  |
              |      .  .  .  .  .  .           |
              |__________________________________|
                 ||          ||           ||
                 ||          ||           ||
              ___||__________||___________||___
             /                                 \
            /   abandoned carts & broken glass  \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
        print()
        print('what do you want to do?')
        print('1. search the food section')
        print('2. look for other survivors')
        print('3. search the storage room')

        supermarket_choice = input('enter your choice (1-3):')
        if supermarket_choice == '1':
            time.sleep(0.5)
            print('you are searching the shelves....')
            time.sleep(0.5)
            print('you found some expired food and water!')
            food += 2
            water += 3
        elif supermarket_choice == '2':
            print('you were roaming around the supermarket..')
            time.sleep(0.5)
            print('you found a group of survivors!')
            time.sleep(0.5)
            trust = input('Do you want to trust them? (y/n): ').lower()
            if trust == 'y':
                print('you trusted them and you got killed!')
                print('GAME OVER')
                exit()
            else:
                print('you did not trust them....')
                time.sleep(1)
                print('they were infected and you got saved!')
                
        elif supermarket_choice == '3':
            print('walking toward the storage room.....')
            time.sleep(0.5)
            print('you can hear some voices..')
            time.sleep(0.5)
            print('you found a hidden underground lab!!!!!!')
            time.sleep(0.5)
            print('secret ending unlocked!')
            medkits += 2
            food += 2
            water += 2
            print()
            print('you found 2 medkits..')
            print('you also found some food and water..')
        else:
            print('invalid choice. You wasted your time..')
        input('\n press ENTER to continue... ')
    elif choice == '3':
        print('you entered a gas station...')
        time.sleep(2)
        print(r"""
                    ___________________________
                   |                           |
                   |       ⛽ GAS STATION       |
                   |___________________________|
                   |                           |
          _________|                           |_________
         |         |                           |         |
         |   ⛽    |                           |   ⛽    |
         |  PUMP   |                           |  PUMP   |
         |_________|                           |_________|
                   |                           |
                   |       ______________      |
                   |      |              |     |
                   |      |  MINI SHOP   |     |
                   |      |______________|     |
                   |                           |
                   |___________________________|
                       ||                 ||
                       ||                 ||
                  _____||_____       _____||_____
                 /           \     /           \
                /   EMPTY    \   /   ABANDONED \
               /     ROAD     \ /      CARS     \
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

        print()
        print('what do you want to do?')
        print('1. search the shelves')
        print('2. search the hallways')
        print('3. walk around')

        gas_choice = input('enter your choice (1-3)')
        if gas_choice == '1':
            print('searching the shelves.......')
            time.sleep(0.5)
            print('you found nothing')
            print('the food was already stolen ')
        elif gas_choice == '2':
            print('you heard a noise.......')
            time.sleep(1)
            investigate = input('Do you want to investigate? (y/n): ').lower()
            if investigate == 'y':
                print('jackpot!!!!!!!!!!!!!!!!')
                time.sleep(0.5)
                print('You found lots of supplies.')
                time.sleep(0.5)
                print('you found a pistol and a shotgun....')
                time.sleep(0.5)
                print('oooohhhh!!!....there are ammos too!!! and medkits')
                time.sleep(0.5)
                weapons.append('Pistol')
                weapons.append('Shotgun')
                pistol_ammo += 6
                shotgun_ammo += 3
                medkits += 3

                print('Pistol added to your inventory')
                print('Shotgun added to your inventory')
                print('you found 3 medkits!')
            else:
                print('you decided not to investigate.')
                time.sleep(0.5)
                print('you missed on something good.....')
                time.sleep(0.5)
                print('have some guts......')
        elif gas_choice == '3':
            print('walking around...')
            time.sleep(0.5)
            print('zombiesssssssssssss')
            time.sleep(0.5)
            print(r'''
       .-"""-.          .-"""-.          .-"""-.
      /  X X  \        /  X X  \        /  X X  \
     |    _    |      |    _    |      |    _    |
      \  ___  /        \  ___  /        \  ___  /
       \_____/          \_____/          \_____/
          ||               ||               ||
        __||__           __||__           __||__
       /  ||  \         /  ||  \         /  ||  \
      /   ||   \       /   ||   \       /   ||   \
     /___/  \___\     /___/  \___\     /___/  \___\

              ☠  THE DEAD HAVE RISEN  ☠
''')
            print()
            print('what do you want to do?')
            print('1. fight')
            print('2. flight' )   
            zombie_choice = input('\nenter your choice (1-2): ')
            if zombie_choice == '1':
                if len(weapons) == 0:
                    print()
                    print('you have no weapon!')
                    print('you tried to fight the zombies.')
                    health -= 60
                else:
                    print()
                    print('choose your weapon:')
                    for i in range(len(weapons)):
                        print(f'{i+1}.{weapons[i]}')
                    weapon_choice = input('\nEnter your weapon choice')
                    if weapon_choice.isdigit():
                        weapon_number = int(weapon_choice)
                        if 1 <= weapon_number <= len(weapons):
                            selected_weapon = weapons[weapon_number - 1]
                            print()
                            print(f'you chose the {selected_weapon}!')
                            time.sleep(0.5)
                            if selected_weapon == 'Baseball Bat':
                                print('you defeated the zombie!')
                                health -= 45
                            elif selected_weapon == 'Pistol':
                                if pistol_ammo > 0:
                                    print('BANG!')
                                    print('you defeated the zombie!')
                                    pistol_ammo -= 1
                                    health -= 10
                                else:
                                    print('you are out of pistol ammo!')
                                    print('the zombie attacked you!')
                                    health -= 45
                            elif selected_weapon == 'Shotgun':
                                if shotgun_ammo > 0:
                                    print('BOOM!!!')
                                    print('you defeated the zombie!')
                                    shotgun_ammo -= 1
                                    health -= 5
                                else:
                                    print('you are out of shotgun ammo!')
                                    print('the zombie attacked you!')
                                    health -= 45
                        else:
                            print('invalid weapon choice.')
                            health -= 30
                    else:
                        print('invalid weapon choice.')
                        health -= 30
            elif zombie_choice == '2':
                print()
                print('You ran as fast as you could!')
                time.sleep(0.5)
                print('you escaped the zombies.')
                health -= 30
            else:
                print()
                print('you froze in fear!!...')
                health -= 50
        else:
            print('invalid choice. you wasted your time..')
        input('\n press ENTER to continue... ')
    elif choice == '4':
        print()
        print('you stayed inside and rested....')
        time.sleep(0.5)
        print('your health improved!')
        time.sleep(0.5)
        health += 20
        if health > 100:
            health = 100
        if medkits > 0:
            print()
            print(f'you have {medkits} medkit(s).')
            use_medkit = input('do you want to use a medkit? (y/n): ').lower()
            if use_medkit == 'y':
                health += 30
                medkits -= 1
                if health > 100:
                    health = 100
                print()
                print('you used a medkit!')
                print(f'health restored to {health}/100')
            else:
                print('you decided to save your medkit.')
                input('\npress ENTER to continue... ')
        else:
            print('invalid choice. you wasted your time..')
        input('\n press ENTER to continue...')
    elif choice == '5':
        print()
        print('you exited the building..')
        time.sleep(0.5)
        print('ready????')
        time.sleep(0.5)
        print(r"""
             ☠ ZOMBIE ATTACK ☠

        🧟       🧟       🧟
       /|\      /|\      /|\
      / | \    / | \    / | \

              \  |  /
               \ | /
                \|/
              ---X---
                /|\
               / | \

             ⚔  YOU  ⚔

        ======================
             FIGHT THEM!
        ======================
""")
        print('A group of zombies is coming towards you...')
        time.sleep(1)
        print()
        print('What do you want to do?')
        print('1. Fight!!!!')
        print('2. Escape..')
        fight_choice = input('\n Enter you choice (1-2):')
        if fight_choice == '1':
            if health <= 50 and medkits >0:
                print()
                print(f'YOUR HEALTH IS ONLY {health}/100!')
                print(f'You have {medkits} medkit(s).')
                use_medkit = input('Do you want to use a medkit before fighting? (y/n):').lower()
                if use_medkit == 'y':
                    health += 30
                    medkits-= 1
                    if health >100:
                        health = 100
                    print()
                    print('You used a medkit!')
                    print(f'❤️ Health restored to {health}/100')
                    time.sleep(0.5)

            if len(weapons) == 0:
                print()
                print('YOU HAVE NO WEAPONS!!')
                print('You will have to fight with your bare hands..')
                time.sleep(0.5)
                print("you got injured heavily but luckily didn't get infected")
                health -= 50
                food -= 2
                water -= 3
            else:
                print()
                print('Choose you weapon:')
                for i in range(len(weapons)):
                    print(f'{i+1}.{weapons[i]}')
                weapon_choice = input('\n Enter your weapon choice:')
                if weapon_choice.isdigit():
                    weapon_number = int(weapon_choice)
                    if 1 <= weapon_number <= len(weapons):
                        selected_weapon = weapons[weapon_number - 1]
                        print()
                        print(f'You chose the {selected_weapon}!')
                        time.sleep(0.5)
                        if selected_weapon == 'Baseball Bat':
                            print('You swing the baseball bat at the zombies!')
                            time.sleep(1)
                            print('You defeated the zombies!')
                            health -= 15
                        elif selected_weapon == 'Pistol':
                            print('You fire your pistol!')
                            time.sleep(1)
                            print('You took down the zombies!')
                            health -= 10
                        elif selected_weapon == 'Shotgun':
                            print('You fire the shotgun!')
                            time.sleep(1)
                            print('BOOOOOOM!!!')
                            print('The zombies are down!')
                            health -= 5
                    else:
                        print('Invalid weapon choice.')
                        print('You panicked and lost valuable time.')
                        health -= 25
                        food -= 1
                        water -= 1
                else:
                    print('Invalid weapon choice.')
                    print('You panicked and lost valuable time.')
                    health -= 25
                    food -= 1
                    water -= 1

        elif fight_choice == '2':

            print()
            print('You decided to escape!')
            time.sleep(1)

            print('You ran through the streets...')
            time.sleep(1)

            print('You escaped the zombies!')
            health -= 20
            food -= 1
            water -= 1


        else:

            print()
            print('You froze!')
            print('The zombies attacked you!')
            health -= 70
            food -= 2
            water -= 3
        
    else:
        print()
        print('INVALID CHOICE')
        print('you wasted the day :(')
        input('\n press ENTER to continue..')
    
    

    food -= 1
    water -= 1

    input('\n press ENTER to end the day')
    print()
    print(r"""
        =====================================
                  ☀ YOU SURVIVED ☀
        =====================================

             Another day is over.
             But the nightmare continues...

                  NIGHT FALLS...

        =====================================
""")
    if food < 0:
        food = 0
        print(r"""
        =====================================

                  ⚠ FOOD DEPLETED ⚠

              The last supplies are gone.

                    Nothing left.

                 Hunger awaits...

        =====================================
""")
        health -= 40

    if water < 0:
        water = 0
        print(r"""
              ___________________
             |                   |
             |   WATER SUPPLIES  |
             |___________________|

                    ______
                   /      \
                  |        |
                  |        |
                  |  EMPTY |
                  |        |
                  |________|

             ⚠  NO WATER LEFT  ⚠

          You need to find more water.
""")
        health -= 55

    print('END OF THE DAY', day)
    print('❤️ Health:', health)
    print('🍖 food:' , food)
    print('💧 water:', water)
    print('Mmedkits:', medkits)
    if weapons:
        print('weapons:', ', '.join(weapons))
    else:
        print('weapons: None')
    print('Pistol ammo:', pistol_ammo)
    print('Shotgun ammo:', shotgun_ammo)

    if health <= 0:
        print(r"""
            ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠

                    YOU DIED

              The apocalypse won.

                   GAME OVER

            ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠
""")
        print('you survived for', day, 'days')
        break 

    if day == 7:
        print()
        print('*' * 45)
        print('             YOU SURVIVED!!!')
        print('*' * 45)
        print()
        print('you survived all seven days of the zombie apocalypse!!')
        time.sleep(1)
        print()
        print('rescue helicoptor arrived!!!!!!!')
        time.sleep(0.5)
        print(r"""
             ==========|==========
                       |
                 ______|______
              __/             \__
             /                   \
            |    ___________     |
            |___/           \____|
                 \_________/
                     ||
                     ||
                     ||
                    /  \

             🚁 RESCUE ARRIVED 🚁
              YOU'RE FINALLY SAFE
""")
        print('you got rescued!!! ')
        print('final health', health)
        time.sleep(1)
        print(r"""
    ☠        🧟              ☠          🧟
          🧟       ☠              🧟
   █████████████████████████████████████████████


             ██╗   ██╗ ██████╗ ██╗   ██╗
             ╚██╗ ██╔╝██╔═══██╗██║   ██║
              ╚████╔╝ ██║   ██║██║   ██║
               ╚██╔╝  ██║   ██║██║   ██║
                ██║   ╚██████╔╝╚██████╔╝
                ╚═╝    ╚═════╝  ╚═════╝


             ██╗    ██╗ ██████╗ ███╗   ██╗
             ██║    ██║██╔═══██╗████╗  ██║
             ██║ █╗ ██║██║   ██║██╔██╗ ██║
             ██║███╗██║██║   ██║██║╚██╗██║
             ╚███╔███╔╝╚██████╔╝██║ ╚████║
              ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝


              █████████████████████████████

                  THE WORLD ENDED.

                       YOU DIDN'T.

                    ★  YOU WON  ★


    ☠        🧟              ☠          🧟
          🧟       ☠              🧟
""")


