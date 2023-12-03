# Automation script for Telegram

This Python script uses the Pyrogram library to perform various actions in Telegram, such as inviting users to a group, gathering information about users, and sending messages.

## Getting Started

### Requirements

- Python 3.x installed
- Pyrogram library (`pip install pyrogram')

### Settings

1. Clone the repository or download the script.
2. Get your `api_id` and `api_hash` from the Telegram API website. (https://my.telegram.org/auth).

### Usage

Run the script using Python and follow the on-screen instructions:

```bash
python main.py



!!! We write the names of the channels in this form: https://t.me/example -> example. (That is, the name of the channel is that after "/", in this example, the name of the channel will be 'example') !!!



The script has the following options:
1) Invite members to a group: Allows you to invite users from one group to another.
   To do this, you need to select 1, and enter the name of the channel from which you want to take participants, and then the name of the channel to which you want to invite participants.
2) Collect all users from the channel: Collects information about users from the Telegram channel and saves it to a file.
   To do this, select 2, and enter the name of the channel from which we want to share users.
3) Spammer: Allows sending multiple messages to the user.
   To do this, select 3 and enter the nickname of the user we want to spam (enter the nickname without @), then select the message you want to send and the number of messages.

Important notes:
Be sure to read the documentation that describes the functionality and usage of the script.
Be careful with the spam feature, as it may violate Telegram's usage policy. Use it responsibly.

Contact me on telegram: https://t.me/whyyaskkkmee (@whyyaskkkmee).
