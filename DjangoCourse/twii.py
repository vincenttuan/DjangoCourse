import requests

def twii(r, pe, pb) :
    #url = 'http://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20190412&selectType=ALL'
    url = 'http://127.0.0.1:8000/twii/getcsv'
    data = requests.get(url).text
    data = data.replace('"', '')
    data = data.replace('-', '-1')

    twii_list = []
    for d in data.split('\n'):
        # "證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",
        list = d.split(',')
        if len(list) >= 7 and list[0] != '證券代號' and len(list[0]) == 4:
            if float(list[2]) > r and 0 <= float(list[4]) < pe and float(list[5]) < pb:
                dic = {}
                dic.setdefault('證券代號', list[0])
                dic.setdefault('證券名稱', list[1])
                dic.setdefault('殖利率', list[2])
                dic.setdefault('本益比', list[4])
                dic.setdefault('股價淨值比', list[5])
                twii_list.append(dic)
                #print(d)

    return twii_list

twii_list = twii(7, 10, 1)
print(twii_list)