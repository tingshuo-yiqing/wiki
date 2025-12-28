from datetime import date, timedelta
import calendar

d1 = date(year=2011, month=4, day=12)  # 显示创建
d2 = date(2011, 4, 22)

while d2 >= d1:  # 日期可以比较，通过这个来遍历比三层循环更简洁
    # 处理逻辑
    d1.year
    d1.month
    d1.day
    print(d1.strftime("%Y-%m-%d"))  # 日期格式化为字符串
    d1 -= timedelta(days=1)  # 往前推一天
    d1 += timedelta(weeks=1)  # 往后推一周

print(d1.weekday())  # [0, 6], 0是星期日
print(d1.isoweekday())  # [1, 7]
print(calendar.isleap(d1.year))  # 判断是否是闰年
