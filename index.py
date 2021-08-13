# coding: UTF-8
# token情報やチャンネルidなどの定数を別のファイルにおく
import const
# 関数関係
import game
# インストールした discord.py を読み込む
import discord

araki = game.player("あらき")
kim = game.player("きむ")

# 自分のBotのアクセストークンに置き換えてください
TOKEN = const.token

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
  print('...ready')

async def shori(message, player):
  if player.start_msg:
    player.start_msg = False
    await message.channel.send("-------------------------\n初期化済みです。\n-------------------------")
  if message.content == "half":
    await message.channel.send(player.half())
    return
  if message.content == "ls":
    await message.channel.send(player.string())
    return
  if message.content.isdecimal():
    num = int(message.content)
    await message.channel.send(player.diff(num))
    return
  if message.content[0] == "-":
    num = int(message.content)
    await message.channel.send(player.diff(num))
    return
  await message.channel.send("数値またはhalf,lsを指定してください")
  return

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
  # メッセージ送信者がBotだった場合は無視する
  if message.author.bot:
    return
  # 全体に影響がある部分
  if message.content == "reset":
    araki.__init__("あらき")
    kim.__init__("きむ")
    await message.channel.send("リセットしました。")
    return
  # ここに影響がある部分
  if message.channel.name == 'あらき':
    await shori(message, araki)
    return
  if message.channel.name == 'きむ':
    await shori(message, kim)
    return
  return 
  # if message.channel.name == 'プレイヤーa-1':
  #   await channel.playera1(message)
  #   return
  # if message.channel.name == 'プレイヤーa-2':
  #   await channel.playera2(message)
  #   return
  # if message.channel.name == 'プレイヤーb-1':
  #   await channel.playerb1(message)
  #   return
  # if message.channel.name == 'プレイヤーb-2':
  #   await channel.playerb2(message)
  #   return

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)