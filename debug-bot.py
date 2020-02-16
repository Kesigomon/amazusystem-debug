# はじまりのじゅもん
import discord
client = discord.Client()

# 起動通知処理部
@client.event
async def on_ready():
    channel = client.get_channel(678483492564107284)
    await channel.send('起動しました。')

# リアクション解除時の処理一覧
from discord.utils import get
@client.event
async def on_raw_reaction_remove(payload):
    # ピン解除処理部
    if payload.emoji.name == '📌':
        user = client.get_user(payload.user_id)
        if user.bot: return
        else:
            channel = client.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            if message.pinned == 1:
                reaction = get(message.reactions, emoji=payload.emoji.name)
                if reaction == 1:
                    await message.unpin()
                    await message.channel.send(f"メッセージのピン留めを解除しました。")
                else: await channel.send(f"バグ１")

# Botの起動とDiscordサーバーへの接続処理部
client.run('Njc4NDQ0MDgwNTQ3NDk1OTgw.Xki4ZQ.GJJ1JVcj20rCT_3u4qnQQonRvSc')