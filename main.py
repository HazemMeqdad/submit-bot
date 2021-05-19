"""
MIT License

Copyright (c) 2021 NamNam#0090 & OTTWAW team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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

# احبك يا رجلي "ODQ0NjI1MjczMzAzMDcyODU4.YKVJnA.qM6aLnzVCpYvjX-IxD9j-0Ybgpk"

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
