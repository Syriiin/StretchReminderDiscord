import logging

from discord.ext import commands

logger = logging.getLogger(__name__)


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def cog_check(self, ctx):
        return self.bot.is_owner(ctx.author)

    @commands.hybrid_command()
    async def ping(self, ctx: commands.Context):
        """
        Checks latency
        """
        await ctx.send(f"Pong: {round(self.bot.latency * 1000)}ms")

    @commands.hybrid_command()
    async def synchere(self, ctx: commands.Context):
        """
        Syncs the global command tree to the current guild as guild commands
        """
        self.bot.tree.copy_global_to(guild=ctx.guild)
        await self.bot.tree.sync(guild=ctx.guild)

        await ctx.send(f"Synced command tree to guild `{ctx.guild.name} ({ctx.guild.id})` successfully")

    @commands.hybrid_command()
    async def unsynchere(self, ctx: commands.Context):
        """
        Un-syncs (removes) the global command tree from the current guild
        """
        self.bot.tree.clear_commands(guild=ctx.guild)
        await self.bot.tree.sync(guild=ctx.guild)

        await ctx.send(f"Un-synced command tree from guild `{ctx.guild.name} ({ctx.guild.id})` successfully")

    @commands.hybrid_command()
    async def sync(self, ctx: commands.Context):
        """
        Syncs the global command tree
        """
        await self.bot.tree.sync()

        await ctx.send(f"Synced command tree successfully")

    @commands.hybrid_command()
    async def load(self, ctx: commands.Context, extension_name: str):
        """
        Loads an extension module
        """
        if not extension_name.startswith("cogs."):
            extension_name = f"cogs.{extension_name}"
        try:
            await self.bot.load_extension(extension_name)
            logger.info(f"Loaded extension {extension_name}")
            await ctx.send("`{0}` successfully loaded.".format(extension_name))
        except commands.ExtensionError as e:
            await ctx.send("`{0}` failed to be loaded. Check logs for details.".format(extension_name))
            logger.error(e)

    @commands.hybrid_command()
    async def reload(self, ctx: commands.Context, extension_name: str):
        """
        Reloads an extension module
        """
        if not extension_name.startswith("cogs."):
            extension_name = f"cogs.{extension_name}"
        try:
            await self.bot.reload_extension(extension_name)
            logger.info(f"Reloaded extension {extension_name}")
            await ctx.send("`{0}` successfully reloaded.".format(extension_name))
        except commands.ExtensionError as e:
            await ctx.send("`{0}` failed to be reloaded. Check logs for details.".format(extension_name))
            logger.error(e)

    @commands.hybrid_command()
    async def unload(self, ctx: commands.Context, extension_name: str):
        """
        Unloads an extension module
        """
        if not extension_name.startswith("cogs."):
            extension_name = f"cogs.{extension_name}"
        try:
            await self.bot.unload_extension(extension_name)
            logger.info(f"Unloaded extension {extension_name}")
            await ctx.send("`{0}` successfully unloaded.".format(extension_name))
        except commands.ExtensionError as e:
            await ctx.send("`{0}` failed to be unloaded. Check logs for details.".format(extension_name))
            logger.error(e)

async def setup(bot):
    await bot.add_cog(Admin(bot))
