from datetime import date,time,datetime,timedelta

def tratrabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual.strftime('%a %d %B %Y - %H:%M:%S'))
    tupla = ('Segunda', 'Terça','Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criar = datetime(2018, 6, 20, 15, 30,20)
    data_string = '1/5/2015'
    data_convert = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_criar)
    print(data_convert)
    nova_data = data_convert - timedelta(days=356)
    print(nova_data)

def trabalhando_date():
    data_atual = date.today()
    print(data_atual.strftime('%a %d %B %Y'))
def trabalhando_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))
if __name__ == '__main__':
    trabalhando_date()
    trabalhando_time()
    tratrabalhando_datetime()