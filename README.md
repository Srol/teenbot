# TeenBot

This repository uses [cobe](https://github.com/pteichman/cobe) and [CanvasText](https://github.com/pmphp/CanvasText). Thank you to the devs who made them available.

This repository was used to make the bot in this [article](http://fusion.net/story/193725/i-was-a-teenage-chatbot/) on Fusion.net, as well as a [how-to guide here](http://fusion.net/story/195480/chatbot-teenage-years-how-to/). 
If you provide it with the material, it will generate a bot to respond to you with markov chains using that material. 
The repository as-is is optimized to live on a Heroku server, with javascript delivering results to the browser window. 

In order to get it to work, you will need to replace the contents of total.txt with your own text corpus, then use cobe to generate a new cobe.brain. 
If you don't do that, it will keep using my crappy deo text.

I hope it's helpful. 