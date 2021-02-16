<h1 align="center">
  Submit Discord Bot
  <br>
</h1>


## 🚀 Getting Started

These are needed to be able to run **Submit bot**.

- [Python 3.8](https://www.python.org/)
- [Discord.py[Rewrite]](https://github.com/Rapptz/discord.py/tree/rewrite)

## ⚙️ Configuration

Edit `config.json` to your liking.

**⚠️ Note: Never commit or share your token keys publicly ⚠️**

```json
{
  "token": "token", 
  "prefix": "!",
  "submit_channel": "811002423303995442",
  "language": "en",
  "cooldown": "86400",
  "role": "Helper",

  "questions": [
    "Example: write your name:",
    "Example: write your age:",
    "Example: write your job:",
    "Example: etc."
  ],

  "aliases": {
    "submit": ["sub"],
    "accept": [],
    "reject": []
  }
}
```

If he wants to make the token hidden, you can leave it blank in the `config.json` file, and put it in the `.env` file, for example.\
`token = <your token>`

## 🤝 Setup

1️⃣ **install the packages**
```shell
pip install -r requirements.txt
```
2️⃣ **Run the bot**
```shell
python main.py
```

## ✨ Commands

`!submit` => to send your submit\
`!reject` => to reject one of the applicants\
`!accept` => to accept one of the applicants\

## ⚠ MIT License

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

## 🔖 Support

![Discord](https://img.shields.io/discord/654423706294026270) 
