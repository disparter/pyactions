import os

from discord.ext import commands
from dotenv import load_dotenv

import character
import mana
import spell

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='cast_spell', help='Define how much mana was used when a spell is cast')
async def cast_spell(ctx, spell_name, character_name):
    dnd_class = character.get_dnd_class(character_name)
    character_id = character.get_character_id(character_name)
    spell_slot = spell.get_mana(spell_name, dnd_class)
    response = mana.get_current_mana_after_spell(character_id, spell_slot)

    await ctx.send(response)

bot.run(TOKEN)
