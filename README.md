# aternos_alert
sends a discord dm when a specified aternos server starts up

# Installation
1. Using the Discord dev portal, create a bot and install the app to your personal discord account. Be sure to take note of the bot token because you definitely need that. 
2. Put the bot token and your user ID into the provided bot.py. Just add them to the variables at the top
3. Edit the url variable on line 14 so the last bit is your minecraft server and port, instead of example.aternos.com:port
4. Turn on your aternos server and scan it using https://mcstatus.io/status be sure to include your port number because aternos does not use the default port
5. Once it is visible on mcstatus, copy the motd entry, it should look something like this "Welcome to the server of yourname!", if it says something like "This server is offline" continue to refresh the page and verify that your server is indeed on.
6. Now that you have the motd copied, paste it in the variable on line 24. Please include the quotes on any variables that have them in the examples.
7. There you go, now just run ```pip install requests``` and ```pip install discord``` and run bot.py it will notify you within the minute the aternos server is online, with a 1hr cooldown after a successfull online message
