from django.conf import settings
import redis
from enum import Enum
from postManager.models import Post, Favorite

import logging

logger = logging.getLogger('development')

logger.debug('connect to redis')

REDIS = None

def get_redis():
    global REDIS
    if REDIS is None:
        REDIS = redis.Redis(host=settings.NOTIFICATION['REDIS']['REDIS_HOST'], port=settings.NOTIFICATION['REDIS']['REDIS_PORT'], db=0)
    return REDIS
    


# r = redis.StrictRedis(host=settings.NOTIFICATION.REDIS.REDIS_HOST, port=settings.NOTIFICATION.REDIS.REDIS_PORT, db=0)

class NotificationChannelGroup(Enum):
    POST = 'POST'
    FAVORITE = 'FAVORITE'

def send_notification(notificationChannelGroup: NotificationChannelGroup, data):
    r = get_redis()
    channel = notificationChannelGroup.name
    r.publish(channel, 'data')
