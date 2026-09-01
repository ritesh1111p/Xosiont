"""
config.py
All configuration and credits for the Telegram Hosting Bot.
No .env files, no os.getenv() — everything lives here.
Edit the values below before running the bot.
"""

# ─── Core Bot Settings ────────────────────────────────────────────────
# ⚠️ Paste your FULL token from @BotFather here. It looks like:
#     123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# The old value was only the numeric bot-id half — not a usable token.
BOT_TOKEN = "8321984658:AAHS2K8zdlUxrb_rhy7w-gmH-rDWICfKoY0"

OWNER_ID = 5924662015

ADMIN_IDS = [
    5924662015
]

# ─── Version ───────────────────────────────────────────────────────────
VERSION = "2.0"

# ─── Credits ───────────────────────────────────────────────────────────
CREDIT_OWNER = "@mooN_X_2006"

CREDIT_TELEGRAM_CHANNEL = "https://t.me/chandxxd"

CREDIT_YOUTUBE_CHANNEL = "soon.."

CREDIT_HOME_VIDEO_URL = "https://files.catbox.moe/5zed53.mp4"

CREDIT_FOOTER = f"\n\n👑 Bot by {CREDIT_OWNER}"

# ─── Paths ─────────────────────────────────────────────────────────────
import os as _os

BASE_DIR = _os.path.dirname(_os.path.abspath(__file__))

UPLOADS_DIR = _os.path.join(BASE_DIR, "uploads")
CONTAINERS_DIR = _os.path.join(BASE_DIR, "containers")
BACKUPS_DIR = _os.path.join(BASE_DIR, "backups")
LOGS_DIR = _os.path.join(BASE_DIR, "logs")
TEMP_DIR = _os.path.join(BASE_DIR, "temp")
DATABASE_DIR = _os.path.join(BASE_DIR, "database")

USERS_DB = _os.path.join(DATABASE_DIR, "users.db")
BOTS_DB = _os.path.join(DATABASE_DIR, "bots.db")
SETTINGS_DB = _os.path.join(DATABASE_DIR, "settings.db")

# ─── Deployment / Runtime Settings ─────────────────────────────────────
# Toggle whether the bot uses Docker for isolation. If Docker isn't
# available on the host, the bot falls back to plain subprocess hosting.
USE_DOCKER = True

DOCKER_IMAGE_PYTHON = "python:3.11-slim"
DOCKER_IMAGE_NODE = "node:22-slim"

# Per-bot resource limits (only enforced when USE_DOCKER = True)
CONTAINER_CPU_LIMIT = 4.0        # CPU cores
CONTAINER_MEMORY_LIMIT = "8g"    # RAM per bot

# Max upload size in megabytes
MAX_UPLOAD_MB = 50

# Max number of bots a single (non-admin) user may host at once
MAX_BOTS_PER_USER = 10

# Max number of bots a premium (non-admin) user may host at once
MAX_BOTS_PER_PREMIUM_USER = 1500

# Number of log lines shown by default in the Logs menu
LOG_TAIL_LINES = 100

# Auto-restart a crashed bot up to N times before giving up
MAX_AUTO_RESTARTS = 10
