import discord
from discord.ext import commands
import json
from prettytable import PrettyTable
import os
from termcolor import colored

with open('./config.json', 'r') as f:
    config = json.load(f)

EXTENSIONS = [
    "submit",
]


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=config["prefix"],
            case_insensitive=True,
            allowed_mentions=discord.AllowedMentions(
                everyone=False,
                users=True,
                roles=False),
            intents=discord.Intents.all()
)
        self.remove_command("help")
        if config["token"] == "" or config["token"] == "token":
            self.token = os.environ['token']
        else:
            self.token = config["token"]

        for filename in EXTENSIONS:
            try:
                self.load_extension(f'cogs.{filename}')
                print(colored('lode ', "green") + '{}'.format(filename))
            except Exception:
                print(colored('error in', "red") + filename)
                print(colored('error in', Exception))

    async def on_ready(self):
        if config['language'] != "ar" and config['language'] != "en":
            print(colored(f"Warning: No support the language `{config['language']}`", "red"))
        tap = PrettyTable(
            ['Name Bot', 'Id', 'prefix', 'commands'])
        tap.add_row([
            self.user.display_name,
            str(self.user.id),
            self.command_prefix,
            len(self.commands),
        ])
        print(tap)
        print(colored("Copyright (c) 2021 NamNam#0090 & OTTWAW team", "green"))

    def run(self):
        super().run(self.token, reconnect=True)


if __name__ == '__main__':
    client = Bot()
    client.run()
# Copyright (c) 2021 NamNam#0090 & OTTWAW team
