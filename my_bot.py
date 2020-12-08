import discord

client = discord.Client()

@client.event

async def on_ready():

    general_channel = client.get_channel(725997163804360709)

    await general_channel.send("Hello")

client.run('Nzg1NzYyOTg5NjQyMDg4NDQ5.X88kzw.-_Zo259hnJjQmyLOB0y-UepChcE')
