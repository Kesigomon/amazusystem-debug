# はじまりのじゅもん
import discord
client = discord.Client()

# 起動通知処理部
@client.event
async def on_ready():
    channel = client.get_channel(678483492564107284)
    await channel.send('起動しました。')

# Botの起動とDiscordサーバーへの接続処理部
client.run('Njc4NDQ0MDgwNTQ3NDk1OTgw.Xki4ZQ.GJJ1JVcj20rCT_3u4qnQQonRvSc')