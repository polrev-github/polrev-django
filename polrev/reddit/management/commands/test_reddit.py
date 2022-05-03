from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'test reddit/praw'

    def handle(self, *args, **options):

        reddit = praw.Reddit(
            client_id="SI8pN3DSbt0zor",
            client_secret="xaxkj7HNh8kwg8e5t4m6KvSrbTI",
            password="1guiwevlfo00esyy",
            user_agent="testscript by u/fakebot3",
            username="fakebot3",
        )
