from time import sleep
from typing import Union


IS_DEV = True


# Creates a delayed print output
def sprint(strs: Union[str, list[str]]):
    if not isinstance(strs, list):
        strs = [strs]

    for string in strs:
        for c in string:
            print(c, flush=True, end="")
            if not IS_DEV:
                sleep(0.05)
        print()

