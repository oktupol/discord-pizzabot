from discord import utils
from discord.client import Client
from discord.guild import Guild
from discord.message import Message
from discord.reaction import Reaction


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
      return

    await self.pizza_reaction(message)

  
  async def on_message_edit(self, before: Message, after: Message): 
    if after.author == self.user:
      return
    if after.guild != self.active_guild:
      return

    await self.pizza_reaction(after)


  async def pizza_reaction(self, message: Message):
    own_reactions: list[str] = [ r.emoji for r in message.reactions if r.me ]

    reactions_target: list[str] = []

    content: str = message.content.lower()
    if ('pineapple pizza' in content or 'pizza with pineapple' in content):
      reactions_target.append('👎')
      reactions_target.append('🚫')
    
    elif ('pizza' in content):
      reactions_target.append('🍕')
      
    reactions_to_remove = [ r for r in own_reactions if r not in reactions_target ]
    reactions_to_add = [ r for r in reactions_target if r not in own_reactions]
    
    for r in reactions_to_remove:
      await message.remove_reaction(r, self.user)
    
    for r in reactions_to_add:
      await message.add_reaction(r)
