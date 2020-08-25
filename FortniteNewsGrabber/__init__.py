import aiohttp
import json
from enum import Enum


class news:
    def __init__(self, data):
        try:
            self.trending = data["trending"]
        except KeyError:
            self.trending = None
        try:
            self.noTopImage = data["noTopImage"]
        except KeyError:
            self.noTopImage = None
        try:
            self.gridTitle = data["gridTitle"]
        except KeyError:
            self.gridTitle = None
        try:
            self.image = data["image"]
        except KeyError:
            self.image = None
        try:
            self.contentTypeSticky = data["contentTypeSticky"]
        except KeyError:
            self.contentTypeSticky = None
        try:
            self.author = data["author"]
        except KeyError:
            self.author = None
        try:
            self.enableLightbox = data["enableLightbox"]
        except KeyError:
            self.enableLightbox = None
        try:
            self._type = data["_type"]
        except KeyError:
            self._type = None
        try:
            self.shareImage = data["shareImage"]
        except KeyError:
            self.shareImage = None
        try:
            self.title = data["title"]
        except KeyError:
            self.title = None
        try:
            self.content = data["content"]
        except KeyError:
            self.content = None
        try:
            self.trendingImage = data["trendingImage"]
        except KeyError:
            self.trendingImage = None
        try:
            self.subtitle = data["subtitle"]
        except KeyError:
            self.subtitle = None
        try:
            self.sticky = data["sticky"]
        except KeyError:
            self.sticky = None
        try:
            self.short = data["short"]
        except KeyError:
            self.short = None
        try:
            self.featured = data["featured"]
        except KeyError:
            self.featured = None
        try:
            self.date = data["date"]
        except  KeyError:
            self.date = None
        try:
            self.link = data["link"]
        except KeyError:
            self.link = None
        try:
            self._id = data["_id"]
        except KeyError:
            self._id = None
        try:
            self.pageMapping = data["pageMapping"]
        except KeyError:
            self.pageMapping = None
        try:
            self.slug = data["slug"]
        except KeyError:
            self.slug = None
        try:
            self.urlPattern = data["urlPattern"]
        except KeyError:
            self.urlPattern = None
        try:
            self.locale = data["locale"]
        except KeyError:
            self.locale = None
        try:
            self.noIndex = data["noIndex"]
        except KeyError:
            self.noIndex = None
        try:
            self._script = data["_script"]
        except KeyError:
            self._script = None
        try:
            self.category = data["category"]
        except KeyError:
            self.category = None
        try:
            self.tags = data["tags"]
        except KeyError:
            self.tags = None
        try:
            self._metaTags = data["_metaTags"]
        except KeyError:
            self._metaTags = None
        try:
            self.shareDescription = data["shareDescription"]
        except KeyError:
            self.shareDescription = None
        try:
            self.catLocaleMap = data["catLocaleMap"]
        except KeyError:
            self.catLocaleMap = None
        try:
            self.prevSlug = data["prevSlug"]
        except KeyError:
            self.prevSlug = None
        try:
            self.nextSlug = data["nextSlug"]
        except KeyError:
            self.nextSlug = None
        self.raw = data


class types(Enum):
    gridTitle = "gridTitle"
    author = "author"
    image = "image"
    shareImage = "shareImage"
    shareDescription = "shareDescription"
    title="title"

async def searchForFromList(searchText: str, search: types, data: list):
    stuff = []
    for x in data:
        try:
            if searchText.lower() == x.raw[search.value].lower():
                stuff.append(x)
        except KeyError:
            pass
    return stuff

async def getAllNews():
    async with aiohttp.ClientSession() as session:
        a = await (await session.get("https://www.epicgames.com/fortnite/api/blog/getPosts?category=&postsPerPage=0&offset=0&locale=en-US&rootPageSlug=blog")).json()
    stuff = []
    for x in a["blogList"]:
        stuff.append(news(x))
    return stuff

async def searchFor(searchText: str, search: types):
    async with aiohttp.ClientSession() as session:
        a = await (await session.get("https://www.epicgames.com/fortnite/api/blog/getPosts?category=&postsPerPage=0&offset=0&locale=en-US&rootPageSlug=blog")).json()
    stuff = []
    for x in a["blogList"]:
        try:
            if searchText.lower() == x[search.value].lower():
                stuff.append(news(x))
        except KeyError:
            pass
    return stuff
