
import discord
from discord import app_commands

from config import COMMIT_HASH, GUILD_ID
from lib.platforms import Platform

class SbgImitate(app_commands.Command):
    def __init__(self) -> None:
        super().__init__(
            name="sbg_imitate",
            description="Query the one and only ARESx legend",
            callback=self.cmd_callback,
        )

    # TODO: do i extend database with all sbg messagess from history, and upload them once
    # after which i can upload only new messages with intents
    # TODO: second option is to query a random message every time we call the command and
    # add sleep a bit so the bot takes time
    async def cmd_callback(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Kekw, SBG insert photo and random msg here")
