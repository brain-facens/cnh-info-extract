from library.extra_functions import *


# COLOR.
WHITE = "\033[1m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
GRAY = "\033[1;37m"
END = "\033[m"

# KEYBOARD.
QUIT = ord("q")
EXTRACT_INFO = 32

# TEXT.
QUIT_TXT = "Quit. [q]"
INFO_TXT = "Extract text. [SPACE]"

def INTRO() -> None:
    __line = 45
    os.system("clear")
    print("-"*__line)
    print(f"\t{WHITE}CNH INFO EXTRACT - ({END}{CYAN}BRAIN{END}{WHITE}){END}")
    print("-"*__line)
    print(f"\n{CYAN}Initializing..{END}")
    time.sleep(2)

def ERROR(_txt:str) -> None:
    
    print(f"{RED}ERROR:{END}", end=" ")
    print(f"{YELLOW}{_txt}{END}")

def WARNING(_txt:str) -> None:

    print(f"{YELLOW}ATTENTION:{END}", end=" ")
    print(f"{WHITE}{_txt}{END}")

def print_results(_data:dict) -> None:
    __line = 20
    os.system("clear")
    print("-"*__line)
    for key in _data.keys():
        print(str(key) + ": " + str(_data[key]))
    print("-"*__line)

def save_results(_data:dict) -> None:
    with open("result.json", "w") as f:
        json.dump(_data, f)

def save_fig_(_image) -> None:
    
    from PIL import Image
    __img = Image.fromarray(_image, mode="RGB")
    __img.save("notebooks/img.png")
    print("Saved!")