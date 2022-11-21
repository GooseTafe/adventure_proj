from Locations import *
from Characters.Adventurer import Adventurer
from random import randint
from enum import Enum
from util import sprint
from Help import help_printout



# sets the movement directions
class MovementAction(Enum):
    WEST = 1
    EAST = 2
    NORTH = 3
    SOUTH = 4


# Defining the coordinates to move
class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # Correlates the movement direction to a coordinate (vector)
    @staticmethod
    def from_movement(action: MovementAction):
        if action is MovementAction.WEST:
            return Coordinate(-1, 0)
        if action is MovementAction.EAST:
            return Coordinate(1, 0)
        if action is MovementAction.NORTH:
            return Coordinate(0, 1)
        if action is MovementAction.SOUTH:
            return Coordinate(0, -1)

    def as_2d_matrix_vec(self) -> tuple[int, int]:
        # reverse the up / down val
        if self.y != 0:
            return self.y * -1, self.x

        return self.y, self.x

    def __str__(self):
        return f"({self.x}, {self.y})"


# checks location is not None
class Locations:
    def __init__(self, locations, size):
        self.locations = locations
        self.size = size

    # Gets the current location from the current vector
    def get_loc_from_point(self, point: tuple[int, int]):
        if 0 <= point[0] < self.size[0] and 0 <= point[1] < self.size[1]:
            return self.locations[point[0]][point[1]]
        return None


# GAME COORDINATOR THAT CONTROLS AND RUNS THE GAME
# EVERYTHING GOES THROUGH HERE
class GameCoordinator:

    def __init__(self):
        self.adventurer = Adventurer()
        self.player_pos = self.adventurer.position
        # the 2d array of locations
        self.locations = Locations([
            [None, House(), None],
            [None, Village(), None],
            [Plains(), Forest(), Clearing()],
            [WheatField(), Forest2(), Mountain()],
            [None, None, Cave()],
            [None, Forge(), Volcano()]
        ], (6, 3))

    # Creates the player map
    #TODO: add when player visits area map updates with an identifier of current location and where has been travelled
    def player_map(self):
        print((len(self.locations.locations[0]) * 3 + 5) * "%")

        for row in self.locations.locations:
            print("%" + (len(self.locations.locations[0]) * 3 + 3) * " " + "%")
            print("%", end="")
            for cell in row:
                if cell is None:
                    print("_X_|", end="")
                else:
                    print(f"_{cell.name[0]}_|", end="")
            print("%")
        print((len(self.locations.locations[0]) * 3 + 5) * "%")

    # list of commands
    def exe_command(self, command: str):
        # separating command string into command and object
        command_raw = command.split(' ')
        # setting the command type e.g. move
        command_type = command_raw[0].lower()
        action = command_raw[1:]
        # getting the relevant command from the pre-set dictionary of commands to run function
        if command_type == "move":
            self.move(action)
        elif command_type == "scan":
            self.scan()
        elif command_type == "search":
            self.search(action)
        elif command_type == "talk":
            self.talk(action)
        elif command_type == "store":
            self.store(action)
        elif command_type == "open":
            self.open(action)
        elif command_type == "craft":
            self.craft(action)
        elif command_type == "eat":
            self.eat(action)
        elif command_type == "attack":
            self.attack(action)
        elif command_type == "defend":
            self.defend()
        elif command_type == "help":
            help_printout()
        elif command_type == "exit":
            print("Exiting Game, thank you for playing")
            exit()
        elif action is None:
            print("invalid command, check the help file for commands")
            return False

    #Gets the current location information based on player_pos
    def current_loc(self) -> BaseLocation:
        return self.locations.get_loc_from_point(self.player_pos)

    # move gilbert by vector = location class
    def move(self, args: list[str]):
        action = Coordinate(0, 0)
        direction = args[0].lower()
        if direction == 'n':
            sprint("Gilbert decides to move North")
            action = MovementAction.NORTH
        elif direction == 'e':
            sprint("Gilbert decides to move East")
            action = MovementAction.EAST
        elif direction == 's':
            sprint("Gilbert decides to move South")
            action = MovementAction.SOUTH
        elif direction == 'w':
            sprint("Gilbert decides to move West")
            action = MovementAction.WEST
        else:
            print("direction unknown please choose N,E,S,W direction:")
            return False

        temp_player_pos = tuple(map(sum, zip(self.player_pos, Coordinate.from_movement(action).as_2d_matrix_vec())))
        if self.locations.get_loc_from_point(temp_player_pos) is not None:
            self.player_pos = temp_player_pos
        else:
            print("not a valid direction")

    # scan area print area description
    def scan(self):
        print(self.locations.get_loc_from_point(self.player_pos).description)

    # search command
    def search(self, args: list[str]):
        search_type = args[0].lower()
        # search bag option
        if search_type == "bag":
            search_item = input("Gilbert searches his inventory for: ")
            if self.adventurer.bag.search_inventory(search_item) is not None:
                print(f"Found \x1b[32m{self.adventurer.bag.search_inventory(search_item)}\x1b[0m in Gilbert's bag")
            else:
                print(f"Did not find \x1b[31m{search_item}\x1b[0m in Gilbert's bag")
        # search area option
        elif search_type == "area":
            print("Gilbert is having a look around")
            if self.current_loc().item is not None:
                print(f"Found: {self.current_loc().item.description}")
                print("adding item to bag")
                self.adventurer.bag.items.append(self.current_loc().item.name)
            else:
                print("Nothing to be found here")
        # search body option
        elif search_type == "body":
            if self.current_loc().character is None:
                sprint(f"No body here to search")
            elif self.current_loc().character is not None and self.current_loc().character.dead is True:
                sprint(f"You cannot search this body")
            else:
                sprint(f"Gilbert searches {self.current_loc().character.name} for anything")
                self.current_loc().character.item_drop(self.adventurer.bag)
        else:
            print("invalid command, check the help file for commands")

    # talk to character
    def talk(self, args: list[str]):
        character = args[0].lower()
        loc_character = self.current_loc().character
        if loc_character is not None and character == loc_character.name:
            print(loc_character.description)
            prompt = loc_character.prompts(self.adventurer.bag)
            if prompt is not None:
                self.adventurer.bag = prompt
        else:
            print(f"character by the name of {character} cannot be found at this location")

    # store item in bag
    def store(self, args: list[str]):
        item_to_store = args[0].lower()
        self.adventurer.bag.items.append(item_to_store)
        print(f"adding item {item_to_store} to bag")

    # open map command
    def open(self, args: list[str]):
        open_object = args[0].lower()
        if open_object == "map":
            self.player_map()

    # craft command while in forge
    def craft(self, args: list[str]):
        craft_type = args[0].lower()
        if craft_type == "sandwich" and self.current_loc().name.lower() == "forge":
            sprint("""Gilbert starts, the careful and precise procedure of creating the perfect sandwich...
            Gilbert puts the wheat in the refinery leaving it to powder and bake into bread from the wheat fields...
            Gilbert cuts up the meat and lightly salts it with the minerals he'd gotten from the miner...
            Gilbert puts the seasoned meat onto the grill... *SSssszzzzz*
            Gilbert shreds the vegetables and slices the cheese...
            *DING* The bread is done...
            Gilbert gathers his ingredients and precisely layers everything into the perfect sandwich""")
            self.adventurer.bag.remove_item("meat")
            self.adventurer.bag.remove_item("cheese")
            self.adventurer.bag.remove_item("minerals")
            self.adventurer.bag.remove_item("vegetables")
            self.adventurer.bag.remove_item("wheat")

            self.adventurer.bag.add_item("sandwich")
            sprint("Gilbert decides to eat this perfect sandwich back at home")
        else:
            sprint("You can only craft at the forge")

    # eat game objective item while in home
    def eat(self, args: list[str]):
        food = args[0].lower()
        if food == "sandwich" and self.current_loc().name.lower() == "home":
            sprint("""Gilbert settles down at the table with his sandwich on a plate
            'finally' he thinks, and raises the sandwich to his mouth...
            ...
            ...
            a tear rolls down his cheek...
            perfect.""")
            sprint('')
            sprint('')
            sprint("THE END")
            exit()
        else:
            sprint("Gilbert doesnt want to eat the sandwich here he wants to eat it at home")

    # defend against incoming attack
    def defend(self):
        sprint("Gilbert raises his shield to defend against the oncoming attack")
        return True

    #attack character
    def attack(self, args: list[str] = []):
        exiter = True
        blocked = False
        damage = randint(0, 8)
        opponent = self.current_loc()
        opponent_name = self.current_loc().character.name
        opponent_life = self.current_loc().character.life
        sword = self.adventurer.bag.search_inventory("sword")
        adventurer_life = self.adventurer.life
        target = args[0].lower()
        print(target)
        if target == opponent_name.lower():
            # if player hasn't found the sword use fists with low damage
            if target is not None and sword is None:
                sprint("Are you sure you want to attack with your fists and not a weapon?")
                choice = input("> ")
                if choice.lower() == 'y':
                    sprint(f"""Very well, your funeral
                            Gilbert throws a right hook at {opponent_name}""")
                    while exiter:
                        if adventurer_life <= 0:
                            sprint(f"""Gilbert's life is: {adventurer_life}...
                            Gilbert has been slain by {opponent_name}...
                            GAME OVER""")
                            exit()
                        else:
                            opponent_life = opponent_life - damage
                            sprint(f"{opponent_name}'s life is now at: {opponent_life}")
                            if opponent_life <= 0:
                                sprint(f"Gilbert has punched {opponent_name} to death ")
                                break
                            elif opponent_life > 0:
                                opponent.character.pre_attack_phase()
                                sprint("Do you want to defend against the incoming attack?")
                                blocking = input("> ").lower()
                                defending = False
                                if blocking == "defend":
                                    defending = GameCoordinator.exe_command(self, blocking)
                                elif blocking == 'n':
                                    sprint("Gilbert decides not to block")
                                else:
                                    sprint("You took to long to decide to block with your shield")
                                if defending is True:
                                    blocked = True
                                    oppo_damage = opponent.character.attack_response(blocked)
                                    adventurer_life = adventurer_life - oppo_damage
                                    sprint(f"Gilbert's life is now at: {adventurer_life}")
                                else:
                                    oppo_damage = opponent.character.attack_response(blocked)
                                    adventurer_life = adventurer_life - oppo_damage
                                    sprint(f"Gilbert's life is now at: {adventurer_life}")

                                sprint("Do you want to throw a punch again?: ")
                                choice = input("> ")
                                if choice.lower() == "attack" or choice.lower() == 'n':
                                    sprint(f"Gilbert continues to attack {opponent}")
                                elif choice.lower() == "n":
                                    sprint(f"Gilbert turns tail and runs from this fight")

                elif choice.lower() == 'n':
                    sprint("You should find a weapon")
                else:
                    print("invalid choice, please enter: y = yes | n = no")
                    choice = input("> ")
            # if player has found sword attack with higher damage
            elif target is not None and opponent.character is not None and sword is not None and opponent.character.enemy is True:
                sprint("Gilbert draws his sword and gets into his fighters stance...")
                sprint(f"Gilbert swings his sword at {opponent_name}")
                while exiter:
                    if adventurer_life <= 0:
                        sprint(f"""Gilbert's life is: {adventurer_life}...
                        Gilbert has been slain by {opponent_name}...
                        GAME OVER""")
                        exit()
                    else:
                        opponent_life = opponent_life - damage
                        sprint(f"{opponent_name}'s life is now at: {opponent_life}")
                        if opponent_life <= 0:
                            sprint(f""" with one last breath {opponent_name} topples over with cuts all over...
                                   Gilbert has slain {opponent_name} \
                                   """)
                            break
                        elif opponent_life > 0:
                            opponent.character.pre_attack_phase()
                            sprint("Do you want to defend against the incoming attack?")
                            blocking = input("> ").lower()
                            defending = False
                            if blocking == "defend":
                                defending = GameCoordinator.exe_command(self, blocking)
                            elif blocking == 'n':
                                sprint("Gilbert decides not to block")
                            else:
                                sprint("You took to long to decide to block with your shield")
                            if defending is True:
                                blocked = True
                                oppo_damage = opponent.character.attack_response(blocked)
                                adventurer_life = adventurer_life - oppo_damage
                                sprint(f"Gilbert's life is now at: {adventurer_life}")
                            else:
                                oppo_damage = opponent.character.attack_response(blocked)
                                adventurer_life = adventurer_life - oppo_damage
                                sprint(f"Gilbert's life is now at: {adventurer_life}")
                            sprint("Do you want to attack again?: ")
                            choice = input("> ")
                            if choice.lower() == "attack" or choice.lower() == 'n':
                                sprint(f"Gilbert continues to swing his sword at {opponent_name}")
                            elif choice.lower() == "n":
                                sprint(f"Gilbert turns tail and runs from this fight")
            elif target != opponent_name.lower():
                sprint(f"There is no one by the name of {target} to attack")
            else:
                sprint("There is nothing to attack here")


