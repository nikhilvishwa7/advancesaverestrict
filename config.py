# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20918873"))
API_HASH = getenv("API_HASH", "55def0bf201add8cb672967921f65551")
BOT_TOKEN = getenv("BOT_TOKEN", "7258246322:AAF-akYkXA0ZzQVELrmyprFO2IWG3SONzpc")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7336971189").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://weloxa8533:WKmtuOzgMtTFGCrC@cluster0.jrz7hfn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002395040216")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002190745268"))
