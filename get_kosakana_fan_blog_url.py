from bs4 import BeautifulSoup
from urllib import request, parse
from selenium import webdriver
import time


file = "kosakana_fan_blog_url.txt"

f = open(file, "w")

url_list = []

for i in range(1, 30):
    hatena_search_url = f"https://www.hatena.ne.jp/o/search/top#gsc.tab=0&gsc.q=%E5%B0%8F%E5%9D%82%E8%8F%9C%E7%B7%92%20-site%3Ahttp%3A%2F%2Fd.hatena.ne.jp%20-site%3Ahttp%3A%2F%2Fb.hatena.ne.jp%20-site%3Ahttp%3A%2F%2Fa.hatena.ne.jp&gsc.page={i}"
    options = webdriver.ChromeOptions()
    options.add_argument("")
    driver = webdriver.Chrome(executable_path="", options=options)
    driver.get(hatena_search_url)
    time.sleep(5)
    hatena_search_html = driver.page_source
    hatena_search_soup = BeautifulSoup(hatena_search_html, "html.parser")
    kosakana_fun_blog_url_list = hatena_search_soup.select("div.gsc-webResult.gsc-result > div.gs-webResult.gs-result > div.gsc-thumbnail-inside > div.gs-title > a.gs-title")
    for kosakana_fun_blog_url_info in kosakana_fun_blog_url_list:
        kosakana_fun_blog_url = kosakana_fun_blog_url_info.get("data-ctorig")
        if kosakana_fun_blog_url.find("archive/category") != -1:
            new_kosakana_fun_blog_html = request.urlopen(kosakana_fun_blog_url)
            new_kosakana_fun_blog_soup = BeautifulSoup(new_kosakana_fun_blog_html, "html.parser")
            new_kosakana_fun_blog_list = new_kosakana_fun_blog_soup.select("div.archive-entries > section.archive-entry.autopagerize_page_element > div.archive-entry-header > h1.entry-title > a")
            for new_kosakana_fun_blog_info in new_kosakana_fun_blog_list:
                new_kosakana_fun_blog_url = new_kosakana_fun_blog_info.get("href")
                if new_kosakana_fun_blog_url not in url_list:
                    print(new_kosakana_fun_blog_url)
                    f.write(new_kosakana_fun_blog_url)
                    f.write("\n")
                    url_list.append(new_kosakana_fun_blog_url)
        elif kosakana_fun_blog_url.find("/archive") != -1:
            continue
        elif kosakana_fun_blog_url.find("?page=") != -1:
            continue
        elif kosakana_fun_blog_url.find("?amp=") != -1:
            continue
        else:
            if kosakana_fun_blog_url not in url_list:
                print(kosakana_fun_blog_url)
                f.write(kosakana_fun_blog_url)
                f.write("\n")
                url_list.append(kosakana_fun_blog_url)
    driver.quit()
f.close()