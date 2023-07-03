import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
PORT = environ.get("PORT", "8000")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '21818317'))
API_HASH = environ.get('API_HASH', 'bc6ab154300cc41fe127ca4d658dc75d')
BOT_TOKEN = environ.get('BOT_TOKEN', '5429528025:AAEBJOtfDkRgcYPI5Hjdo8VrnceSl5Bc0bU')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
# Bot images & videos
PICS = (environ.get('PICS', 'https://te.legra.ph/file/c848fa0b53d58a7d94a51.jpg https://te.legra.ph/file/f0baefb59a2b631ce182a.jpg https://te.legra.ph/file/90da02c94b40ea21829ed.jpg https://te.legra.ph/file/47d72397c2ba4f0e8ab3e.jpg https://te.legra.ph/file/1ddc66b365bbd611b480c.jpg https://te.legra.ph/file/0d5888bf952fe07e84f99.jpg https://te.legra.ph/file/b1c86c252ffe132b42bad.jpg https://te.legra.ph/file/88b9edd741cf9784077a9.jpg https://te.legra.ph/file/ebf775de3ee8f3d9a168b.jpg https://te.legra.ph/file/68916c092d1fd000eb205.jpg https://te.legra.ph/file/8bc1730f0ddf298366594.jpg https://te.legra.ph/file/b906f81f0164248054c87.jpg https://te.legra.ph/file/eb1a3fdba60d504571a11.jpg https://te.legra.ph/file/e5912d2a60175c57b296e.jpg https://te.legra.ph/file/8a583c83343a1081edd11.jpg https://te.legra.ph/file/54590b987bf9983c9b5f4.jpg https://te.legra.ph/file/0235d624f506fde506f7c.jpg https://te.legra.ph/file/9ac25e07ea401e9f6b527.jpg https://te.legra.ph/file/7e87bd99301823e11bcd1.jpg https://te.legra.ph/file/46cf137dde3887fc2a5b5.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/0593a3103ba1b9a5855bf.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://te.legra.ph/file/485b93dd1ec801061f091.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/2a888a370f479f4338f7c.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5792675265 5681376068').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'FILES')

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'ipopkorn.io')
SHORTLINK_API = environ.get('SHORTLINK_API', '0cf6028fba3f0a9c4ac283f7807039dac1eb50d3')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'True')), True)
MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001847958537))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Mx_Support_Bot')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", '📂 <em>File Name</em>: <code>{file_name}</code> \n\n🖇 <em>File Size</em>: <code>{file_size}</code> \n\n</i>🍿 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮</i> [@iPopkarnBots](https://t.me/iPopkarnBots)')
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", '')
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", '🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10  \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} \n\n🎊 𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝑩𝒚 [𝗶𝗣𝗼𝗽𝗸𝗮𝗿𝗻𝗕𝗼𝘁𝘀](t.me/iPopkarnBots)')
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

HOW_DWLD_LINK = environ.get('HOW_DWLD_LINK', 'https://t.me/iPopkarnTutorial')

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
