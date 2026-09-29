# System Architecture

```text
+---------------------------+
|       Player / User       |
+-------------+-------------+
              |
              v
+---------------------------+
|      Input / Menu Layer   |
|  start + daily decisions  |
+-------------+-------------+
              |
              v
+---------------------------+
|      Game Controller      |
|     7-day game loop       |
+-------------+-------------+
              |
       +------+------+
       |             |
       v             v
+-------------+ +-------------+
| Exploration | |   Combat    |
| Locations   | |  Decisions  |
+------+------+ +------+------+
       |               |
       +-------+-------+
               v
      +--------------------+
      |   Game State       |
      | health             |
      | food / water       |
      | medkits            |
      | weapons            |
      | ammunition         |
      | current day        |
      +---------+----------+
                |
                v
      +--------------------+
      | Outcome Controller |
      | Game Over / Win    |
      +--------------------+
```

## Architectural Style

The current implementation is a procedural, state-based console application.

The central game loop controls progression. Player input selects branches, and each branch directly changes shared game-state variables.

This design is appropriate for a beginner-level Python project because it demonstrates fundamental control flow without introducing unnecessary frameworks.
