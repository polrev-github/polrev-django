import json

from django.conf import settings

#import redis
from django_redis import get_redis_connection

import praw

from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

@shared_task
def hot_task():
    logger.info("The reddit:hot task just ran.")

    reddit = praw.Reddit(
        client_id=settings.PRAW_CLIENT_ID,
        client_secret=settings.PRAW_CLIENT_SECRET,
        username=settings.PRAW_USERNAME,
        password=settings.PRAW_PASSWORD,
        user_agent="XYZ",
    )

    subreddit = reddit.subreddit("Political_Revolution")

    hot = []

    for id in subreddit.hot(limit=20):
        submission = reddit.submission(id=id)
        title = submission.title
        permalink = submission.permalink
        hot.append({
            'title': title,
            'permalink': permalink,
        })

    client = get_redis_connection("default")

    client.set('reddit:hot', json.dumps(hot))