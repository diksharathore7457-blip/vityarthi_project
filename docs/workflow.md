# Process Flow / Workflow

```text
START
  |
  v
Ask player to play?
  |
  +---- n ----> EXIT
  |
  y
  |
  v
Initialize game state
  |
  v
DAY 1 ... DAY 7
  |
  v
Display story + survivor status
  |
  v
Choose action
  |
  +--> Abandoned Building
  |       |
  |       +--> Rooms / Basement / Leave
  |
  +--> Supermarket
  |       |
  |       +--> Food / Survivors / Storage
  |
  +--> Gas Station
  |       |
  |       +--> Shelves / Hallways / Walk
  |
  +--> Rest
  |       |
  |       +--> Recover health / use medkit
  |
  +--> Fight Zombies
          |
          +--> Fight / Escape
                  |
                  v
             Choose weapon
                  |
                  v
             Update health/ammo
  |
  v
Consume food + water
  |
  v
Check health
  |
  +---- health <= 0 ----> GAME OVER
  |
  +---- day < 7 -------> NEXT DAY
  |
  +---- day == 7 ------> RESCUE / VICTORY
```
