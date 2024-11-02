import urllib
from urllib import request
import ssl
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context
url=input("Enter page")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, "html.parser")
soup_anchor=soup.find_all("a")
href=list()
for i in soup_anchor:
    link = i.get("href")
    if link and link.startswith("http"):  # Only add valid links
            href.append(link)
visited=set(href)
x=0
while len(href) < 100 and x < len(href):
    try:
        url=href[x]
        x=x+1
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        soup_anchor = soup.find_all("a")
        for link in soup_anchor:
            link=link.get("href")
            if link and link.startswith("http") and link not in visited:
                href.append(link)
                visited.add(link)
                if len(href) >= 100:
                    break
    except Exception as e:
        print(f"Failed to open {url}: {e}")
print(href)
print(len(href))





