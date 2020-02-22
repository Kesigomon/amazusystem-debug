import discord
import os
client = discord.Client()
token = os.environ["TOKEN"]

# 各チャンネルIDを代入
startup_ch = client.get_channel(678507923311165443)
register_ch = client.get_channel(678511640693440526)
join_notify_ch = client.get_channel(678511642346258432)
questionnaire_ch = client.get_channel(678585920294748160)
# 起動時の処理一覧
@client.event
async def on_ready():
    # 待機
    await client.wait_until_ready()

    # 起動通知処理部
    await startup_ch.send("起動しました。")

# メッセージ送信時の処理一覧
@client.event
async def on_message(message):
    if message.author.bot:
        return
    # アカウント登録処理部
    if message.content == "!register":
        if not message.channel == register_ch:
            await message.channel.send("ここでは実行できません。")
            return
        role = discord.utils.get(message.guild.roles, name="member")
        await message.author.add_roles(role)
        join = client.get_channel(678585920294748160)
        user_count = sum(1 for member in join.members if not member.bot)
        await join.send(f"{message.author.name}が参加しました。\n現在の参加者数は{user_count}人です。")
        dm = await message.author.create_dm()
        await dm.send((f"{message.author.mention} アカウントが登録されました。\n"
                        "まず何をすればいいかわからない方へ▽\n"
                        "step1: <#655311853844430858> にて自己紹介をしましょう！\n"
                        "step2: <#653919145729064970> から各サーバーに入室してください！\n"
                        "【Tips】スパム防止のため #welcome と #register は非表示になりました。\n"
                        "そして #welcome の上位互換の <#661167351412162580> が閲覧できるようになりました。"))

    # サーバーアンケート処理部
    if message.channel.id == 660392800399130633:
        sansei = '<:sansei:660392552528347157>'
        hantai = '<:hantai:660392595159121959>'
        await message.add_reaction(sansei)
        await message.add_reaction(hantai)

# リアクション追加時の処理一覧
@client.event
async def on_raw_reaction_add(payload):
    # ピン留め処理部
    if payload.emoji.name == '📌':
        user = client.get_user(payload.user_id)
        if user.bot:
            return
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        if message.pinned:
            return
        await message.pin()
        await channel.send(f"{user.name}がピン留めしました。")

# リアクション解除時の処理一覧
@client.event
async def on_raw_reaction_remove(payload):
    # ピン解除処理部
    if payload.emoji.name == '📌':
        user = client.get_user(payload.user_id)
        if user.bot:
            return
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        if not message.pinned:
            return
        reaction = discord.utils.get(
            message.reactions, emoji=payload.emoji.name)
        if reaction:
            return
        await message.unpin()
        await channel.send("リアクションがゼロになったため、ピン留めが解除されました。")
        embed = discord.Embed(
            title=f"送信者:{message.author}", description=f"メッセージ内容:{message.content}", color=0xff0000)
        await channel.send(embed=embed)

client.run(token)