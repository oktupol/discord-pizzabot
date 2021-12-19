from discord import utils
from discord.client import Client
from discord.guild import Guild
from discord.message import Message


class PizzaClient(Client):
  def __init__(self, *, active_guild_id: int, loop=None, **options):
    super().__init__(loop=loop, **options)
    self.active_guild_id = active_guild_id

  async def on_ready(self):
    self.active_guild: Guild = utils.get(self.guilds, id=self.active_guild_id)
    print(f'{self.user} has connected to Discord server {self.active_guild.name}')

  async def on_message(self, message: Message):
    if message.author == self.user:
      return
    if message.guild != self.active_guild:
      return

    content: str = message.content

    if (content.lower().strip() == 'pizza'):
      await message.channel.send('🍕')
    elif ('pizza' in content.lower()):
      await message.add_reaction('🍕')
