import datetime
import locale
import schedule
import time
import requests

class LINE_Notify:
    def __init__(self):
        self.API_url = 'https://notify-api.line.me/api/notify'
        self.access_token = 'fFSNqLiMC3rzFt7H8SJpt0g0FDrk9i1Vtz9DtSviZ9m'
        self.__headers = {'Authorization':'Bearer'+self.access_token}
        
    def Sent_Message(self,message):
        payload = {'message':message}
        requests.post(self.API_url,headers=self.__headers,params=payload)
        
    

def Gomi_Sute_Mess():
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    Today = datetime.datetime.now()
    week_num = Today.weekday()
    w_list = ['月曜日','火曜日','水曜日','木曜日','金曜日','土曜日','日曜日']
    if week_num == 1 or week_num == 4:
        message='明日は可燃ゴミの日です。'
    elif week_num == 2:
        message='明日はビン・缶、ペットボトルの日です。'
    else:
        message='明日のゴミ捨てはありません。'
    
    return message

def main():
    LINE_Notify = LINE_Notify()
    message=Gomi_Sute_Mess()
    LINE_Notify.Sent_Message(message)

if __name__ == '__main__':
    schedule.every().day.at("22:00").do(main)
    
    while True:
        schedule.run_pending()
        time.sleep(1)