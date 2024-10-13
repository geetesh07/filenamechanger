from telethon import TelegramClient, events
from telethon.tl.types import DocumentAttributeFilename, MessageMediaDocument

# Add your API ID, API hash, and Bot Token here
api_id = '6572614'
api_hash = 'a0df85f9cdca64fa7418d41ace4b6513'
bot_token = '6850555173:AAGbHvEAqZhyAeweaZiFFhw4dOd0Oq_blFI'

# Caption to be appended
custom_caption = """\nPackage : Fluid Mechanics (V) - ME - (L3691215182124) - Hinglish - Live 2024 - 1st Sep

Course :- ESE + GATE+SES(GS) 2024 Live Online Foundation Course (L6) Mechanical Engineering (H)"""

# Initialize the client
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# Event handler for new messages in channels
@client.on(events.NewMessage(chats=-1002326130210))  # Replace with your actual channel ID
async def handle_channel_message(event):
    original_caption = None  # Initialize original caption

    # Check if the message contains media (photo, video, document, etc.)
    if event.is_channel and event.media:
        media_list = []

        # Handle albums or single media files
        if hasattr(event.message, 'media_group_id'):  # If the message contains an album of media
            media_list = event.message.get_media_entities()
        else:
            media_list.append(event.media)  # Just a single media file

        # Loop through each media item in the list
        for media in media_list:
            original_caption = None  # Reset original caption for each file

            # Check if the media contains a document (e.g. file, video, etc.)
            if isinstance(media, MessageMediaDocument):
                for attribute in media.document.attributes:
                    if isinstance(attribute, DocumentAttributeFilename):
                        original_caption = attribute.file_name

            # If no file name, fall back to message caption (if available)
            if not original_caption:
                original_caption = event.message.message or "No Title"  # Fallback if no caption

            # Append the custom caption to the original caption
            new_caption = f"{original_caption}{custom_caption}"

            # Edit the message with the new caption
            await event.edit(new_caption)

    # If no media is present, add only the custom caption
    elif event.is_channel and not event.media:
        await event.edit(custom_caption)

# Start the bot
print("Bot is running...")
client.run_until_disconnected()
