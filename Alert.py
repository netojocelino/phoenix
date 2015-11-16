#!/env/usr/python
#-*- coding: utf-8 -*-
class Alert:#(object):
        ''' Este programa deverá gerar um alerta que terá o título, corpo e
           botão definidos pelo desenvolvedor '''
        def __init__(self, titulo, msg, btn='Ok', FileLog=None):
                ''' Aqui são iniciadas as variaveis '''
                self.FileLog = FileLog
                self.titulo = titulo
                self.msg = str("\n" + msg)
                self.btn = btn
                #print(self.__log__())
                self.__show__()
        def __show__(self):
                import tkinter as tk
                #
                self.master = tk.Tk()
                #
                self.master.title(self.titulo)
                #
                tk.Label(self.master, text=self.msg).grid(row=0,columnspan=1)
                #
                tk.Button(self.master, text=self.btn, command=self.out).grid(row=2,columnspan=2)
                #
                self.master.geometry('200x120+500+400')
                #
                self.master.wm_attributes("-topmost", 1)
                self.master.mainloop()
        #
        def __call__(self, titulo, msg, btn):
                self.__init__(titulo, msg, btn)
                #
        def __callable__(titulo, msg, btn):
                self.__init__(self, titulo, msg, btn)
                #
        def out(self):
                if self.FileLog is None:
                        pass
                else:
                        Arq = open(self.FileLog, 'a')
                        Arq.write(self.__log__())
                        Arq.close()
                #self.__log__()
                self.master.destroy()
        #
        def __log__(self):
                return ('Alerta.\nTítulo: %s.\nMensagem: %s.\nBotão: %s.'%(self.titulo, self.msg, self.btn))
if __name__ == '__main__':
        Alert('Bem Vindo!', 'Você acaba de iniciar o módulo\nAlert\n', 'Fechar')
