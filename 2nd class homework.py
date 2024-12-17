import colorama
import sys
import time
from colorama import Fore,Style
from textblob import TextBlob

colorama.init(autoreset=True)

username = ""
convseration_history = []
positive_count = 0
negative_count = 0
nuetral_count = 0

def show_processing_animation():
    print(f"{Fore.CYAN}Detecting Sentiment for {username}",end="")
    for i in range(0,3):
        time.sleep(0.5)
        print('.',end="")
        sys.stdout.flush()
def analyze_sentiment(text):
    global positive_count, negative_count, nuetral_count, convseration_history
    blob = TextBlob(text)
    show_processing_animation()
    sentiment = blob.sentiment.polarity
    convseration_history.append(text)
    print("")
    if sentiment > 0.75:
        print(f"{Fore.GREEN}Very Positive")
        positive_count += 1
    elif 0.25 < sentiment <= 0.75:
        print(f"{Fore.GREEN}Positive")
        positive_count += 1
    elif -0.25 <= sentiment <= 0.25:
        print(f"{Fore.YELLOW}Neutral")
        nuetral_count =+ 1
    elif sentiment < 0.75:
        print(f"{Fore.RED}Very Negative")
        negative_count += 1
    elif 0.25 > sentiment >= 0.75:
        print(f"{Fore.RED}Negative")
        negative_count += 1

def execute_command(command):
    global positive_count, negative_count, nuetral_count, convseration_history
    if command == "history":
        for i in convseration_history:
            print(i)
    elif command == "summary":
        print(f"{Fore.GREEN}Positive Count: {positive_count}")
        print(f"{Fore.YELLOW}Neutral Count: {nuetral_count}")
        print(f"{Fore.RED}Negative Count: {negative_count}")
    elif command == "clear":
        negative_count = positive_count = nuetral_count = 0
        convseration_history.clear()
    elif command == "exit":
        print("Bye!")
        quit()
    elif command == "continue":
        print('Continuing')

username = input("Enter your name: \n")
print(f"Hi, Nice to meet you {username}")
while True:
    text = input("Enter any sentence: \n")
    analyze_sentiment(text)
    print("Choose a option among the following\nHistory | Summary | Clear | Exit | Continue")
    command = input('').lower()
    execute_command(command)
