import urllib.request
import re
import time

UA = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
headers = {}
headers["User-Agent"] = UA

def get_html(url):
    n = 0
    while(n < 9):
        try:
            request = urllib.request.Request(url, headers = headers)
            response = urllib.request.urlopen(request, timeout = 10)
            a = response.read()
            response.close()
            return a
        except Exception as e:
            n += 1
            print("Error for the %d time, exception type: %s" % (n, e))
            time.sleep(5)
    return ""

def img_list(url):
    html = get_html(url)
    if html == "":
        print("Get image list error!!!")
        return []
    html = html.decode('utf-8')
    reg = r'<img.*?src="(.*?)".*?>' # how to recognize the images
    r = re.compile(reg)
    url_list = r.findall(html)
    return url_list

i = img_list("") # root page
n = 0
print(i)
for img in i:
    with open("%d.jpg" % n, "wb") as f: # filename
        f.write(get_html(img))
    n += 1
