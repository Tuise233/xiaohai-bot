import requests
from bs4 import BeautifulSoup
import json

#协议头
header={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 Edg/80.0.361.48'
    }

#获取5e注册id （防止玩家注册后使用改名卡改名后导致查不到数据）
#形参 name 为玩家当前游戏昵称
def real_name(name):
    try:
        html =  requests.get('https://www.5ewin.com/api/search/player/1/16?keywords='+name,headers=header)
        data = json.loads(html.text)
        rname = data['data']['user']['list'][0]['domain']
        if data['data']['user']['list'][0]['vip_level'] == 0:
            rname = rname + '_=novip'
        else:
            rname = rname + '_=isvip'
        return rname
    except:
        return 'error'
    
#普通用户/VIP 获取信息
#形参 name为玩家注册id  fname为玩家当前昵称
def normal_user(name,fname):
    html = requests.get('https://www.5ewin.com/data/player/'+name,headers=header)
    html_text = BeautifulSoup(html.text,'html.parser')
    status = html_text.find_all('ul',attrs={'class':'stat-data'})
    user_number = html_text.find_all('ul',attrs={'class':'stat-data'})[0].find_all('li')[0].find_all('span')[0].get_text()
    user_races = html_text.find_all('ul',attrs={'class':'stat-data'})[0].find_all('li')[1].find_all('span')[0].get_text()
    user_rws = html_text.find_all('ul',attrs={'class':'stat-data'})[0].find_all('li')[2].find_all('span')[1].get_text()
    user_rating = html_text.find_all('ul',attrs={'class':'stat-data'})[0].find_all('li')[3].find_all('span')[1].get_text()
    user_rank = html_text.find_all('ul',attrs={'class':'stat-data'})[0].find_all('li')[4].find_all('span')[0].get_text()
    #检查是否被封禁
    if len(html_text.find_all('div',attrs={'class':'account_banned'})) != 0:
        checkban = html_text.find_all('div',attrs={'class':'account_banned'})[0].get_text()
    else:
        checkban = 'Safe'
    if checkban == '作弊封禁':
        row = '用户名:'+fname+'\n5E帐号:'+name+'\n帐号状态:作弊封禁\n总排名:'+user_number+'\n总场次:'+user_races+'\nRWS:'+user_rws+'\nRating:'+user_rating+'\nRank:'+user_rank
    elif checkban == '违规行为封禁':
        row = '用户名:'+fname+'\n5E帐号:'+name+'\n帐号状态:非法行为冻结\n总排名:'+user_number+'\n总场次:'+user_races+'\nRWS:'+user_rws+'\nRating:'+user_rating+'\nRank:'+user_rank
    else:
        row = '用户名:'+fname+'\n5E帐号:'+name+'\n帐号状态:正常\n总排名:'+user_number+'\n总场次:'+user_races+'\nRWS:'+user_rws+'\nRating:'+user_rating+'\nRank:'+user_rank
    return row

#SVIP用户 暂未开发完毕 动态页面
#形参 name为玩家注册id  fname为玩家当前昵称
def svip_user(name,fname):
    html = requests.get('https://www.5ewin.com/data/player/'+name,headers=header)
    html_text = BeautifulSoup(html.text,'html.parser')
    status = html_text.find_all('div',attrs={'class':'tbs mt20'})
