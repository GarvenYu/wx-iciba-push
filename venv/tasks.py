#! usr/bin/env python3
# -*-coding:utf-8-*-

from celery import Celery
import json
import redis

celery_instance = Celery('tasks')
celery_instance.config_from_object('celeryconfig')
redis_client = redis.StrictRedis(db=1)


@celery_instance.task
def put(msg: dict):
    # del old data
    redis_client.flushdb()
    # put new data
    content = msg.get('content', None)
    pic_url = msg.get('picture', None)
    return json.dumps({'content': content, 'pic': pic_url})
