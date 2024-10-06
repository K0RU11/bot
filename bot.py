import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TARGET_USER_ID = 626556492987760641  # Your updated user ID

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message_delete(message):
    if message.author.id == TARGET_USER_ID and message.attachments:
        for attachment in message.attachments:
            await message.channel.send(attachment.url)

# Run the bot using the token from the environment variables
TOKEN = os.getenv("MTI5MjMxODQ2MDkyMzA4ODkwOA.GB57U6.ivUAg2gp6oKwIumlKkfnUz85nC2_f2vauB-mTM")
client.run(TOKEN)
