import datetime
import os
l = 'images/'+str(datetime.datetime.now())+'.jpg'
print(l)

print(l.replace(' ', ''))

print(os.listdir('images'))