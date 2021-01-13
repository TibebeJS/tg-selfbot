# tg-selfbot
A self-bot with argparse integration and easy scripts management.

## Important Note:
The selfbot creates a folder named "`KEEP_SECRET`" upon operation to keep sensitive data.
It contains your telegram/telethon session which can be used to authenticate as you.

## How to run:
### By building Docker image:
First run the following to build the image:
```
docker build . -t selfbot
```
and then run the following to run it
```
docker run -i --tty --env-file .env -v $(pwd)/KEEP_SECRET:/bot/KEEP_SECRET selfbot
```

Powered by: [Telethon](https://github.com/LonamiWebs/Telethon) and [ArgParse](https://docs.python.org/3/library/argparse.html)