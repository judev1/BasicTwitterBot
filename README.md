# BasicTwitterBot
#### Basic Twitter Bot: The bare essentials to creating a Twitter bot
Although this program has actually added additional programming to prevent crashing, it should be really easy to use. Downloading this will allow you to connect your program to this code and then tweet it at specified regular intervals. Additional features below (to be added), will allow you to extend your bot and do things including retweet posts from random/certain people, liking posts from random/certain people and much, much more!



## Contents
 - [Setting up your Twitter bot](https://github.com/judev1/BasicTwitterBot/blob/master/README.md#setting-up-your-twitter-bot)

 - [Going Further](https://github.com/judev1/BasicTwitterBot/blob/master/README.md#going-further)

 - [Extensions for your Twitter bot](https://github.com/judev1/BasicTwitterBot/blob/master/README.md#extensions-for-your-twitter-bot)

 - [Linking your Program](https://github.com/judev1/BasicTwitterBot/blob/master/README.md#linking-your-program)



## Setting up your Twitter bot
#### Step 1
Create a [Twitter Account](https://twitter.com/i/flow/signup) unless you already have one you want to use

IMG

#### Step 2
Login to the [Twitter Developers Account](https://developer.twitter.com/) page using your twitter credentials

#### Step 3
Apply for a [Twitter Developers Account](https://developer.twitter.com/)

IMG

#### Step 4
Once you have filled out the questions and gained your developers account, create an application

IMG

Now you've created it, keep in mind the keys

IMG

#### Step 5
Now download BasicTwitterBot if you haven't already

IMG

Fill in the keys to connect your Twitter account with your enviroment, make sure to fill in 'runs' and 'frequency' as well

IMG

#### Step 6
Personalise your message, Twitter will not allow the same message to be tweeted within a certain time period, so it's best to link it to a program that will post a spesified random message, for more infomation go to [Linking Your Program](https://github.com/judev1/BasicTwitterBot/blob/master/README.md#linking-your-program)

IMG

#### Step 7
Now you should be ready to go! Test to make sure everything is running smoothly and if you have and questions, feel free to ask

IMG



## Going Further
#### Techniquely this bot can be simplified even more, if you really want, although it isn't recommended:
```
import twitter

 # Keys - fill these out with your info
access_token = ""
access_token_secret = ""
cons_key = ""
cons_secret = ""

auth = twitter.OAuth( access_token, access_token_secret, cons_key, cons_secret)
t = twitter.Twitter(auth=auth)
```
And although this essentially is all you need, all that program will do is connect you to your twitter [developers page](https://developer.twitter.com) using your keys



## Extensions for your Twitter Bot
Either using the BasicTwitterBot program or the stripped program above, be sure to add these extensions

#### You could make it tweet something:
```
message = "Hello World"
t.statuses.update(status=message)
```
Where 'message' is what you want it to tweet (this is the default feature that BasicTwitterBot already comes with)

#### You could make it re-tweet something:
(to be added)

#### You could make it reply to a comment:
(to be added)

#### You could make it message someone:
(to be added)

#### You could make it like something:
(to be added)



## Linking your Program
If ou have a program which has an output which you want to tweet, then follow these steps to link it to your BasicTwitterBot program

#### Step 1
Make sure the program which you want to use is stored in the same folder as BasicTwitterBot, for this example the name of my program will be called NumOfDay.py, this is the raw code for it
```
import random

num = random.randint(2,1000)

num = num/2
num = num*random.randint(1,10)

output = "Your number of the day is {}! Lucky you!".format(num)
```

#### Step 2
Now we are going to put your program into a class and define it to return the desired output
```
import random

class numofday:
	def num(self):
		num = random.randint(2,1000)

		num = num/2
		num = num*random.randint(1,10)

		output = "Your number of the day is {}! Lucky you!".format(num)

		return output
```

#### Step 3
Next we need to link your program to BasicTwitterBot, so open basic twitter bot and add
```
from NumOfDay import numofday
```
Where 'NumOfDay' is the file name and 'numofday' is the class name

#### Step 4
Finally we set the message to our desired output
```
message = numofday.num()
```
Where 'numofday' is the class name and 'num' is the definition, and there you go!
