#Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).
An access token is an object that describes the security context of a process or thread. 
The information in a token includes the identity and privileges of  the user account associated with the process or thread. ...
The security identifier (SID) for the user's account. SIDs for the groups of which the user is a member.


consumer_key29='vwdqsgjcvjabsncvvnmsxvs99'
consumer_secrete29='xshfxhg99lhfsbsvffgswgf1hdsghfgkhufteeryyi99'
access_token29='dsnxjwsdghjknbvffrddhjjjkjgdddghjjfg1'
access_token_secret29='bswhvwhvdwhsvhjwdsc33'





#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.
	C:\Users\Bhanu>nslookup google.com
DNS request timed out.
    timeout was 2 seconds.
Server:  UnKnown
Address:  2402:8100:2033:5fb:2583:

DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
*** Request to UnKnown timed-out

C:\Users\Bhanu>nslookup facebook.c
DNS request timed out.
    timeout was 2 seconds.
Server:  UnKnown
Address:  2402:8100:2033:5fb:2583:

DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
*** Request to UnKnown timed-out

C:\Users\Bhanu>nslookup youtube.co
DNS request timed out.
    timeout was 2 seconds.
Server:  UnKnown
Address:  2402:8100:2033:5fb:2583:

DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
*** Request to UnKnown timed-out




#Q.3- Using Tweepy library try to extract tweets from Twitter. 

import tweepy


consumer_key29=''
consumer_secrete29=''
access_token29=''
access_token_secret29=''
auth=tweepy.OAuthHandler(consumer_key29,consumer_secrete29)
auth.set_access_token(access_token29,access_token_secret29)
api=tweepy.API(auth)
tweets=api.search("#notwithoutmydog",lang="en",count="5",tweet_mode="extended")

#print(tweets)


for tweet in tweets:
    print("-----------------")
    print(tweet.full_text)
    print("-----------------------")

	
	
	
	
	
	
	
	
	
#.4- What is a difference between library and API . Figure it out with examples.
	LIBRARY
	A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects. (Various specialized services in our case)
     Library:

is Reusable set of code or compilation of set of things which you may need in order to  ease your process of development, ex: JQuery library, is a library of prewritten, cross-browser Javascript animations and functions which you will need while making a website.
	
	
	
	API(application programming interface)
An API is an interface for other programs to interact with your program or library  without having direct access. ( giving specifications for our need to various vendors in our case)

API (Application Programming Interface):

It is interface with which you can access any Application's features, without hosting it on your server, ex: with Google Map APIs you can show maps for different places without writing/hosting the whole code on your server, and just use it, usually this data transfer is in form of JSON i.e JavaScript Object Notation.

SDK (Software Development Kit):

example= date today =new date()