#!/bin/env python3.6
import twitter
api = twitter.Api(consumer_key="CONSUMER_KET", consumer_secret="CONSUMER_SECRET",
                  access_token_key="ACCESS_TOKEN", access_token_secret="ACESS_SECRET")

#GET status info
user = "@USERNAME"
statuses = api.GetUserTimeline(
	screen_name=user, count=30 ,include_rts=False)
for s in statuses:
    print (s.text)

#POST "test50" on twitter"
status = api.PostUpdate('test50')
print (status.text)
