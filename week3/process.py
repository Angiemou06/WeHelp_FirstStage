import urllib.request as request
import json
import csv
import bs4

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)

clist = data["result"]["results"]

with open("data.csv", "w", newline="", encoding="UTF-8-Sig") as csvfile:
    for attractions in clist:
        data_list=[]
        data_list.append(attractions["stitle"])
        data_list.append(attractions["address"][5:8])
        data_list.append(attractions["longitude"])
        data_list.append(attractions["latitude"])
        text = attractions["file"].lower()
        index = text.find(".jpg")
        data_list.append(attractions["file"][:index+4])
        writer = csv.writer(csvfile)
        writer.writerow(data_list)

def find_keys_with_same_value(input_dict):
    result_dict = {}
    for key, value in input_dict.items():
        if value not in result_dict:
            result_dict[value] = [key]
        else:
            result_dict[value].append(key)
    return result_dict

data={}
for attractions in clist:
    data.update({attractions["stitle"]:attractions["MRT"]})
data=find_keys_with_same_value(data)
with open("mrt.csv", "w", newline="", encoding="UTF-8-Sig") as csvfile:
    for key, value in data.items():
        if key == None:
            continue
        else:
            writer = csv.writer(csvfile)
            data_list = value
            data_list.insert(0, key)
            writer.writerow(data_list)

def getData(url):
    # 建立一個 Request 物件，附加 Request Ｈeaders 的資訊，讓你的連線請求看起來比較像真正的使用者
    req = request.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    })
    # 抓取資料
    with request.urlopen(req) as response:
        data_movie = response.read().decode("utf-8")
    # 解析資料
    root = bs4.BeautifulSoup(data_movie, "html.parser")
    
    return root
    
def crawler(url):
    root = getData(url)
    titles = root.find_all("div", class_="title") # 從網頁中尋找所有 div 標籤，且 class 為 title 者
    numbers = root.find_all("div", class_="nrec")
    with open('movie.txt', 'a') as file:
        for i in range(len(titles)):
            title = titles[i]
            number = numbers[i]
            if(title.a):
                content_title = title.a.string
                titleLink = "https://www.ptt.cc/" + titles[i].a["href"]
                root_title = getData(titleLink)
                date = root_title.find("span",class_="article-meta-tag",string="時間")
                content_date = date.next_sibling.string
            if(number.span):
                content_number = number.span.string
            else:
                content_number = "0"
            content = content_title + "," + content_number + "," + content_date + "\n"
            file.write(content)
    nextLink = root.find("a", string="‹ 上頁") # 從網頁中找到內文是 ‹ 上頁 的 a 標籤
    nextLink = "https://www.ptt.cc/" + nextLink["href"]
    return nextLink

url="https://www.ptt.cc/bbs/movie/index.html"
ct=0
while(ct<3):
    url = crawler(url)
    ct+=1