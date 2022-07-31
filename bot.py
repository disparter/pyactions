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
    try:
        user_character = character.get_user_character(character_name)
        dnd_class = character.get_dnd_class(character_name)
    except Exception:
        await ctx.send(f'character {character_name} was not found')
    else:
        try:
            spell_slot = spell.get_mana(spell_name, dnd_class)
        except Exception:
            await ctx.send(f'spell {spell_name} was not found in {user_character.dnd_class} spell list')
        else:
            response = mana.get_current_mana_after_spell(user_character, spell_slot)
            await ctx.send(f'{user_character.character_name}  current mana points is {response}t')


@bot.command(name='create_character',
             help='Create a character based on an unique name, dnd_class and total mana points')
async def create_character(ctx, character_name, dnd_class, mana_total:int):
    user_character = character.create_character(mana_total, character_name, dnd_class)
    await ctx.send(f'Your character {user_character.character_name} was created')


bot.run(TOKEN)
