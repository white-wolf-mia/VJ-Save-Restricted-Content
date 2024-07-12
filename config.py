import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7412819789:AAE0m4PxPpZ9Ap7TKRXaxl6kYdd0IJo4G-c")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21775862"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3cf8696da93ae9df8bf71ab84d64a1be")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://dhimanrajat:Y8IAGI0lVrMhjvkU@cluster0.mytkgu6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
