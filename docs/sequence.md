# Sequence Diagram

```text
Player          Game Loop        Exploration/Combat       Game State
  |                 |                    |                    |
  |-- start ------->|                    |                    |
  |                 |-- initialize ----->|------------------->|
  |                 |                    |                    |
  |-- choose ------>|                    |                    |
  |                 |-- action --------->|                    |
  |                 |                    |-- update state --->|
  |                 |                    |                    |
  |                 |<-- result ---------|                    |
  |<-- status ------|                    |                    |
  |                 |                    |                    |
  |                 |-- end of day ------------------------->|
  |                 |                    |<-- consume food --|
  |                 |                    |<-- consume water -|
  |                 |                    |                    |
  |                 |-- health check ------------------------>|
  |                 |                    |                    |
  |                 |<-- game over / next day / victory -----|
```

The sequence repeats for each day until health reaches zero or the player completes day seven.
