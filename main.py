import time
from pyrogram import Client

api_id = 'your api_id (without paws)'
api_hash = 'your api_hash'

def menu():
    print('!!! Be sure to read the documentation, it describes how to use the script !!!')
    choose_option = int(input('1.Invite to a Telegram group, from another group\n2.Parsing of all users from channel telegrams\n3.Spamer\nChoose option (1 or 2): '))
    if choose_option == 1:
        option1()
    elif choose_option == 2:
        option2()
    elif choose_option == 3:
        option3()

def option1():
    parsing_chat = str(input('Where to get users from: '))
    invited_chat = str(input('Where to invite users: '))
    get_parsing_chat_id(parsing_chat)
    get_invite_chat_id(invited_chat)

def get_parsing_chat_id(parsing_chat):
    with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
        get_parsing_chat = app.get_chat(parsing_chat)
        return get_parsing_chat.id

def get_invite_chat_id(invited_chat):
    with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
        get_invited_chat = app.get_chat(invited_chat)
        return get_invited_chat.id

def get_chat_users(get_parsing_chat_id):
    user_ids = []
    with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
        chat_id = get_parsing_chat_id
        members = app.get_chat_members(chat_id)

        for member in members:
            user_ids.append(member.user.id)

    return user_ids

def add_users_to_group(user_ids, get_invited_chat_id):
    with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
        chat_id = get_invited_chat_id
        for user_id in user_ids:
            try:
                app.add_chat_members(chat_id, [user_id])
                print(f"User with ID {user_id} added to the group.")
                time.sleep(10)
            except Exception as e:
                print(f"Failed to add user with ID {user_id}: {e}")
                time.sleep(10)
        print('Invitations ended successfully!')

def option2():
    parsing_user_chat = str(input('Where to get users from: '))
    parsinguser(parsing_user_chat)

def parsinguser(parsing_user_chat):
    with Client("my_account", api_id, api_hash) as app:
        chat = app.get_chat(parsing_user_chat)
        members = app.get_chat_members(chat.id)
        for member in members:
            first_name = member.user.first_name if member.user.first_name else "None"
            username = member.user.username if member.user.username else "None"
            user_id = member.user.id
            with open('users.txt', 'a') as file:
                file_content = file.write(f"ID: {user_id}, Username: {username}, Firstname: {first_name}")
        print('Scraping finished successfull!')

def option3():
    user_spamer = str(input('The user you want to spam: '))
    message = str(input('Messages that should be spammed: '))
    count_message = int(input('Number of messages: '))
    spamer(user_spamer,count_message, message)
def spamer(user_spamer,count_message, message):
    with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
        for i in range(count_message):
            app.send_message(user_spamer, message)
        print('Spamer finished successfull!')

def main():
    menu()

if __name__ == '__main__':
    main()
