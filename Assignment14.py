# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:29:14 2016

@author: user
"""

from twython import Twython
import json
import datetime 
import numpy

##codes to access twitter API. 
APP_KEY =  "CLqhxbNmYbSYB0CG2vCx4Lnlc"
APP_SECRET = "Dae8Zh2d8jMRoqVfNkRyCC3ZnvDuMQRyG30i0EN8eJ2IeV0rnL"
OAUTH_TOKEN =  "4832128833-oYdNVhcCVJIDWScAvBe1b7Ev2kf1GxYR9YrXLGR"
OAUTH_TOKEN_SECRET =  "YvlZUam2a7PQizYXhnzZvq3qRtJNIN4EIPrM7STsPnA4N"

##initiating Twython object 
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

##TODO:  This should work as an alternative but it doesn't. Need to find out why
#twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
#ACCESS_TOKEN = twitter.obtain_access_token()
#print ACCESS_TOKEN
#twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

food_list = ["restaurante","comida","pizza","mcdonalds","burger king","subway"]
total_list=[]
#parsing out 
for food in food_list:
    print food

    search_results = twitter.search(q=food,geocode="-23.551300,-46.651638,30km", count=100)
    print len(search_results["statuses"])
    
    for tweet in search_results["statuses"]:
        
        coordinates = tweet['coordinates']    
        if coordinates != None:
            tweetid = tweet['id']
            coords = coordinates['coordinates']
            coords_x = coords[0]
            coords_y = coords[1]
            tweet_list = [food,tweetid,coords_x,coords_y]
            total_list.append(tweet_list)
            
# Write to file
locationFile = open('/home/user/Projects/Assignment14/location_list.csv','w')
for tweet in total_list:
    locationFile.write(str(tweet[0]) + "," + str(tweet[1]) + "," + str(tweet[2]) + "," + str(tweet[3]) + "\n")
locationFile.close()

