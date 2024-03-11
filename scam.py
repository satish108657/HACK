import time
import random
import string
import sys

# List of 50 passwords
passwords = [
    "Alice123456", "Bob987654", "Charlie246810", "David1357911", "Emily3691215",
    "Frank258147", "Grace753951", "Henry159753", "Ivy357159", "Jack951753",
    "Kate753159", "Leo753123", "Mia1234567", "Noah9876543", "Olivia3691215",
    "Peter2581478", "Quinn7539517", "Ryan1597532", "Stella3571594", "Tom9517539",
    "Vera7531596", "Will7531234", "Zoe1234567", "Aaron9876543", "Bella3691215",
    "Chris2581478", "Dana7539517", "Eric1597532", "Fiona3571594", "George9517539",
    "Hannah7531596", "Ian7531234", "Julia1234567", "Kevin9876543", "Lily3691215",
    "Mike2581478", "Nora7539517", "Owen1597532", "Penny3571594", "Quinn9517539",
    "Rose7531596", "Sam7531234", "Tina1234567", "Victor9876543", "Wendy3691215",
    "Xavier2581478", "Yara7539517", "Zach1597532", "Abby3571594", "Ben9517539",
    "Cindy7531596", "Dean7531234", "Eva1234567", "Felix9876543", "Gina3691215",
    "Hank2581478", "Ingrid7539517", "Jake1597532", "Kelly3571594", "Lisa9517539",
    "Max7531596", "Nina7531234", "Oscar1234567", "Paula9876543", "Quinn3691215",
    "Ray2581478", "Sarah7539517", "Tim1597532", "Uma3571594", "Vince9517539",
    "Wendy7531596", "Xander7531234", "Yvonne1234567", "Zane9876543", "Abby3691215",
    "Barry2581478", "Clara7539517", "Dean1597532", "Eliza3571594", "Fred9517539",
    "Grace7531596", "Hank7531234", "Iris1234567", "Jake9876543", "Kim3691215",
    "Luke2581478", "Mia7539517", "Nate1597532", "Olivia3571594", "Paul9517539",
    "Rose7531596", "Sam7531234", "Tina1234567", "Victor9876543", "Wendy3691215",
    "Xavier2581478", "Yara7539517", "Zach1597532", "Abby3571594", "Ben9517539"
]

def print_logo():
    logo = '''\033[1;36m
       _____ _____  _____ __  __ ______ 
      / ____|  __ \|_   _|  \/  |  ____|
     | |    | |__) | | | | \  / | |__   
     | |    |  _  /  | | | |\/| |  __|  
     | |____| | \ \ _| |_| |  | | |____ 
      \_____|_|  \_\_____|_|  |_|______|
                                            '''
    print(logo)

def number_attack(victim_name, victim_number):
    print(f"\nAttacking {victim_name}'s number: {victim_number}")
    
    # Displaying progress bar for the attack
    print("   Attack in progress:")
    for i in range(1, 11):
        progress = f"  [{'=' * i}{' ' * (10 - i)}] {10 * i}%"
        sys.stdout.write('\r' + progress)
        sys.stdout.flush()
        time.sleep(100)  # Simulating 1 second
    
    # Selecting a random password from the list
    password = random.choice(passwords)
    
    print("\n   Attack complete.")
    print(f"   Victim's number: {victim_number}, Generated password: {password}. Exiting...")

def gmail_attack(victim_email):
    print(f"\n  Attacking {victim_email}...")
    
    # Displaying progress bar for the attack
    print("   Attack in progress:")
    for i in range(1, 11):
        progress = f"  [{'=' * i}{' ' * (10 - i)}] {10 * i}%"
        sys.stdout.write('\r' + progress)
        sys.stdout.flush()
        time.sleep(1)  # Simulating 1 second
    
    # Selecting a random password from the list
    password = random.choice(passwords)
    
    print("\n    Attack complete.")
    print(f"     Victim's email: {victim_email}, Generated password: {password}. Exiting...")

def random_attack(victim_name):
    print(f"\n   Attacking {victim_name}...")
    
    # Displaying progress bar for the attack
    print("   Attack in progress:")
    for i in range(1, 11):
        progress = f"  [{'=' * i}{' ' * (10 - i)}] {10 * i}%"
        sys.stdout.write('\r' + progress)
        sys.stdout.flush()
        time.sleep(1)  # Simulating 1 second
    
    # Selecting a random password from the list
    password = random.choice(passwords)
    
    print("\n   Attack complete.")
    print(f"   Target: {victim_name}, Generated password: {password}. Exiting...")

def facebook_menu():
    print("\n\033[1;34m    Facebook Menu:")
    print("    \033[1;32m1. \033[1;31mRandom attack")
    print("    \033[1;32m2. \033[1;31mGmail attack")
    print("    \033[1;32m3. \033[1;31mNumber attack")

def instagram_menu():
    print("\n\033[1;34m    Instagram Menu:")
    print("    \033[1;32m1. \033[1;31mUrl attack")
    print("    \033[1;32m2. \033[1;31mGmail attack")
    print("    \033[1;32m3. \033[1;31mNumber attack")

# Logo print karna
print_logo()

# Main menu display
print("\033[1;32m    Main Menu:")
print("   \033[1;34m1. \033[1;31m   Facebook")
print("   \033[1;34m2. \033[1;31m   Instagram")
print("   \033[1;34m3. \033[1;31m   Exit")

# User se main menu choice input lena
main_choice = input("\n     Choose option: ")

# Facebook menu options
if main_choice == '1':
    facebook_menu()
    facebook_choice = input("\n     Choose option: ")
    if facebook_choice == '1':
        victim_name = input("   Enter victim's Facebook username: ")
        victim_link = input("   Enter victim's facebook link: ")
        random_attack(victim_name, victim_link)
    elif facebook_choice == '2':
        victim_name = input("   Enter victim's Facebook username: ")
        victim_email = input("   Enter victim's Gmail linked with Facebook: ")
        gmail_attack(victim_name, victim_email)
    elif facebook_choice == '3':
        victim_name = input("   Enter victim's Facebook username: ")
        victim_number = input("   Enter victim's phone number linked with Facebook: ")
        number_attack(victim_name, victim_number)
    else:
        print("Invalid choice! Please select a valid option.")

# Instagram menu options
elif main_choice == '2':
    instagram_menu()
    instagram_choice = input("\n     Choose option: ")
    if instagram_choice == '1':
        victim_name = input("   Enter victim's Instagram username: ")
        random_attack(victim_name)
    elif instagram_choice == '2':
        victim_email = input("   Enter victim's Gmail linked with Instagram: ")
        gmail_attack(victim_email)
    elif instagram_choice == '3':
        victim_name = input("   Enter victim's Instagram username: ")
        victim_number = input("   Enter victim's phone number linked with Instagram: ")
        number_attack(victim_name, victim_number)
    else:
        print("Invalid choice! Please select a valid option.")

# Exit the program
elif main_choice == '3':
    print("Exiting...")
else:
    print("Invalid choice! Please select a valid option.")
