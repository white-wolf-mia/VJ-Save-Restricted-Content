import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7189956610:AAFoqc8ziAAXLT27o7aFSvaNZ6oZpZvDE4g")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21857983"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e469e84c943ce3b8b056eb6a296f2c67")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://dhimanrajat:Y8IAGI0lVrMhjvkU@cluster0.mytkgu6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
