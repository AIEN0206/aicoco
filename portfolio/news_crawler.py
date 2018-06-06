import requests, os
import pyquery
import codecs, time

def news(ticker):
    response = requests.get('https://finance.yahoo.com/quote/%s' % (ticker))
    
    if response.status_code == 200:
        d = pyquery.PyQuery(response.text)
        results = d('#quoteNewsStream-0-Stream li.js-stream-content')
        newslist = []
        count = 0
        # items() 可用來把 PyQuery 取回的搜尋結果輸出成 list，方便我們 for...in 取出
        for result in results.items():
            # 搜尋3筆資料後停止
            if count>=3:
                break
            title = result('h3').text()
            link = result('h3 > a').attr('href')
            summary = result('p').text()
            thenews = {"title":title,"link":link,"summary":summary}
            newslist.append(thenews)
            # time.sleep(1)
            count +=1
        return newslist

    else:
        print('response error')

# if __name__ == '__main__':
#     main(ticker)