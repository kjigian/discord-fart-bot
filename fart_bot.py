import discord
import asyncio
import random
import os
from discord.ext import commands
import json
from keep_alive import keep_alive  # Import the keep_alive function

# Configuration
TOKEN = os.environ.get('TOKEN', 'YOUR_BOT_TOKEN')  # Use environment variable if available
FART_SOUNDS_DIR = 'fart_sounds'  # Directory containing fart sound files
CONFIG_FILE = 'config.json'

# Default configuration
default_config = {
    'target_users': {},  # guild_id -> user_id mapping
}

# Bot setup
intents = discord.Intents.default()
intents.voice_states = True  # Need this to detect voice state changes
intents.message_content = True  # Need this for commands
bot = commands.Bot(command_prefix='!', intents=intents)

# Load configuration
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return default_config

# Save configuration
def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

# Global config
config = load_config()

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')
    print(f'Add the bot to your server using the OAuth2 URL from the Discord Developer Portal')
    print(f'Use !settarget <user_id> to set which user to track')

@bot.command()
async def settarget(ctx, user_id: int):
    """Set the target user for this server"""
    guild_id = str(ctx.guild.id)
    config['target_users'][guild_id] = user_id
    save_config(config)
    user = bot.get_user(user_id)
    username = user.name if user else f'User {user_id}'
    await ctx.send(f'Target user set to {username}')

@bot.event
async def on_voice_state_update(member, before, after):
    guild_id = str(member.guild.id)
    # Skip if this guild doesn't have a target user set
    if guild_id not in config['target_users']:
        return
    
    target_user_id = config['target_users'][guild_id]
    # Check if it's our target user
    if member.id == target_user_id:
        # User joined a voice channel
        if before.channel is None and after.channel is not None:
            await join_play_and_leave(after.channel)

async def join_play_and_leave(channel):
    # Join the voice channel
    voice_client = await channel.connect()
    
    # Wait a short moment
    await asyncio.sleep(1)
    
    # Play a random fart sound
    await play_fart_sound(voice_client)
    
    # Wait for the sound to finish (approximately 3 seconds)
    await asyncio.sleep(3)
    
    # Disconnect from the voice channel
    await voice_client.disconnect()

async def play_fart_sound(voice_client):
    # Make sure we have fart sounds
    if not os.path.exists(FART_SOUNDS_DIR) or not os.listdir(FART_SOUNDS_DIR):
        print(f"No fart sounds found in {FART_SOUNDS_DIR}")
        return False
        
    # Play a random fart sound
    fart_file = random.choice(os.listdir(FART_SOUNDS_DIR))
    audio_source = discord.FFmpegPCMAudio(os.path.join(FART_SOUNDS_DIR, fart_file))
    
    if not voice_client.is_playing():
        voice_client.play(audio_source)
        return True
    return False

# Run the bot
if __name__ == "__main__":
    print("Starting Fart Bot...")
    keep_alive()  # Start the web server to keep the bot alive
    bot.run(TOKEN)