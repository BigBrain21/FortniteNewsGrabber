# FortniteNewsGrabber

An async python library for grabbing the news from [this site](https://www.epicgames.com/fortnite/en-US/news).<br />

Installation<br />
-
```py
pip install FortniteNewsGrabber
```

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
This will print a url to the image of the first news element:
```
https://cdn2.unrealengine.com/13br-megadrop-blogthumb-576x576-730037014.jpg
```
