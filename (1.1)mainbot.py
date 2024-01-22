import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='=', intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.reply("Hello World")


@bot.event
async def on_ready():
    print(f'Bot is connected as {bot.user}')


@bot.event
async def on_message(message):
    # Проверяем, что сообщение отправлено определенным пользователем
    if message.author.id == profile id here:  # ID пользователя
        # Проверяем, что сообщение содержит упоминание роли
        if "<@&role id>" in str(message.content):  # ID вашей роли
            # Отправляем ответное сообщение
            await message.reply('<@&role id>')

    await bot.process_commands(message)


bot.run('Your token')  # Замените на токен вашего бота
