# BasicTwitterBot
### Basic Twitter Bot: The bare essentials to creating a Twitter bot
Although this program has actually added additional programming to prevent crashing, it should be really easy to use. Downloading this will allow you to connect your program to this code and then tweet it at specified regular intervals. Additional features below (to be added), will allow you to extend your bot and do things like retweet posts from random/certain people, like posts from random/certain people and lots more!


## Going Further:
### Techniquely this bot can be simplified even more, if you really want, although it isn't recomended:
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


### You could make it tweet something:
```
t.statuses.update(status=message)
```
Where 'message' is what you want it to tweet

### You could make it re-tweet something:

### You could make it reply to a comment:

### You could make it message someone:

### You could make it like something:

