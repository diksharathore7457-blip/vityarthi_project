# Testing Approach

## Manual Functional Test Cases

| ID | Test | Expected Result |
|---|---|---|
| T01 | Enter `y` at startup | Game begins |
| T02 | Enter `n` at startup | Program exits |
| T03 | Enter invalid startup input | Program asks again |
| T04 | Select building | Building choices appear |
| T05 | Select supermarket | Supermarket choices appear |
| T06 | Select gas station | Gas station choices appear |
| T07 | Select rest | Health increases up to 100 |
| T08 | Use a medkit | Health increases and medkit count decreases |
| T09 | Select a weapon | Weapon-specific combat branch runs |
| T10 | Use pistol/shotgun | Corresponding ammunition decreases |
| T11 | Enter invalid weapon choice | Penalty is applied |
| T12 | Health reaches zero | Game-over message appears |
| T13 | Survive seven days | Rescue/victory ending appears |
| T14 | Food reaches zero | Health penalty is applied |
| T15 | Water reaches zero | Health penalty is applied |

## Validation

The program validates several menu and weapon selections using conditional checks and `isdigit()` where numeric weapon choices are expected.

## Future Automated Testing

The current implementation is interactive and therefore difficult to unit-test directly. The next engineering step would be to extract state-changing logic into functions such as:

- `use_medkit()`
- `consume_resources()`
- `apply_damage()`
- `select_weapon()`
- `check_game_over()`

Those pure functions could then be covered with Python's `unittest` module.
