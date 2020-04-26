from configparser import ConfigParser


def get_clientID():
    cfg = ConfigParser()
    cfg.read(r'C:\Users\Administrator\Desktop\UniqueClientCode.ini')
    return cfg.get('ClientUnique', 'ClientIDID')
