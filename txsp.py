import requests
import json
import re

#成长明细
#/fcgi-bin/comm_cgi?name=get_score_flow&score_type=1

# 钉钉机器人的 webhook
webhook = os.environ["webhook"] # 钉钉机器人的 webhook
#webhook = 'https://oapi.dingtalk.com/robot/send?access_token=4978dbdd11859e0e4a036d517e8219e1ec4d06a3ad9aa968d10abe947d409e61'
cookie= os.environ["cookie"] #邮箱
headers = {
    'Referer': 'https://film.qq.com/x/autovue/grade/?ptag=Vgrade.rule',
    'Content-Type': 'text/plain;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54',
    'Referer':'https://v.qq.com',
    'Cookie':cookie
}
global content
contents=''
def output(content):
    global contents
    contents += '\n' + content
    print(content)
    return contents
def sign_1():
    # 观看60分钟签到请求
    url_1 ='https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=1&_=1582997048625&callback=Zepto1582997031843'
    sign_1 = requests.get(url=url_1,headers=headers)
    content = re.findall('\{[^\}]+\}', sign_1.text)[0]
    contents=json.loads(content)['msg']
    output(f'[+] 观看60分钟签到状态： {contents}')
def sign_3():
    # 弹幕签到请求
    url_3 =  'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=3&_=1582368319252&callback=Zepto1582368297765'
    sign_3 = requests.get(url=url_3,headers=headers)
    content = re.findall('\{[^\}]+\}', sign_3.text)[0]
    contents=json.loads(content)['msg']
    output(f'[+] 弹幕签到状态： {contents}')
    
def sign_6():
    # 赠送签到请求
    url_6 =  'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=6&_=1582366326994&callback=Zepto1582366310545'
    sign_6 = requests.get(url=url_6,headers=headers)
    content = re.findall('\{[^\}]+\}', sign_6.text)[0]
    contents=json.loads(content)['msg']
    output(f'[+] 赠送签到状态： {contents}')
    
def sign_7():
    # 下载签到请求
    url_7 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=7&_=1582364733058&callback=Zepto1582364712694'  
    sign_7 = requests.get(url=url_7,headers=headers)
    content = re.findall('\{[^\}]+\}', sign_7.text)[0]
    contents=json.loads(content)['msg']
    output(f'[+] 下载签到状态： {contents}')
    
# 签到请求 20v力   
def sign_10():
    url_10 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2&_=1555060502385&callback=Zepto1555060502385'
    sign_10 = requests.get(url=url_10,headers=headers)
    content = re.findall('\{[^\}]+\}', sign_10.text)[0]
    contents=json.loads(content)['msg']
    output(f'[+] 签到请求1状态： {contents}')
   
# 签到请求,随机
def sign_11():
    url_11 = 'https://v.qq.com/x/bu/mobile_checkin'
    sign_11 = requests.get(url=url_11,headers=headers)
    #content = re.findall('\{[^\}]+\}', sign_11.text)[0]
    #contents=json.loads(content)['msg']
    #print(f'[+] 签到请求2状态： {contents}')
    if 'Unauthorized' in sign_11:
        output ('[+] 签到请求2状态：  错误,Cookie 失效')
       
    else:
        output ('[+] 签到请求2状态：  成功')
        

def userinfo():
    header = {
    'Host': 'vip.video.qq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54',
    'Cookie':'tvfe_boss_uuid=fff6e261fdba336a; pgv_pvid=6821202755; video_platform=2; video_guid=2d0a084412b55178; uin=o0753476038; skey=@NQgPsvEUE; RK=4YyJuUobT8; luin=o0753476038; lskey=00010000ce7372c16fe52c61283aa90966dbc5c8bead2fe8372f220a2461bdb560951ec12179fa0bb377fa88; ptcz=9b5d1500609128b17f085cb97b737bf47f005d34215333107cb262ec7d473d4f; qq_nick=%25E6%25A1%259C; qq_head=http%3A%2F%2Fthirdqq.qlogo.cn%2Fg%3Fb%3Dsdk%26k%3DsslUu06z79AOu48ZNd7PNg%26s%3D140%26t%3D1621760613; main_login=qq; vuserid=155043867; vusession=SWZlb4ckl3FjTLg9okMkoA..; last_refresh_time=1624196483264; last_refresh_vuserid=155043867;',
    'Referer': 'https://film.qq.com/x/autovue/grade/?ptag=Vgrade.rule',
    }
    #获取用户信息
    url= 'https://vip.video.qq.com/rpc/trpc.query_vipinfo.vipinfo.QueryVipInfo/GetVipUserInfoH5'
    data={
        "geticon":1,
        "viptype":"svip",
        "platform":100
        }
    userinfo = requests.post(url=url,json=data,headers=header)
    #当前V力值
    level_score=json.loads(userinfo.text)['score']
    output(f'[+] 当前V力值： {level_score}')
   
def dingtalk(contents):
    webhook_url = webhook
    dd_header = {"Content-Type": "application/json", "Charset": "UTF-8"}
    dd_message = {
        "msgtype": "text",
        "text": {
            "content": f'腾讯视频签到提醒！\n{contents}'
        }
    }
    r = requests.post(url=webhook_url,headers=dd_header,data=json.dumps(dd_message))
    if r.status_code == 200:
        print('[+] 钉钉消息已推送，请查收  ')
def main():
    title='开始签到'
    content_1=sign_1()
    content_3=sign_3()
    content_6=sign_6()
    content_7=sign_7()
    content_10=sign_10()
    content_11=sign_11()
    content_userinfo=userinfo()
    global contents
    dingtalk(contents)

if __name__ == '__main__':
    main()   