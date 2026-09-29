# Zombie Survival Simulator — Project Report

## 1. Introduction

Zombie Survival Simulator is a console-based Python survival game developed as a practical application of programming fundamentals. The player must survive seven days after a fictional zombie outbreak by making decisions about exploration, resources, combat and rest.

## 2. Problem Statement

The project models a constrained survival scenario where limited resources and player decisions affect the outcome. It demonstrates how conditional logic, loops and mutable program state can be combined to create an interactive simulation.

## 3. Objectives

- Build an interactive Python application.
- Apply fundamental programming constructs.
- Implement resource and inventory management.
- Implement branching decisions.
- Provide meaningful game outcomes.
- Practice Git/GitHub version control.

## 4. Functional Requirements

The system provides seven-day progression, exploration locations, resource management, combat, weapons, ammunition, medkits and victory/game-over conditions.

## 5. Non-Functional Requirements

The system aims for usability, performance, reliability, maintainability, resource efficiency and portability.

## 6. System Architecture

The current architecture is procedural and state-based. A central game loop controls daily progression and calls different branches for exploration, rest and combat. See `docs/architecture.md`.

## 7. Design Diagrams

The repository includes workflow, use-case, sequence and component diagrams in the `docs/` directory.

## 8. Design Decisions and Rationale

Python standard-library modules were selected so the game can run without installing external packages. A console interface was selected because the project focuses on programming logic rather than graphical development.

A shared game state stores health, food, water, medkits, weapons and ammunition. This allows player decisions to have persistent consequences across days.

## 9. Implementation Details

The program initializes the survivor state and then enters a seven-day loop. Each day displays story content and survivor statistics. The player chooses one of five main actions.

Exploration branches can provide food, water, medkits, weapons or dangerous encounters. Combat allows the player to choose available weapons or escape. Rest restores health and may consume a medkit. At the end of each day, food and water decrease.

If health reaches zero, the game ends. If the player completes all seven days, the rescue ending is displayed.

## 10. Results

The game provides a complete interactive terminal experience with ASCII art, story progression, resource tracking, exploration and combat.

## 11. Testing

Manual test cases cover startup, menu selection, exploration, combat, weapon selection, medkits, resource depletion, game over and victory.

## 12. Challenges Faced

- Managing many branching choices in one program.
- Maintaining health, food, water, weapons, ammunition and medkits consistently.
- Handling invalid user input.
- Designing readable console output.
- Keeping the game progression understandable while adding multiple outcomes.

## 13. Learnings

The project provided practical experience with Python variables, lists, loops, conditions, user input, string formatting, standard-library modules and state management. It also highlighted why large procedural programs eventually benefit from modularization and automated testing.

## 14. Future Enhancements

- Refactor the current large file into multiple modules.
- Add automated unit tests.
- Add difficulty levels.
- Add randomized events and zombie encounters.
- Add save/load functionality.
- Add scoring and achievements.
- Add a graphical interface.

## 15. References

- Python documentation: https://docs.python.org/3/
- Git documentation: https://git-scm.com/doc
