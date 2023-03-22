from datetime import *
present=datetime.now()
yesterday=present-timedelta(1)
p1=present.strftime('%d/%m/%y')
p2=yesterday.strftime('%d/%m/%y')
print('Today',p1)
print('Yesterday',p2)


