import datetime
import locale

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
Today = datetime.datetime.now()

week_num = Today.weekday()

w_list = ['月曜日','火曜日','水曜日','木曜日','金曜日','土曜日','日曜日']

print(Today,week_num,w_list[week_num])