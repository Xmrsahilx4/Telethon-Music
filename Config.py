import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6301715240:AAEKGi8QunVC61CD9jLKmeuVMMD_JqiBRaY")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIEBu2me53VQNjqE9SOfInBUHkkbF26h8EBsegv8sD4YLbWfZEi26Qi3ZzCpL1KvANmi2xUUPoVAX3pk_DYkJp4rgL2qAGHzucB6mRAaPjgN0GsJ3dX8KNl1OCiBwGPQSKvL1Grxn4FfPKhWxY_WDIng_IvNqpKHff9-ye_s2Pkwjs4W1y47Fw6U0bhHnxxeBKkgdKIZiUOu0fbnYiLx3SLOr6sL54qWgPYCtl3O5JgdIMOaojdE-67ycQFTmcmKP89K89AS3YjcR2UEPJ4-d9rTkcyrvzF2Bjn_Il_O1OlrYcTRO7PE-Yr2fmMZDExAqjeGGLNI0qGLDnbZAR3UB9qKEX8=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
