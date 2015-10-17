#!/env/usr/python
#-*- coding: utf-8 -*-
class Computer(object):
        ''' Este programa deverá mostrar o tempo de uso, qual a plataforma,
           distribuição, qual a cpu'''
        #ver distro:
        ##lsb_release -a
        #arquitetura
        ## arch
        def __init__(self):
            ''' aqui recebe todas as variaveis, e monta a parte visual
            do programa '''
            import tkinter as tk
            #
            #
            #### DEFINE VARS
            self.__system__()
            #
            #
            self.master = tk.Tk()
            self.master.title('Phoenix!')
            #
            self.estilo = ('FreeSerif 10')  
            self._distro_ = tk.Label(self.master,background='white', text='Distro:\n%s'%self.__distro__, font=self.estilo).grid(row=0)
            #
            _arch_ = tk.Label(self.master,background='white', text='Arquitetura:  %s'%self.__arch__, font=self.estilo).grid(row=2)
            #
            _prc_ = tk.Label(self.master,background='white', text='Processador:\n%s'%self.__processor__, font=self.estilo).grid(row=4)
            #
            _btn_ = tk.Button(self.master, text="Sair", font=self.estilo, background="#eee", foreground="#000",command=self.out).grid(row=6, columnspan=2)
            #
            #
            #
            self.master['background'] = 'white'
            #
            #
            self.master.geometry('170x140+1185+220')
            self.master.mainloop()
            #
        def out(self):
            ''' aqui fecha o aplicativo '''
            self.master.destroy()
            #
            #
            #
        def __system__(self):
            import os
            ######   PROCESSADOR ######
            os.system("cat /proc/cpuinfo > cpu.txt")
            ARQUIVO = open('cpu.txt','r')
            ### aqui ele recebe o valor do precessador
            self.__processor__ = self.__PROCESSOR__(ARQUIVO)
            ARQUIVO.close()
            os.system("rm cpu.txt")
            #
            ############################
            ##########  ARCH ###########
            ############################
            os.system("arch > arch.txt")
            ARQUIVO = open('arch.txt','r')
            ### aqui ele recebe o valor do precessador
            self.__arch__ = self.__ARCH__(ARQUIVO)
            ARQUIVO.close()
            os.system("rm arch.txt")
            #
            ############################
            #########  DISTRO ##########
            ############################
            os.system("lsb_release -a > distro.txt")
            ARQUIVO = open('distro.txt','r')
            ### aqui ele recebe o valor do precessador
            self.__distro__ = self.__DISTRO__(ARQUIVO)
            ARQUIVO.close()
            os.system("rm distro.txt")
            #
            #
            #
            #
        def __PROCESSOR__(self, ARQUIVO):
            InModel = ARQUIVO.read()
            COUNT,DUOPOINT = 0, 1
            while InModel[COUNT:COUNT+10] != 'model name':
                COUNT+=1
            COUNT+=10
            while InModel[COUNT:COUNT+2] != ": ":
                COUNT+=1
            COUNT+=2
            ENDS = COUNT
            while InModel[ENDS:ENDS+3] != "GHz":
                ENDS+=1
            retorno = str(InModel[COUNT:ENDS+3])
            #print(retorno)
            COUNT, ENDS = 0, 0
            while retorno[COUNT:COUNT+7] != '       ':
                COUNT+=1
            retorno = retorno[:COUNT] + "\n" + retorno[COUNT+6:]
            return retorno
        #
        #
        def __DISTRO__(self,ARQUIVO):
            txt = ARQUIVO.readlines()
            l = 0
            for ln in txt:
                if l == 1:
                    return ln[13:-1]
                l+=1
        #
        def __ARCH__(self,ARQUIVO):
            txt = ARQUIVO.read()
            return txt[:-1]

if __name__ == '__main__':
    Computer()
