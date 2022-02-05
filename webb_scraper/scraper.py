import requests

URL = 'https://en.wikipedia.org/wiki/RuPaul%27s_Drag_Race'

page = requests.get(URL)

print (page.content)

if __name__ == "main":
  pass