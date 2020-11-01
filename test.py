from datetime import datetime

x = "07:30"
y = "09:30"

waktu_x = datetime.strptime(x,'%H:%M').time()
waktu_y = datetime.strptime(y,'%H:%M').time()
now = datetime.now().time()

print(waktu_x)
print(now)
print(waktu_y)

print( )