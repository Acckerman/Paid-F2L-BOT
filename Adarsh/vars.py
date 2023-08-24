# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '24865057'))
    API_HASH = str(getenv('API_HASH', 'a45372ac22649e134c7871ab3125bfb1'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6415159418:AAFhfA3au-E3lIEo6JeDW2Qi2GRJpDYcGxs'))
    SESSION_NAME = str(getenv('SESSION_NAME', ''))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001788767433'))
    PORT = int(getenv('PORT', 8080))
    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "BOTTOM")
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5557955876").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    SHORTENER_API = str(getenv('SHORTENER_API', '4fbe384f585aa6c0df736bd9a859bfc3b9216fee'))
    SHORTENER_WEBSITE = str(getenv('SHORTENER_WEBSITE', 'tnlink.in'))
    FDQN = str(getenv('FDQN', ''))

    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME', 'filetolinkda'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://F2lbot:acckerman@cluster0.mjuvpp0.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', "@tamilanmovieschat"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001788767433")).split())) 
