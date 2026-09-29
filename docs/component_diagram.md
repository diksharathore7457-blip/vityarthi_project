# Component / Class Design

The current code is procedural rather than class-based, so a class diagram would misrepresent the implementation. The following component view reflects the actual structure.

```text
+----------------------+
| Startup / Input      |
+----------+-----------+
           |
           v
+----------------------+
| Main 7-Day Loop      |
+----------+-----------+
           |
     +-----+-----+----------------+
     |           |                |
     v           v                v
+---------+ +---------+      +----------+
|Building | |Supermarket|     |Gas Station|
+---------+ +---------+      +----------+
     |           |                |
     +-----------+----------------+
                 |
                 v
          +--------------+
          | Combat Logic |
          +------+-------+
                 |
                 v
          +--------------+
          | State Data   |
          | health       |
          | food         |
          | water        |
          | medkits      |
          | weapons      |
          | ammo         |
          +--------------+
                 |
                 v
          +--------------+
          | Outcome      |
          +--------------+
```

## Implementation Note

The assignment asks for modular implementation. The present game is intentionally kept as one procedural source file so its current behaviour remains unchanged. A future refactor can extract the components above into separate Python modules and functions.
