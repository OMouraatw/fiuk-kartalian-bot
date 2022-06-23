import hikari
import lightbulb
from lightbulb import commands

import random

from possums import *


#Token e Prefix do App

bot = lightbulb.BotApp(
    token='Secret',
    prefix='!'
)

#Evento de início

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has started!')

#Comando = Ping Pong!
@bot.command
@lightbulb.command('ping', 'retorna com pong (/)')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context):
    latência = bot.heartbeat_latency * 1000
    await ctx.respond('Latência: {}ms https://cf-images.us-east-1.prod.boltdns.net/v1/static/694940094001/ff6df457-ba21-46fb-8f49-224223c38101/6848d6ae-9953-4bc4-82c9-044b496e0779/1280x720/match/image.jpg'.format(round(latência, 2)),)

#Evento = Nome para o Possum Every Hour

#Comando = Nome para o Possum

@bot.command
@lightbulb.command('OPOSSIM', 'Dê um nome para o Possum que acabou de aparecer!')
@lightbulb.implements(lightbulb.PrefixCommand)
async def OPOSSIM(ctx: lightbulb.Context):
    await ctx.respond("O nome desse possum é {}".format(random.choice(possum_names)))

@bot.command
@lightbulb.command('nomepossum', 'Dê um nome para o Possum que acabou de aparecer!')
@lightbulb.implements(lightbulb.SlashCommand)
async def nomepossum(ctx: lightbulb.Context):
    await ctx.respond("O nome desse possum é {}".format(random.choice(possum_names)))

@bot.command
@lightbulb.option("escolhas", "Escolha um tipo de mídia para receber seu kin:", str)
@lightbulb.command("kinassign", "Indeciso sobre seu kin? Vamos escolher um para você!")
@lightbulb.implements(commands.SlashCommand)
async def kinassign(ctx: lightbulb.Context) -> None:
    escolha = ctx.options.escolhas
    if escolha == "anime":
        await ctx.respond("Segundo minhas análises... Você tem kin em {}".format(random.choice(kinass_game_names)))
        return
    
    if escolha == "jogo":
        await ctx.respond("Segundo minhas análises Você tem kin em {}".format(random.choice(kinass_game_names)))
        return

    if escolha == "filme":
        await ctx.respond("Segundo minhas análises Você tem kin em {}".format(random.choice(kinass_game_names)))
        return
    
    if escolha == "série":
        await ctx.respond("Segundo minhas análises Você tem kin em {}".format(random.choice(kinass_game_names)))
        return

    if escolha == "música":
        await ctx.respond("Segundo minhas análisesVocê tem kin em {}".format(random.choice(kinass_game_names)))
        return

    else:
        await ctx.respond("Categoria não encontrada :(")
        await ctx.respond("As categorias até agora são {}".format(categoria_names))


bot.run()
