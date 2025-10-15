import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME")
VIDEO_TUTORIAL_LINK = os.getenv("VIDEO_TUTORIAL_LINK", "https://t.me/your_video_tutorial")
VPN_DOMAIN = os.getenv("VPN_DOMAIN", "vpn.example.com")
VLESS_PORT = int(os.getenv("VLESS_PORT", 443))
DATA_FILE = os.getenv("DATA_FILE", "users.json")