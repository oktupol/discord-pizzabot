import os
from dotenv import load_dotenv

from pizza_client import PizzaClient

if __name__ == '__main__':
  load_dotenv()
  TOKEN = os.getenv('DISCORD_TOKEN')
  GUILD_ID = os.getenv('GUILD_ID')

  client = PizzaClient(active_guild_id = int(GUILD_ID))
  client.run(TOKEN)
  