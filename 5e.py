import requests
import json

url = 'https://www.5ewin.com/api/banned/1'

def get_html(url):
    header={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 Edg/80.0.361.48'
    }
    html = requests.get(url,headers=header)
    content = html.text
    content = content.encode('utf-8').decode('unicode_escape')
    result = json.loads(content)
    data = result['data'][0]
    row = '用户名:'+data['username']+'\n5E帐号:'+data['domain']+'\nSteamID:'+data['steamid_64']+"\n封禁原因:"+data['description']+'\n封禁时间:'+data['datetime']+'\n封禁时长:'+data['expiretime']
    with open('5e.txt','w+',encoding='utf-8') as f:
        f.write(row)
        f.close()
