# Writes out a user's comments to a plain text file for metrics processing
import praw
import sys

userscrape = sys.argv[1]

output_handle = open(userscrape + ".txt", "w")

# Create reddit instance
r = praw.Reddit(client_id='CLIENTID',
                client_secret='SECRET',
                password='PASSWORD',
                user_agent='personality metrics from reddit comments',
                username='OBFUSCATETHIS')

user = r.redditor(userscrape)
# Print out all new comments (Max limit = 1000 per API)
for comment in user.comments.new(limit=None):
    output_handle.write(comment.body.encode('utf-8'))

output_handle.close()
