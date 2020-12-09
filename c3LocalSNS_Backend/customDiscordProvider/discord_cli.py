from discord import Client
import requests
from logging import getLogger
logger = getLogger('Django')

def checkGuild(token, guildId):
  guilds = getGuilds(token)
  for guild in guilds:
    logger.debug(guild['id'])
    if guild['id'] == guildId:
      return True

  return False

def getGuilds(token):
  res = requests.get(
    # "https://discord.com/api/guilds/656128980805615618",
    "https://discord.com/api/users/@me/guilds",
    headers={ "Authorization": "Bearer " + token}
    )
  return res.json()