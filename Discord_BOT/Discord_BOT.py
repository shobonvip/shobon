import discord

# 起動時に実行するお
client = discord.Client()

@client.event
async def on_ready():
    print('起動')


# ほ ん へ
@client.event
async def on_message(message):
    if message.author.id == "459591712369541140":
        print("a")
        await client.delete_message(message)
    print(message.author.name)


# bot起動構文
client.run('NTMyNTc3MDE3OTg4OTA3MDI4.Dxegpg.ShmleaxXvDJBwF_EpJmnZrhxZBk')
