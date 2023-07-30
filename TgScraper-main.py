#Made By PersonalPr0xy

import time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
import os

os.system("cls")
print("""
  _____     ____                            
 |_   _|_ _/ ___|  ___ _ __ __ _ _ __   ___ 
   | |/ _` \___ \ / __| '__/ _` | '_ \ / _ |
   | | (_| |___) | (__| | | (_| | |_) |  __/
   |_|\__, |____/ \___|_|  \__,_| .__/ \___|
      |___/                     |_|             
            Made by PersonalPr0xy
    """)


print("╔═══════════════════════════════╗")
print("║ Choice |        Option        ║")
print("╟────────┼──────────────────────╢")
print("║   1    | Telegram scrape      ║")
print("║   2    | Telegram users adder ║")
print("╚═══════════════════════════════╝")


choice = int(input("select the option: "))

if choice == 1:

    api_id = input("Enter the API_ID of the telegram:")
    api_hash = input('Enter the API_Hash of the telegram:')
    server_link = input("Enter invite to server , Example, t.me/(servername): ")

    with TelegramClient('session_name', api_id, api_hash) as client:
        client.start()

        entity = client.get_entity(server_link)
        all_users = client.get_participants(entity)

        with open('user.txt', 'w') as file:
            for user in all_users:
                file.write(f"Username: {user.username}, ID: {user.id}\n")

    print('The user list has been successfully written to user.txt.')


elif choice == 2:
    api_id = input("Enter the API_ID of the telegram:")
    api_hash = input('Enter the API_Hash of the telegram:')
    phone_number = input('Please enter your mobile number: ')
    group_id = int(input("Write your ID of the group you want to invite people to: "))


    def format_time(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


    with TelegramClient('session_name', api_id, api_hash) as client:
        client.start()

        with open('user.txt', 'r') as file:
            for line in file:
                if line.startswith('Username:'):
                    username, user_id = line.split('ID: ')
                    user_id = int(user_id.strip())
                    users = [user_id]

                    while True:
                        try:
                            result = client(InviteToChannelRequest(group_id, users))
                            print(f"User {username} has been successfully added to the group.")
                            time.sleep(300)
                            break
                        except Exception as e:
                            if "A wait of" in str(e):
                                wait_time = int(str(e).split("A wait of")[1].split("seconds")[0].strip())
                                if "Too many requests" in str(e):
                                    print(
                                        f"Error adding user {username} to a group: Too many requests. wait 10 minutes.")
                                    time.sleep(600)
                                else:
                                    print(
                                        f"Error adding user {username} to a group: A wait of {wait_time} seconds is required")
                                    for remaining_time in range(wait_time, 0, -1):
                                        print(f"Remaining time: {format_time(remaining_time)}", end='\r')
                                        time.sleep(1)
                                    print("\n")
                            else:
                                print(f"Error adding user {username} to a group: {str(e)}")
                                break

else:
    print("Invalid choice. Please select 1 or 2.")
