import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

#import redis
from django_redis import get_redis_connection

import praw
from praw.models import MoreComments

class Command(BaseCommand):
    help = 'test reddit/praw'

    def handle(self, *args, **options):

        reddit = praw.Reddit(
            client_id=settings.PRAW_CLIENT_ID,
            client_secret=settings.PRAW_CLIENT_SECRET,
            username=settings.PRAW_USERNAME,
            password=settings.PRAW_PASSWORD,
            user_agent="XYZ",
        )

        print(reddit.user.me())

        subreddit = reddit.subreddit("Political_Revolution")

        hot = []

        for id in subreddit.hot(limit=20):
            print(id)
            submission = reddit.submission(id=id)
            title = submission.title
            print(title)
            '''
            for top_level_comment in submission.comments:
                if isinstance(top_level_comment, MoreComments):
                    continue
                print(top_level_comment.body)
            '''
            permalink = submission.permalink
            print(permalink)
            #print(submission.url)
            #print(submission.selftext)

            hot.append({
                'title': title,
                'permalink': permalink,
            })

        #client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
        client = get_redis_connection("default")

        client.set('reddit:hot', json.dumps(hot))