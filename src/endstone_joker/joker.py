from endstone.plugin import Plugin
from endstone import ColorFormat
from endstone.command import *
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

    name = "Joker"
    version = "0.1.0"
    api_version = "0.4"
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
            a = asyncio.run(self.get_jokes())
            sender.send_message(f"{cf.MATERIAL_AMETHYST}" + a)
            return True