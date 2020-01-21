 # TwitterBot - Jude

 # Setup
import time
from storygenerator import storygen
valid1 = 0
valid2 = 0
minute = 60
hour = 60*60
day = hour*24
month = day*30
year = day*365
retry = 0


print(u"Welcome to Jude's Twitter Bot")


 # Inputs & clarifications of elligibility
while valid1 == 0:
    fre = str(input(u"How frequent would you like me to post? (ye/mo/da/ho/mi) "))
    if fre == "ye":
        fre = year
        valid1 = 1
    elif fre == "mo":
        fre = month
        valid1 = 1
    elif fre == "da":
        fre = day
        valid1 = 1
    elif fre == "ho":
        fre = hour
        valid1 = 1
    elif fre == "mi":
        fre = minute
        valid1 = 1
    else:
        input(u"You response wasn't one of the options, try again ")
while valid2 == 0:
    tot = str(input(u"And how many times would you like me to post? "))
    try:
        tot = int(tot)
        valid2 = 1
        if tot < 0:
            valid2 = 0
            input(u"Your input wasn't a positive integer, try again ")
    except:
        input(u"Your input wasn't a positive integer, try again ")


print(u"\nRunning...")


 # Twitter keys
cons_key = "DuUoGgv6cRaNn8ygco5dq28dg"
cons_secret = "kK3SQfydqq2DGAWouPfFyrowqTQJMpCdebv4ZxeJ9YShwtd6k1"
access_token = "1217393920684056576-cjlcMrakasMxoAxdZRez1Q1eLC7OMa"
access_token_secret = "6oVQKg7OeVanIVnkAlYiyY0OR4WFnaAa6zcizYT15CBlw"


 # Install Twitter
try:
    import twitter
    td = True
    print(u"Successfully installed Twitter")
except:
    td = False
    print(u"Failed to install Twitter")

while retry < 3 or tot == 0:
    if td == True:
         # Logging in to Twitter
        try:
            auth = twitter.OAuth( access_token, access_token_secret, cons_key, cons_secret)
            t = twitter.Twitter(auth=auth)
            print(u"Successfully logged into Twitter")
            li = True
        except:
            print("Failed to log into Twitter")
            li = False
            retry = retry + 1
        if li == True:
             # Posting message
            plot = "whore"
            t.statuses.update(status=plot)
            print(u"It worked! Tweeted:", plot)
            if tot > 0:
                print(u"Sleeping for {} seconds".format(fre))
                time.sleep(fre)
                tot = tot - 1
