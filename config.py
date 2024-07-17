import os
class Config:     #Placeholder configs
    SECRET_KEY = os.environ.get('SECRETS_KEY') or 'default_secret_key'
    MODS_FOLDER = os.environ.get('MODS_FOLDER') or '/path/to/mods/'
    SERVER_SETTINGS_FILE = os.environ.get('SERVER_SETTINGS_FILE') or '/path/to/server/settings/file'
