#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29435108"))
API_HASH = environ.get("API_HASH", "2d211eb63606dae1bcb413d57391b2de")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "6050965589"))
CREDIT = "𝐌𝐫 & 𝐌𝐫𝐬 𝐁𝐡𝐚𝐫𝐝𝐰𝐚𝐣"
AUTH_USER = os.environ.get('AUTH_USERS', '6050965589').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
