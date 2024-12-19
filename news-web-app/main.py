import requests
from send_email import send_email

topic = "tesla"
api_key = "api_key"
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&"\
      "from=2023-12-07&sortBy=publishedAt&"\
      "apiKey=f5231b85fc7e43d2ad4e67a2c404941c&"\
      "language=en"


reqst = requests.get(url)
content = reqst.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's News" +\
                "\n" + body + article["title"] + "\n" \
               + article["description"]  \
               + "\n" + article["url"] + 3 * "\n"

body = body.encode("utf-8")
send_email(message=body)
