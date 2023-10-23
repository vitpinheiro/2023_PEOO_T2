def AbrirAgenda(cls):
        data_txt = input('Data: ')
        data = datetime.datetime.strptime(data_txt, '%d/%m/%Y')
        
        while True:
            hora_ini_txt = input('Hora inicial: ')
            hora_ini = datetime.datetime.strptime(hora_ini_txt, '%H:%M')
            hora_fin_txt = input('Hora final: ')
            hora_fin = datetime.datetime.strptime(hora_fin_txt, '%H:%M')
            
            if hora_ini >= hora_fin:
                print('A hora inicial deve ser menor que a hora final.')
            else: 
                contador_txt = input('Contador: ')
                contador = datetime.datetime.strptime(contador_txt, '%H:%M')
                
                while hora_ini <= hora_fin:
                    data_e_horario = datetime.datetime(data.year, data.month, data.day, hora_ini.hour, hora_ini.minute)
                    
                    agenda = Agenda(0, 0, 0, data_e_horario, confirmado=False)
                    NAgenda.inserir(agenda)

                    hora_ini += datetime.timedelta(minutes=contador.minute, hours=contador.hour)

                break

UI.Main()