#!/bin/env python3.6
import twitter
api = twitter.Api(consumer_key="NMZVVEnIxgspNJYeRqJmxT1MQ", consumer_secret="gy6AmMRPRhqDnbE0ouZoFnlcj3WPbklvWdaOffle1B18N7ZjVr",
                  access_token_key="2645489335-ESQydRomsHsDSM5EOwtzdYVeET8D97bZY8QsDSY", access_token_secret="jrkprNE28SL9IwE8nfPSQgoSWSxk22uyjuAyyyRoI3Cwt")
 
#user = "@doryanmzr"
#statuses = api.GetUserTimeline(
#	screen_name=user, count=30 ,include_rts=False)
#for s in statuses:
#    print (s.text)

status = api.PostUpdate('test50')
print (status.text)
