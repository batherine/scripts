from asyncio.windows_events import NULL
from typing import Collection
from notion.client import NotionClient


token = "5775a55d3381012f6c2ade02a159c2746b56301be65d96ddf11b89a2add041d0cd388c78db52732bb8e38d89652ae5d780b54587369b3519a814d0eeebd4fa8dbade5f1ea94bc65adbe265dab757"

client = NotionClient(token_v2 = token)

page_url = ""
page = client.get_block(page_url)
print(page.title)
print(page.children)
list_id = ""
collection_view = client.get_collection_view(list_id)
print(collection_view)
collection = collection_view.collection
for item in page.children:
    print(item)
    if item.title != NULL and item.title == 'To-Do Tracker':
        print(item.collection)



