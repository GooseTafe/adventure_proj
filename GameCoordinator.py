from Locations.Cave import Cave
from Locations.Clearing import Clearing
from Locations.Forest import Forest
from Locations.Forge import Forge
from Locations.House import House
from Locations.Mountain import Mountain
from Locations.Plains import Plains
from Locations.Village import Village
from Locations.Volcano import Volcano
from Locations.WheatField import WheatField
from Characters.Adventurer import Adventurer
from Locations.BaseLocation import BaseLocation
from Locations.Forest2 import Forest2


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
        ], (3, 6))

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
        vector = (0, 0)
        direction = args[0].lower()
        if direction == 'n':
            print("Gilbert decides to move North")
            vector = (-1, 0)
        elif direction == 'e':
            print("Gilbert decides to move East")
            vector = (0, 1)
        elif direction == 's':
            print("Gilbert decides to move South")
            vector = (1, 0)
        elif direction == 'w':
            print("Gilbert decides to move West")
            vector = (0, -1)
        # TODO: add 'help' entry where it opens a help file and outputs file to screen
        else:
            print("direction unknown please choose N,E,S,W direction:")
            return False
        temp_player_pos = tuple(map(sum, zip(self.player_pos, vector)))
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
            print(f"Found {self.adventurer.bag.search_inventory(search_item)} in Gilbert's bag")
        elif search_type == "area":
            print("Gilbert is having a look around")
            if self.current_loc().item is not None:
                print(f"Found: {self.current_loc().item.description}")
                print("adding item to bag")
                self.adventurer.bag.items.append(self.current_loc().item)
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
            loc_character.prompts()
        else:
            print(f"character by the name of {character} cannot be found at this location")

    # store item in bag
    def store(self, args: list[str]):
        item_to_store = args[0].lower()
        self.adventurer.bag.items.append(item_to_store)
        print(f"adding item {item_to_store} to bag")

    def open(self, args: list[str]):
        pass

    def craft(self, args: list[str]):
        pass

    def attack(self, args: list[str]):
        pass

    def defend(self, args: list[str]):
        pass