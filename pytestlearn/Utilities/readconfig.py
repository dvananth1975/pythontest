from configparser import ConfigParser

# config = ConfigParser()
# config.read("config.ini")
# print(config.get("basic info","browser"))

def readconfig(section,option):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(section,option)

print(readconfig("basic info","browser"))
