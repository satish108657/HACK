import time
import random
import string
import sys

# List of 50 passwords
passwords = [
    "1111111", "22222222", "33333333", "44444444", "55555555",
    "6666666", "777777", "88888888", "9999999", "000000000",
    "11111111111", "2222222222", "3333333333", "4444444444", "555555555555",
    "666666666666", "7777777777", "8888888888", "99999999988", "000000",
    "11122u373", "22828283383", "33838838383", "4484848", "558858585",
    "688882", "788888", "89929922", "99928181", "1003883383",
    "7288119", "7282919", "74738392", "747492", "838363",
    "82910100", "83376363", "819191001", "82837737", "838291910",
    "81928373", "838383747", "9494994", "4773828", "8392920",
    "838292919", "838382901", "8373773", "8383839", "7484890"
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
        progress = f"[{'=' * i}{' ' * (10 - i)}] {10 * i}%"
        sys.stdout.write('\r' + progress)
        sys.stdout.flush()
        time.sleep(1)  # Simulating 1 second
    
    # Selecting a random password from the list
    password = random.choice(passwords)
    
    print("\n   Attack complete.")
    print(f"   Victim's number: {victim_number}, Generated password: {password}. Exiting...")

def gmail_attack(victim_email):
    print(f"\n  Attacking {victim_email}...")
    
    # Displaying progress bar for the attack
    print("   Attack in progress:")
    for i in range(1, 11):
        progress = f"[{'=' * i}{' ' * (10 - i)}] {10 * i}%"
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
        progress = f"[{'=' * i}{' ' * (10 - i)}] {10 * i}%"
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
    print("    \033[1;32m1. \033[1;31mRandom attack")
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
        random_attack(victim_name)
    elif facebook_choice == '2':
        victim_email = input("   Enter victim's Gmail linked with Facebook: ")
        gmail_attack(victim_email)
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