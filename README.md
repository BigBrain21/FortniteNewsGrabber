# FortniteNewsGrabber

An async python library for grabbing the news from https://www.epicgames.com/fortnite/en-US/news.<br />
Basic Usage:<br />
-
```py
import FortniteNewsGrabber
import asyncio

async def main():
    a = await FortniteNewsGrabber.getAllNews()
    print(a[0].image)


asyncio.run(main())
```
This will print the image of the first news element.
