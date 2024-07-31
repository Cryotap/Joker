from endstone.plugin import Plugin
from endstone import ColorFormat
from endstone.command import *
from endstone import Player
import asyncio
import requests


class Joker(Plugin):
    cf = ColorFormat

    def on_load(self) -> None:
        self.logger.info("Loaded!")

    def on_enable(self) -> None:
        self.logger.info("Enabled!")

    def on_disable(self) -> None:
        self.logger.info("Disabled!")

    name = "joker"
    prefix = "Joker"
    version = "0.1.1"
    api_version = "0.5"
    description = "Python joke plugin for Endstone!"

    commands = {
        "joker": {
            "description": "Let me tell you a joke.",
            "usages": ["/joker"],
            "permissions": ["joker.command.use"],
        },
    }

    permissions = {
        "joker.command.use": {
            "description": "Allow users to use the plugin manager form.",
            "default": True,
        },
    }

    async def get_jokes(self):
        response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt")
        return response.text

    def on_command(self, sender: CommandSender, command: Command, args: list[str], cf=cf) -> bool:
        if command.name == "joker":
            if isinstance(sender, Player):
                a = asyncio.run(self.get_jokes())
                sender.send_message(f"{cf.MATERIAL_AMETHYST}" + a)
                return True
            else:
                sender.send_error_message(f"{cf.MATERIAL_REDSTONE}" + "You must be a player to run this command")
