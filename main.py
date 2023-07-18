import asyncio
import json
import logging

import discord

from bot import StretchRemindersBot


async def main():
    # Setup logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("stretchremindersbot.log")
    file_handler.setLevel(logging.ERROR)
    datefmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter("{asctime}:{levelname}:{name}: {message}", datefmt=datefmt, style="{")
    file_handler.setFormatter(formatter)
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    # Load config json
    with open("config.json") as fp:
        config = json.load(fp)

    # Initialise bot instance
    intents = discord.Intents.default()
    intents.members = True
    intents.presences = True
    intents.message_content = True
    bot = StretchRemindersBot(command_prefix="!", intents=intents)

    # Load extensions
    await bot.load_extension("cogs.admin")
    await bot.load_extension("cogs.autoreminders")

    # Start bot loop
    await bot.start(config)

if __name__ == "__main__":
    asyncio.run(main())
