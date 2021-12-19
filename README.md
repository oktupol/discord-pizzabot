# Discord Pizzabot

Simple bot that says 🍕 whenever someone mentions pizza.

This bot was mainly made as a proof of concept for an application that is
deployed on a Raspberry Pi in my home using a CI Workflow. I used my
[`oktupol/rsync-onion`](https://github.com/oktupol/rsync-onion) action; that
way I'm able to enjoy the beauty of Continuous Integration on something like my
Raspberry Pi without having to open and forward a publicly accessible port on
my home router.

## Installation

This bot requires Python 3 and pip 3 to be installed.

1. Download source files
    ```bash
    git pull https://github.com/oktupol/discord-pizzabot.git
    cd discord-pizzabot
    ```
2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

## Usage

discord-pizzabot requires following environment variables:

- `DISCORD_TOKEN` - Authentication Token for the Discord Bot.
- `GUILD_ID` - ID of the server (guild) in which the bot is supposed to be
  active. You can find out the server id by opening Discord in a web browser
  and opening a server there; the first numeric ID in the url is the server id.
  
  The Bot account has to be added to the server manually prior to starting the
  program.
  
For development purposes, you can save these inside a .env file in the
repository root.

Start the bot using

```bash
python src/bot.py
```