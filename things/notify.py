import datetime
import locale

locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
Today = datetime.datetime.now()

week_num = Today.weekday()

w_list = ['月曜日','火曜日','水曜日','木曜日','金曜日','土曜日','日曜日']

#print(Today,week_num,w_list[week_num])

if week_num == 1 or week_num == 4:
    message='明日は可燃ゴミの日です。'

elif week_num == 2:
    message='明日はビン・缶、ペットボトルの日です。'

else:
    message='明日のゴミ捨てはありません。'

print(w_list[week_num],message)