from Locations import *
from Characters.Adventurer import Adventurer

from enum import Enum
from util import sprint


class MovementAction(Enum):
    WEST = 1
    EAST = 2
    NORTH = 3
    SOUTH = 4


class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

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

    def get_loc_from_point(self, point: tuple[int, int]):
        if 0 <= point[0] < self.size[0] and 0 <= point[1] < self.size[1]:
            return self.locations[point[0]][point[1]]
        return None


class GameCoordinator:

    def __init__(self):
        self.adventurer = Adventurer()
        self.player_pos = self.adventurer.position
        self.locations = Locations([
            [None, House(), None],
            [None, Village(), None],
            [Plains(), Forest(), Clearing()],
            [WheatField(), Forest2(), Mountain()],
            [None, None, Cave()],
            [None, Forge(), Volcano()]
        ], (6, 3))

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
        elif command_type == "attack":
            self.attack(action)
        elif command_type == "defend":
            self.defend(action)
        elif command_type == "help":
            print("TODO: ADD HELP FILE HERE")
        elif command_type == "exit":
            print("Exiting Game")
            exit()
        elif action is None:
            print("invalid command, check the help file for commands")
            return False

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
        # TODO: add 'help' entry where it opens a help file and outputs file to screen
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

    # search for item in bag
    def search(self, args: list[str]):
        search_type = args[0].lower()

        if search_type == "bag":
            search_item = input("Gilbert searches his inventory for: ")
            if self.adventurer.bag.search_inventory(search_item) is not None:
                print(f"Found \x1b[32m{self.adventurer.bag.search_inventory(search_item)}\x1b[0m in Gilbert's bag")
            else:
                print(f"Did not find \x1b[31m{search_item}\x1b[0m in Gilbert's bag")
        elif search_type == "area":
            print("Gilbert is having a look around")
            if self.current_loc().item is not None:
                print(f"Found: {self.current_loc().item.description}")
                print("adding item to bag")
                self.adventurer.bag.items.append(self.current_loc().item.name)
            else:
                print("Nothing to be found here")
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

    def open(self, args: list[str]):
        open_object = args[0].lower()
        print(f"Gilbert attempts to open {open_object}")
        item_check = self.adventurer.bag.search_inventory("key")
        if item_check is not None and item_check is True:
            print(f"The item needed to open the {open_object} is in Gilbert's bag")
            print(f"Gilbert opens the {open_object} with the key")
        else:
            print(f"Gilbert does not have the right item in his bag to open the {open_object}")

    def craft(self, args: list[str]):
        # TODO: check that all ingredients for the sandwich have been collected before crafting
        # TODO: also check that the cooking tools have been found
        pass

    def attack(self, args: list[str]):
        opponent = self.current_loc().character.name
        atk = args[0].lower()
        if atk == "attack":
            print(f"Gilbert swings his sword at {opponent}")

    def defend(self, args: list[str]):
        pass
