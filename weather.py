import requests
import json

header={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 Edg/80.0.361.48'
}

# name 为城市名
def get_html(name):
    #天气API申请链接:http://doc.tianqiapi.com/603579
    url = 'https://tianqiapi.com/api?version=v6&appid=123123123123&appsecret=123123123123&city='+name
    html = requests.get(url,headers=header)
    content = html.text.encode('gbk').decode('unicode_escape')
    data = json.loads(content)
    city = data['city']
    country = data['country']
    weather = data['wea']
    min_tem = data['tem']
    max_tem = data['tem1']
    ave_tem = data['tem2']
    wind = data['win']
    wind_level = data['win_speed']
    air_level = data['air_level']
    tips = data['air_tips']
    row = '今日{0}{1}天气预报\n天气状况:{2}\n最低温度:{3}\n最高温度:{4}\n平均温度:{5}\n户外情况:{6}{7}\n空气质量:{8}\n\n{9}'.format(country,city,weather,min_tem,max_tem,ave_tem,wind_level,wind,air_level,tips)
    if city != name:
        row = '暂未查到当前城市天气预报,请核对城市名后重新查询\n目前仅支持国内省、市、县等，国外天气预报暂不可查'
    return row
