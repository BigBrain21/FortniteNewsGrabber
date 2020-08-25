# FortniteNewsGrabber

An async python library for grabbing the news from https://www.epicgames.com/fortnite/en-US/news.<br />
Usage:<br />
-
```py
import FortniteNewsGrabber
import asyncio

async def main():
    a = await FortniteNewsGrabber.getAllNews()
    print(a[0].image)


asyncio.get_event_loop().run_until_complete(main())```
This will print the image of the front news element
