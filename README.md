# Discord Fart Bot

A fun Discord bot that automatically joins voice channels when a specific user does, plays a fart sound, and leaves.

## Features

- Joins voice channels automatically when a target user does
- Plays a random fart sound
- Automatically leaves after playing the sound
- Easy configuration with commands
- Support for multiple servers

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- FFmpeg installed on your system (for audio processing)
- A Discord bot token

### Installation

1. Clone this repository
   ```
   git clone https://github.com/kjigian/discord-fart-bot.git
   cd discord-fart-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the bot:
   - Set your bot token as an environment variable:
     ```
     # On Windows
     set TOKEN=your_bot_token_here
     
     # On macOS/Linux
     export TOKEN=your_bot_token_here
     ```
   - Or update the `TOKEN` variable in `fart_bot.py`

4. Add fart sounds:
   - Place MP3 fart sound files in the `fart_sounds` directory

5. Run the bot:
   ```
   python fart_bot.py
   ```

## Usage

- `!settarget <user_id>` - Set which user the bot should track

## Finding User IDs

To find a Discord user's ID:
1. Enable Developer Mode in Discord (User Settings > Advanced > Developer Mode)
2. Right-click on a user and select "Copy ID"

## 24/7 Hosting Options

### Option 1: Replit (Free)

1. Fork this repository to your GitHub account
2. Create a new Replit project using your GitHub repository
3. Add your bot token as an environment variable named `TOKEN`
4. Run the bot
5. Set up UptimeRobot to ping your Replit URL every 5 minutes

### Option 2: Railway (Free Tier)

1. Fork this repository to your GitHub account
2. Create a new Railway project using your GitHub repository
3. Add your bot token as an environment variable named `TOKEN`
4. Railway will automatically deploy your bot

### Option 3: Render (Free Tier)

1. Fork this repository to your GitHub account
2. Create a new Render Web Service using your GitHub repository
3. Set the Start Command to `python fart_bot.py`
4. Add your bot token as an environment variable named `TOKEN`

## Troubleshooting

- If you get audio-related errors, make sure FFmpeg is installed correctly
- If the bot doesn't respond to commands, check that you enabled the Message Content Intent
- If no sounds play, make sure you have MP3 files in the `fart_sounds` directory