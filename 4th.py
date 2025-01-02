import random
import re
from colorama import Fore,init
init(autoreset=True)
destination = {
    "beaches": ["Bali","Maldives","Phuket"],
    "mountains":["Mount everest","Rocky Mountains","Swiss alps"],
    "cities":["Tokyo","Delhi","New York"]
}
jokes = [
    "why are bees in america, becaue they are usb",
    "joke: you"
]
def greetuser():
    print(Fore.CYAN + "Hello I am travel bot")
    name = input(Fore.BLUE + "May I know your name?")
    print(Fore.GREEN + f"Nice to meet you {name}! How can i assist you today?")
    return name
def show_help():
    print(Fore.CYAN + "\nI can you to the following things")
    print(Fore.GREEN + "1 - Provide Trevel Recoemdation")
    print(Fore.GREEN + "2 - Offer Packaging tips")
    print(Fore.GREEN + "3 - Travel Jokes")
def proces_input(user_input):
    user_input = user_input.strip().lower()
    user_input = re.sub(r"\s+","",user_input)
    return user_input
def provide_rec():
    print(Fore.CYAN+ "TravelBot: Sure. What are you interested\nbeaches\ncities\nmountains")
    prefrece = input(Fore.YELLOW+"You: ")
    prefrece = proces_input(prefrece)
    if prefrece in destination:
        suggestion = random.choice(destination[prefrece])
        print(Fore.GREEN + f"TravelBot: How about visiting {suggestion}")
        print(Fore.CYAN+ "TravelBot: Do you like this suggetion? (yes/no)")
        respone = input(Fore.BLUE+ "You: ").strip().lower()
        if respone == "yes":
            print(Fore.GREEN + "TravelBot: Great have fun!")
        elif respone == "no":
            print(Fore.YELLOW + "Lets find another destination")
            provide_rec()
        else:
            print(Fore.RED + "Sorry I don't have that recommendations")
            show_help()
def offer_pack():
    print(Fore.GREEN+"Where are you going to")
    dest = input(Fore.CYAN+"You: ")
    dest = proces_input(dest)
    print(Fore.GREEN + "How long will you be there?")
    days = input(Fore.BLUE+"You: ")
    print(Fore.GREEN + f"TravelBot: Travel packing tips for {destination} for {days} days")
    print("Pack clother and check weather")
def tell_joke():
        joke = random.choice(jokes)
        print(Fore.YELLOW + f"TravelBot: {joke}")

def chat():
    name  = greetuser()
    show_help()
    while True:
        user_input = input(Fore.YELLOW+f"{name}: ")
        user_input = proces_input(user_input)
        if "recommendation" in user_input or "suggest" in user_input:
            provide_rec()
        elif "pack" in user_input or "packing" in user_input:
            offer_pack()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.RED+"TravelBot: Safe Travel!")
            break
        else:
            print(Fore.RED+"TravelBot: I am sorry I wasn't able to understand you.")
chat()
