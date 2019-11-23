from urllib import request,parse
from urllib import error
from bs4 import BeautifulSoup


f = open("kosakana_fan_blog_url.txt", "r")
wf = open("kosakana_fan_blog_text.txt", "w")

lines = f.readlines()

for line in lines:
    print(line)
    try:
        blog_html = request.urlopen(line)
        blog_soup = BeautifulSoup(blog_html, "html.parser")
        sleep_check = blog_soup.select("div.sleeping-ad")
        if sleep_check == []:
            blog_text = blog_soup.select("div.entry-inner > div.entry-content")[0].text
        else:
            blog_text = blog_soup.select("div.entry-inner > div.entry-content")[1].text
        print(blog_text)
        wf.write(blog_text)
    except error.HTTPError:
        continue
wf.close()
f.close()