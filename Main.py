import util
from GameCoordinator import GameCoordinator
from util import sprint


def main():
    coordinator = GameCoordinator()

    sprint(
        """The day was warm and sunny in the village.
In one of the village house's lived an adventurer 
called Gilbert (Hey that's you!). 
Gilbert like any other adventurer was rigorously 
using his saturday training in the sword.

By the time the clock struck 10 in the morning,
Gilbert had become rather famished.
Gilbert heads inside his house to make a sandwich.
'OH NO' Cries Gilbert as he looks around.
There are none of his special ingredients to make a sandwich.

And this is where the adventure of Gilbert and the perfect sandwich begins!

Where do you wish to go Gilbert? North(N),East(E),South(S), or W(W):
        """
    )

    while True:
        command_input = input("> ")
        coordinator.exe_command(command_input)


if __name__ == "__main__":
    util.IS_DEV = True
    main()
