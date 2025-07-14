from datetime import date, datetime, time

data_manual = date(1989, 11, 6)
data_automática = date.today()
print(data_manual)
print(data_automática)

data_hora_manual = datetime(2025, 7, 14)
data_hora_automatico = datetime.today()
print(data_hora_manual)
print(data_hora_automatico)

hora_manual = time(18, 2)
hora_automatica = datetime.now().strftime("%H:%M:%S")
print(hora_manual)
print(hora_automatica)