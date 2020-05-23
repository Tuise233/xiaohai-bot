import requests
import json

def get_html():
    header={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 Edg/80.0.361.48'
    }
    datas = {
        'pageNo': '1',
        'pageSize': '1'
    }
    html = requests.post('https://www.b5csgo.com.cn/userBaseInfoController/getBannedList.do',headers=header,data=datas)
    data = json.loads(html.text)[0]
    row ='用户名:'+data['nickName']+'\nSteamID:'+str(data['steamId'])+'\n封禁原因:作弊封禁\n封禁时间:'+data['lastTime']+'\n封禁时长:永久封禁'
    return row