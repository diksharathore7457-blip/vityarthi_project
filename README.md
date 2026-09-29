# ☠ Zombie Survival Simulator

## 1. Project Overview

Zombie Survival Simulator is a console-based Python survival game in which the player must survive a seven-day zombie apocalypse.

The player begins with limited health, food, water and no weapons. During each day, the player chooses an action such as searching an abandoned building, supermarket or gas station, resting, or fighting zombies. These decisions change the player's health, supplies, weapons, ammunition and medkits.

The game uses Python's standard library (`random`, `time`, and `os`) and runs directly in a terminal/console.

## 2. Objectives

- Apply Python programming concepts in a practical project.
- Use variables, conditional statements, loops and lists.
- Build an interactive menu-driven application.
- Implement resource and inventory management.
- Implement branching decisions and multiple game outcomes.
- Demonstrate input validation and state changes.
- Practice version control using Git and GitHub.

## 3. Major Functional Modules

### A. Survival and Day Progression
The game progresses through seven days. Each day presents a different story event and updates the survivor's status.

### B. Exploration and Resource Collection
The player can explore an abandoned building, supermarket and gas station. These locations provide different choices and rewards or consequences.

### C. Combat and Inventory
The player can encounter zombies and choose whether to fight or escape. Weapons include a baseball bat, pistol and shotgun. Ammunition and medkits affect combat and survival.

### D. Resource and Health Management
Food and water decrease at the end of every day. Health changes according to player decisions, combat, resting and resource depletion.

### E. Win/Loss Conditions
The player loses when health reaches zero. Surviving all seven days produces the rescue ending.

## 4. Technologies Used

- Python 3
- `random`
- `time`
- `os`
- Git
- GitHub
- Terminal/Command Prompt

## 5. Project Structure

```text
vityarthi_project/
├── zombie_sim.py
├── README.md
├── statement.md
├── requirements.txt
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   ├── use_case.md
│   ├── sequence.md
│   ├── component_diagram.md
│   └── testing.md
└── tests/
    └── test_game_logic.md
```

## 6. How to Run

1. Install Python 3.
2. Clone/download the repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python zombie_sim.py
```

On Windows, this may also be:

```bash
py zombie_sim.py
```

No external Python packages are required.

## 7. Gameplay

The player starts with:

- Health: 100
- Food: 5
- Water: 5
- Medkits: 0
- Weapons: none
- Pistol ammunition: 0
- Shotgun ammunition: 0

The player then survives a maximum of seven days.

### Available daily actions

1. Search an abandoned building
2. Search a supermarket
3. Search a gas station
4. Rest for the day
5. Fight the zombies

Every action can change the player's state.

## 8. Combat

The game supports three weapons:

| Weapon | Combat effect |
|---|---|
| Baseball Bat | Defeats the enemy but causes some health loss |
| Pistol | Uses pistol ammunition and causes lower health loss |
| Shotgun | Uses shotgun ammunition and causes the lowest listed health loss |

If the player has no weapon, they must fight with their hands and receive heavier damage.

Medkits can restore health.

## 9. Requirements

### Functional Requirements

- The system shall accept a player's decision to start or exit.
- The system shall progress the game through seven days.
- The system shall display survivor status.
- The system shall provide multiple exploration locations.
- The system shall allow combat and escape decisions.
- The system shall maintain weapons and ammunition.
- The system shall maintain food, water, health and medkits.
- The system shall provide game-over and victory outcomes.

### Non-Functional Requirements

- **Usability:** Menus and prompts should be understandable to a beginner.
- **Performance:** The console game should respond quickly apart from intentional story delays.
- **Reliability:** Invalid menu selections should not immediately crash the game.
- **Maintainability:** Game logic is organized through clearly separated sections for story, exploration, combat and resource handling.
- **Resource efficiency:** The game uses only Python's standard library and does not require a database or external service.
- **Portability:** The program can run on systems with a compatible Python installation.

## 10. Design

The game follows a state-based procedural design. The main game state consists of:

`health`, `food`, `water`, `medkits`, `weapons`, `pistol_ammo`, `shotgun_ammo`, and the current `day`.

The main loop processes one day at a time. Within each day, the player's selected action changes the state. At the end of the day, food and water are consumed and the game checks whether the player is still alive.

## 11. Testing

Testing focuses on:

- Starting with `y`
- Exiting with `n`
- Invalid start input
- Valid and invalid daily choices
- Weapon selection
- Ammunition consumption
- Medkit use
- Food/water depletion
- Health reaching zero
- Seven-day victory condition

## 12. Future Enhancements

- Convert the large procedural file into separate Python modules.
- Add a save/load system.
- Add random zombie encounters.
- Add more weapons and weapon durability.
- Add difficulty levels.
- Add a scoring system.
- Add sound effects or a graphical interface.
- Add automated unit tests around extracted game-logic functions.

## 13. Academic Relevance

The project demonstrates practical use of Python fundamentals including variables, lists, loops, conditionals, input handling, string formatting, modules, state management and procedural control flow.


