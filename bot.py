import discord
import asyncio
import requests

# Your bot token and user ID
TOKEN = 'YOUR_BOT_TOKEN'
USER_ID = YOUR_USER_ID  # Replace with your Discord user ID

# Initialize the bot client with intents
intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def check_server_status():
    url = "https://api.mcstatus.io/v2/status/java/example.aternos.com:portnumber"
    cooldown = False  # Flag to manage the cooldown state

    while True:
        try:
            if not cooldown:  # Only check if not on cooldown
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    motd_clean = data.get("motd", {}).get("clean", "")
                    if motd_clean == "MOTD ONLINE MESSAGE HERE":
                        user = await client.fetch_user(USER_ID)
                        await user.send("The server is now welcoming players!")
                        
                        # Set cooldown to True and start 1-hour cooldown
                        cooldown = True
                        await asyncio.sleep(3600)  # 1 hour in seconds
                        cooldown = False  # Reset cooldown after the wait
                else:
                    print(f"Failed to fetch status. HTTP {response.status_code}")
        except Exception as e:
            print(f"Error checking server status: {e}")
        
        await asyncio.sleep(60)  # Check every minute if not on cooldown

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # Start the server status check loop
    client.loop.create_task(check_server_status())

client.run(TOKEN)
