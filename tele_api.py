from telethon import TelegramClient
from datetime import datetime
from telethon.tl.types import MessageMediaPoll  # Import this class to use it for type checking

import time
import pytz

folder_path = "./media_files"

# Replace these with your own values
api_id = 6666666 #int
api_hash = 'API_HASH'
phone_number = 'PHONE_NUMBER'  # include country code
# Create the client and connect
client = TelegramClient(phone_number, api_id, api_hash)
client.start()

# This assumes you have already joined the group
group_url = 'GROUPS_URL_USERNAME'  # Can be the group's username or invite link

async def get_messges():
    # Getting the entity will allow us to interact with it
    group = await client.get_entity(group_url)

    # Fetch 100 messages from the group
    messages = await client.get_messages(group, limit=1000)
    for message in messages:
        print(message.sender_id, message.text)


async def get_messages_by_date(date_input):
    tz = pytz.timezone('UTC')  # Change 'UTC' to your timezone if needed

    specific_date = datetime.strptime(date_input, "%Y-%m-%d")
    start_of_day = tz.localize(datetime.combine(specific_date, datetime.min.time()))
    end_of_day = tz.localize(datetime.combine(specific_date, datetime.max.time()))

    group = await client.get_entity(group_url)
    all_messages = []
    async for message in client.iter_messages(group, offset_date=end_of_day):
        if message.date < start_of_day:
            break
        if start_of_day <= message.date <= end_of_day:
            all_messages.append(message)
            print(f"{message.date}: {message.sender_id} - {message.text}")

            # Check for and handle media (e.g., audio)
            if message.media:
                path = await message.download_media(file=folder_path)
                print(f"Downloaded media to {path}")

    for message in all_messages:
        print(f"{message.date}: {message.sender_id} - {message.text}")
        # Check for and handle polls
        if hasattr(message, 'media') and isinstance(message.media, MessageMediaPoll):
            poll = message.media.poll
            print(f"Poll/Quiz: {poll.question}")
            for answer in poll.answers:
                print(f"Option: {answer.text}")
