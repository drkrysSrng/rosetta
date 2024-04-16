from tele_api import *
import os
def main_menu():
    print("""
                                                 
         _____                 _    _        
        | __  | ___  ___  ___ | |_ | |_  ___ 
        |    -|| . ||_ -|| -_||  _||  _|| .'|
        |__|__||___||___||___||_|  |_|  |__,|
        
                """)

    while True:

        print("\n")
        print("1. All messages")
        print("2. Messges by date")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            with client:
                client.loop.run_until_complete(get_messges())
        elif choice == "2":
            # Get user input for start and end dates
            date_input = input("Enter the date (YYYY-MM-DD): ")
            with client:
                client.loop.run_until_complete(get_messages_by_date(date_input))

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    if not os.path.exists(folder_path):
        # Create the directory
        os.makedirs(folder_path)
    main_menu()


