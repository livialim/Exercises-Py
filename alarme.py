from datetime import datetime
import time
import playsound
print()
x = datetime.now().strftime('%H:%M:%S')
print('horario atual {}'.format(x))
a = str(input('Insira o horário: '))
b = str(input('Insira o minuto: '))
print('Alarme definido para {}:{}'.format(a, b))
while True:
    now = time.localtime()
    if now.tm_hour == int(a) and now.tm_min == int(b):
        print('ALARM NOW!')
        playsound.playsound('ex.021.mp3')