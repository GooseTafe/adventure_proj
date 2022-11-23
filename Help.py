# prints out the list of commands for the user when help is called

def help_printout():
    print("""
    HELP COMMANDS
    =============
    '>' is the start of a command
    MOVEMENT:
    North = n, East = e, South = s, West = w
    > move [direction] 
    
    COMBAT:
    attack a character
    > attack [character]
    block the attackers attack for reduced damage
    > block
    
    ENVIRONMENT:
    get a description of the area
    > scan
    search the area for items
    > search area
    store an item
    > store [item]
    
    INTERACTION:
    talk to a character
    > talk [character]
    search character(dead)
    > search body
    search your inventory
    > search bag
    search for a specific item
    > search bag > [item]
    store an item
    > store [item]
    open the map
    > open map
    
    GAME SPECIFIC:
    To eat the sandwich
    > eat [sandwich]
    
    
    CHOICE:
    when offered an option of;
    yes = y
    > y
    no = n
    > n
    
    EXIT GAME:
    > exit
    """)