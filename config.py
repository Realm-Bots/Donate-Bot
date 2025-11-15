# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# --- REQUIRED ---
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# ----------------

# --- TEXTS ---
# This is where you can now use Markdown formatting freely.
# For example: **bold**, *italic*, `code`, [link](https://telegram.org)

# Your bot's owner user ID (as an integer), for the "master" link.
# Get it from @userinfobot
OWNER_ID = 123456789 

START_TEXT = """
You can support the bot development by donating through the link below.
Donations will be used for bot development and also server rental costs for this bot.
_*Thank you very much for your donation*_ 🙏

**Bank Jago:** `wulan17`
"""

CRYPTO_TEXT = f"""
**Main Crypto Address:** ❞
(Same address for same network)
**BTC:** `1DxGWYXeSMqqpouJeHEqHsLuxGv1ydkCoe`
**TRX (TRC20):** `TSZUxHqvNhQMUkUPB92vzCVcVANxZGs3tD`
**TON:** `EQBRYjGMy_f7wQSy518W9mmBTjRtAvT4VBJ3pS51jwDkn8pP`

**Backup Crypto Address:** ❞
(Same address for same network)
**BTC:** `1PuNnnBcW7eYmx4F9jafNd4bRsjvkQueNd`

If you need another crypto address, please [contact my master here](tg://user?id={OWNER_ID}).
"""

STARS_TEXT = "**How many stars do you want to donate?**"

# --- BUTTONS (No changes here) ---

MAIN_MENU_BUTTONS = {
    "Crypto": "callback:crypto",
    "Dana": "url:https://link.dana.id/qr/yourcode",
    "Trakteer": "url:https://trakteer.id/yourusername",
    "Telegram Stars": "callback:stars",
    "Github Sponsors": "url:https://github.com/sponsors/yourusername",
    "Paypal": "url:https://paypal.me/yourusername"
}

STARS_TIERS = {
    "5": "☕ Coffee",
    "10": "✨ Sparkle",
    "25": "🥉 Bronze",
    "50": "🥈 Silver",
    "100": "🥇 Gold",
    "200": "💎 Diamond",
    "500": "🚀 Rocket Fuel",
    "1000": "👑 Legendary"
}
