import asyncio
import json

import discord

from bot import StretchRemindersBot


async def main():
    discord.utils.setup_logging()

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
