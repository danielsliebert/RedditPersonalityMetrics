# Writes out a user's comments to a plain text file for metrics processing
import praw
import sys
import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3

userscrape = sys.argv[1]

output_handle = open(userscrape + ".txt", "w")

# Create reddit instance
r = praw.Reddit(client_id='MGO4o5cR0fs5WQ',
                client_secret='c_VLGjmD_zYmmbohcqlKSO1uq8Y',
                password='W4Qu5cqT6J!',
                user_agent='personality metrics from reddit comments',
                username='personalitymetrics')

user = r.redditor(userscrape)
# Print out all new comments (Max limit = 1000 per API)
for comment in user.comments.new(limit=None):
    output_handle.write(comment.body.encode('utf-8'))

output_handle.close()


personality_insights = PersonalityInsightsV3(
    #version='2016-10-20',
    username='',  # insert your personality insights username here
    password='',  # insert your personality insights password here
    x_watson_learning_opt_out=True
)


with open(join(dirname(__file__), userscrape + '.txt')) as profile_txt:
    profile = personality_insights.profile(
        profile_txt.read(), consumption_preferences=True
    )

with open(userscrape + '_metrics.txt', 'w') as outfile:
    json.dump(profile, outfile)

