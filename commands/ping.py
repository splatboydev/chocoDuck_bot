from commands.base_command  import BaseCommand
import discord


class Ping(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Get the bot's connection stats."
        params = ["lower", "upper"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):

        embed = discord.Embed(title="Pong 🏓")
        embed.set_timestamp()

        await message.channel.send(embed)
