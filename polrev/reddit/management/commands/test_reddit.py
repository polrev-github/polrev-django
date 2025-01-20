import json

from django.core.management.base import BaseCommand
from django.conf import settings

from django_redis import get_redis_connection

import praw


class Command(BaseCommand):
    help = "test reddit/praw"

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
            permalink = submission.permalink
            print(permalink)
            # print(submission.url)
            # print(submission.selftext)

            hot.append(
                {
                    "title": title,
                    "permalink": permalink,
                }
            )

        client = get_redis_connection("default")

        client.set("reddit:hot", json.dumps(hot))
