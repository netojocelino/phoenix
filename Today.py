#!/env/usr/python
#-*- coding: utf-8 -*-
class Today(object):
        ''' Este programa deverá mostrar o horario para o usuário, mostrando
           data, horario e dia da semana '''
        def __init__(self):
            ''' aqui recebe todas as variaveis, e monta a parte visual
               do programa '''
            import tkinter as tk
            self.HOURS = self.__NOW__()[0]
            self.DATE = self.__NOW__()[1]
            self.WEEKDAY = self.__NOW__()[2]
            #
            self.master = tk.Tk()
            self.master.title('Phoenix!')
            #
            self.__tkLHora__ = tk.Label(self.master, text=self.HOURS, font=('FreeSerif 24'))
            self.__tkLHora__.grid(row=0, columnspan=2)
            #
            self.__tkLDia__ = tk.Label(self.master, text=str(self.DATE + "("+self.WEEKDAY+")"), font=('FreeSerif 17'))
            self.__tkLDia__.grid(row=2, columnspan=2)
            tk.Button(self.master, text="Sair", font=('FreeSerif 10'), background="#eee", foreground="#000",command=self.out).grid(row=3, columnspan=2)
            #
            self.__refresh__()
            #
            #
            self.master['background'] = 'white'
            self.__tkLHora__['background'] = 'white'
            self.__tkLDia__['background'] = 'white'
            self.__tkLHora__['foreground'] = 'blue'
            self.__tkLDia__['foreground'] = 'black'
            #
            #
            self.master.geometry('170x100+1185+90')
            self.master.mainloop()
            #
        def __refresh__(self):
            ''' aqui ele atualiza a parte visual do programa '''
            self.__NOW__()
            self.__tkLHora__['text'] = str(self.__NOW__()[0])
            #self.__tkLDia__['text'] = str(self.__NOW__[1] + "("+self.__NOW__[2]+")")
            #
            self.__tkLHora__.after(500, self.__refresh__)
            
            #
        def out(self):
            ''' aqui fecha o aplicativo '''
            self.master.destroy()
            #
        def __weekday__(self, tmp):
            ''' aqui ele reconhece o dia da semana '''
            day = {'Sun': 'Dom', 'Mon': 'Seg', 'Tue': 'Ter', 'Wed': 'Qua',
                   'Thu': 'Qui', 'Fri': 'Sex', 'Sat': 'Sab'}
            return day[tmp]
        #
        def __NOW__(self):
            ''' aqui atribui o valor às variaveis '''
            import time
            hora = time.strftime("%H:%M:%S")
            data = time.strftime("%d-%m-%Y")
            dia = time.strftime("%a")
            # retorna
            ### hora, data, dia
            return (hora, data, self.__weekday__(dia))

if __name__ == '__main__':
    Today()
