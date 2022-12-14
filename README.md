# adventure_proj
Assessment 4 of Applied Python, creating a text based adventure game
[D] = Done
[P] = In Progress
# GAME REQUIREMENTS
1. [D]The program has a name that reflects the adventure’s world.
2. [D]The program has a world that contains at least 10 locations. 
   Each location has a unique name, a description, and zero or more objects. 
3. [D]The program allows the player to navigate the world. 
   It should at least offer to go in the directions N, E, W, and S. 
   The program shows available exits from every location. 
   The player can move in these four directions by only typing the corresponding letter. 
   E.g., entering just the letter N will mean the player moves North.
4. [D]The adventure has at least three additional characters (excluding the player). 
   Each character must have a unique name. The characters can be people, animals, fictional characters, etc.
5. [D]The player can interact with the additional characters (talk, ask questions, etc.) in a meaningful way. 
6. [D]The adventure should have at least ten different objects. Each object must be uniquely named. Objects can be static or not static, visible or invisible, etc. Some (non-static) objects must be able to be picked up by the player and there should be at least five of those. The player should be able to “look at” objects to get additional information.
7. [D]For the purpose of holding objects, the player should have a “rucksack” or similar holding device (i.e., an Inventory).
8. [D]The inventory may hold multiple objects at a time. Objects should be stored using their unique names. Objects must be searched using a simple binary search technique.
9. [D]The adventure must have at least one conditional action. A conditional action is an action that can only be performed if a certain prerequisite holds. For example, a certain door may only open if the player has a key.
10. [P]The adventure must store a simple map (2D) in a file. This map should be updated using a random-access algorithm. The map should have X’s for places that have been visited and a ▢ (space) for places that have not been visited. 
11. [D]The adventure must have a certain goal: that is how to win the game. For example: “Your task is to re-engage the safety system of the reactor core to prevent a core meltdown.” In addition, it’s possible for the player to lose the game (“game over”) under certain conditions. 
After winning or losing the game, the players should be able to start a new game

# SYSTEM REQUIREMENTS
12. [D]The adventure was developed using an IDE.
13. [D]The adventure must be built using a modular approach, preferable in an object-oriented fashion. This means multiple sources files must be used, for example, one per class. 
14. [D]The adventure must be tested in a useful way. Unit tests are encouraged, but a system test is acceptable too.
15. [D]The code must have useful documentation, e.g., docstrings, comments, etc. 
16. [D]The adventure must have clear instructions for the player. No guesswork as to how to run the program is allowed. The instructions must also explain how to win the game.
17. [D]The adventure should follow the “General game play of text adventures” that is described in the Project Scenario. This includes:
    • A starting description of the game
    • Show available exits (mentioned before)
    • Interaction with characters, e.g., “ask information”, “give dime”, etc.
    • Use commands like “look clock”, “get key”, etc. Commands should be kept simple, e.g., in the form of “<verb> <noun>”, for example, “light match”.
    • Objects: fixed, not fixed, (in)visible, having a condition
    • List player’s possessions with the I or Inventory command
18. [D]The adventure MUST NOT have any unsuitable jokes in it, e.g. no rude jokes or puns. Easter eggs are allowed, though, as long as they are SFW.
19. [D]Student has requested feedback early and often during the assessment process
20. [D]The solution has been committed to a GitHub repository and a history of commits is readily available.
21. [D]The code is written in Python3, version 3.8 or higher.
22. [D]The student followed all guidelines, including PEP 8 for writing Python code.
23. [D]The submission’s front page has student name and ID

