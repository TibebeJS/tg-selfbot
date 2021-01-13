# tg-selfbot
A self-bot with argparse integration and easy scripts management.

## Important Note:
The selfbot creates a folder named "`KEEP_SECRET`" upon operation to keep sensitive data.
It contains your telegram/telethon session which can be used to authenticate as you.

## How to run:
### Step 1:
Goto https://my.telegram.org and create application.\
Create a file called `.env` in the format
```
API_ID=<REPLACE_WITH_YOUR_APP_ID>
API_HASH=<REPLACE_WITH_YOUR_APP_HASH>
```
and replace those values for your app.

### Step 2:
#### Pull an already built Image from Docker Hub:
```
docker pull tibebesjs/tg-selfbot
```
and then:
```
docker run -i --tty --env-file .env -v $(pwd)/KEEP_SECRET:/bot/KEEP_SECRET tg-selfbot
```

#### Alternatively, you can build a Docker image yourself:
First run the following to build the image:
```
git clone git@github.com:TibebeJS/tg-selfbot.git
```
```
cd tg-selfbot
```
After that, build the image:
```
docker build . -t selfbot
```
and then run the following to run it
```
docker run -i --tty --env-file .env -v $(pwd)/KEEP_SECRET:/bot/KEEP_SECRET selfbot
```

Powered by: [Telethon](https://github.com/LonamiWebs/Telethon) and [ArgParse](https://docs.python.org/3/library/argparse.html)
