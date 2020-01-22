 # TwitterBot - Judev1

 # Setup
import time
import sys
retry = 0
validate = 0


print(u"Welcome to my Twitter Bot!")
print(u"Running...")


 # Message
 # Posting the same message directly after each other will not work
 # Default "Hello World"
message = "Hello World"


 # Twitter keys
cons_key = ""
cons_secret = ""
access_token = ""
access_token_secret = ""


 # Runs - how many times do you want the program to repeat
 # Default 1 run
runs = 1


 # Frequency - how often do you want this program to run
 # minute = 60 seconds
 # hour = 3600 seconds
 # day = 86400 seconds
 # month = 2592000 seconds
 # Any larger than a month and the program will not work
 # Default 21600 seconds
frequency = 21600


 # Install Twitter
try:
    import twitter
    dwnld = True
    print(u"Successfully installed Twitter")
except:
    dwnld = False
    print(u"Failed to install Twitter")


 # Setups the Twitter authenification
auth = twitter.OAuth( access_token, access_token_secret, cons_key, cons_secret)
t = twitter.Twitter(auth=auth)


 # Checks that the frequency is a positive integer
try:
    frequency = int(frequency)
    if frequency < 0:
        print(u"The frequency wasn't a positive integer")
        print("Killed program")
        sys.exit()
except:
    print(u"Your frequency wasn't a positive integer")
    print("Killed program")
    sys.exit()


totalruns = runs
totaltime = (frequency*runs) - frequency
if dwnld == True:
    while retry > 3 or runs > 0:
        success = False
        # Tweeting
        try:
            t.statuses.update(status=message)
             # Add extensions here
            success = True
        except:
            print(u"Unable to tweet")
            if retry < 3:
                retry = retry + 1
                print(u"Attempting to retry")
                time.sleep(2)
            else:
                print("Killed program")
                sys.exit()
        if success == True:
            print(u"Successfully tweeted")
            print(u"Tweeted:", message)
            runs = runs - 1
            print(u"Next tweet in {} seconds".format(frequency))
            time.sleep(frequency)
print("Program Finished! Posted {} times, elapsed time {} seconds".format(totalruns, totaltime))
