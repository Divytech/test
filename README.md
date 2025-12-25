# File Converter Telegram Bot

A simple Telegram bot to convert files (Image to PDF, Text to PDF) using Pyrogram.

## Features
- **Image to PDF**: Converts JPG/PNG images to PDF.
- **Text to PDF**: Converts `.txt` files to PDF.
- **Easy Deployment**: Ready for local or cloud deployment.

## Local Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd convert/conv2
   ```

2. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Configure Environment:**
   - Rename `.env.sample` to `.env`.
   - Edit `.env` and add your `API_ID`, `API_HASH`, and `BOT_TOKEN`.

4. **Run the bot:**
   ```bash
   python3 bot.py
   ```

## EC2 Deployment Guide

Follow these steps to deploy the bot on an AWS EC2 instance (Ubuntu).

### 1. Launch EC2 Instance
- Go to AWS Console > EC2 > Launch Instance.
- Name: `FileConvertBot`.
- OS Image: **Ubuntu Server 22.04 LTS (HVM)**.
- Instance Type: **t2.micro** (Free tier eligible).
- Key Pair: Create new or select existing (download the `.pem` file).
- Network Settings: Allow SSH traffic from Anywhere (0.0.0.0/0).
- Launch Instance.

### 2. Connect to Instance
Open your terminal (or Putty on Windows) and run:
```bash
chmod 400 your-key.pem
ssh -i "your-key.pem" ubuntu@<your-ec2-public-ip>
```

### 3. Install Python & Tools
Update the system and install necessary packages:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
```

### 4. Setup Project
Clone your repo or upload files (e.g., using SCP or FileZilla). Assuming files are in `~/bot`:
```bash
mkdir bot
cd bot
# Upload your files here...
# Or if you used git:
# git clone <repo> .
```

Install python dependencies:
```bash
pip3 install -r requirements.txt
```

Create your `.env` file:
```bash
nano .env
# Paste your API_ID, API_HASH, BOT_TOKEN
# Ctrl+X, Y, Enter to save
```

### 5. Run as a Service (Systemd)
To keep the bot running 24/7 even after you close SSH, create a systemd service.

```bash
sudo nano /etc/systemd/system/bot.service
```

Paste the following (change paths if needed):
```ini
[Unit]
Description=File Converter Telegram Bot
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/bot
ExecStart=/usr/bin/python3 /home/ubuntu/bot/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Save and exit. Then enable and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable bot
sudo systemctl start bot
```

### 6. Verify Status
Check if the bot is running:
```bash
sudo systemctl status bot
```
If you see `Active: active (running)`, your bot is live!
