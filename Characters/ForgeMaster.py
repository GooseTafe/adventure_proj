from Items import Money
from Characters.BaseCharacter import BaseCharacter


class ForgeMaster(BaseCharacter):
    def __init__(self):
        self.name = "forgemaster"
        self.description = """An extremely hairy short stature dwarf dressed in a leather apron, gloves, and metal 
        welding helmet (I wonder how he has not caught on fire yet?) """
        self.items = [] # TODO: add items that can be found on the Forge Master
        self.life = 3
        self.condition = False

    def prompts(self):
        exiter = True
        print("Forge Master: HO HO HO *BUURRPRP* Who do we have here?")
        print("Forge Master: Gilbert you say? Well *BUURRPPP* G-Giblert what can i do for you?")
        print("Gilbert inquires into using the Forge Master's mighty forge to create the perfect sandwich")
        print("Forge Master: sure I'll allow you to use my forge, only if you have the right tools")
        # TODO: search for cooking tools in inventory to allow conversation to continue