import json
import os
import uuid
from datetime import datetime, timedelta
from bot.config.config import DATA_FILE, VPN_DOMAIN, VLESS_PORT


def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)


def generate_vless_link(user_id: int):
    fake_uuid = str(uuid.uuid4())
    return f"vless://{fake_uuid}@{VPN_DOMAIN}:{VLESS_PORT}?type=tcp&security=reality#user_{user_id}"


def create_subscription(days: int = 30):
    return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")