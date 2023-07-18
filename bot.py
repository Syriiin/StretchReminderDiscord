import logging
import sys
import traceback

import discord
from discord.ext import commands

logger = logging.getLogger(__name__)

class StretchRemindersBot(commands.Bot):
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.ArgumentParsingError):
            await ctx.send(error)
        elif isinstance(error, commands.CommandInvokeError):
            original = error.original
            if not isinstance(original, discord.HTTPException):
                print(f"In {ctx.command.qualified_name}:", file=sys.stderr)
                traceback.print_tb(original.__traceback__)
                print(f"{original.__class__.__name__}: {original}", file=sys.stderr)

    async def on_ready(self):
        logger.info("Bot ready...")
        await self.change_presence(activity=discord.Game(name="at the gym"))
    
    async def start(self, config):
        logger.info("Bot starting...")
        self.config = config
        await super().start(config["bot_token"])
