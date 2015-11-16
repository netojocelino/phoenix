#!/env/usr/python
#-*- coding: utf-8 -*-
class Phoenix(object):
        ''' Este programa deverá exibir um pequeno menu que mostra botões
           que exibem as telas de "Computer" e "Today", breve mais widgets.
            Além de um Menu que mostra dados sobre o desenvolvedor. '''
        def __init__(self):
            import tkinter as tk
            self.dev      = "Jocelino Alves"
            self.material = "Python 3\ne Tkinter"
            #
            self.master = tk.Tk()
            self.master.title('Phoenix!')
            self.master.geometry('300x200+500+350')
            #
            ### aqui ficará o menu bar
            #### chama o menu principal que sustena tudo
            self.menuBar = tk.Menu(self.master)
            #
            #### chama o menu sobre
            self.About = tk.Menu(self.master, tearoff=0)
            #### chama os submenus de sobre
            self.About.add_command(label='Phoenix', command=self.__about__)
            self.About.add_command(label='Desenvolvedor', command=self.__dev__)
            #### adicona um separador
            self.About.add_separator()
            ####
            self.About.add_command(label='Fechar', command=self.master.destroy)
            #
            ## chama o menu links
            self.Links = tk.Menu(self.master, tearoff=0)
            #### submenus
            self.Links.add_command(label='Github',   command=lambda: self.__link__("Github"))
            self.Links.add_command(label='Homepage', command=lambda: self.__link__("Homepage"))
            self.Links.add_command(label='Facebook', command=lambda: self.__link__("Facebook"))
            
            #
            self.menuBar.add_cascade(label='Sobre', menu=self.About)
            self.menuBar.add_cascade(label='Links', menu=self.Links)
            #
            #
            #
            self.topSoft = 'Programa que mostra janelas \n(widgets) com'
            self.topSoft += ' informações sobre\no computador do usuário, e hora'
            self.topSoft += '\n\n'
            #
            tk.Label(self.master, text=self.topSoft, font=('FreeSerif 12')).grid(row=0, columnspan=2)
            #
            #
            tk.Button(self.master, text='Computador', command=self.__Computer__).grid(row=1, column=0)
            tk.Button(self.master, text='Agora', command=self.__Today__).grid(row=1, column=1)
            #
            #
            tk.Label(self.master, text="\n"+self.dev, font=('FreeSerif 14')).grid(row=2, columnspan=2)
            #
            #
            #
            #
            self.master.config(menu=self.menuBar)
            #
            self.master.wm_attributes("-topmost", 1)
            self.master.mainloop()
            #
        def __Computer__(self):
                from Computer import Computer
                Computer()
        def __Today__(self):
                from Today import Today
                Today()
        def __about__(self):
            from Alert import Alert
            Alert('Sobre Phoenix', 'Phoenix!\nPhoenix for Linux - 0.1\nPhoenix is designed by Jocelino\nAlves')
            #
        def __dev__(self):
            from Alert import Alert
            Alert('Sobre', 'Programa desenvolvido por\n%s, usando %s.\n<http://netojocelino.github.io>'%(self.dev, self.material))
            #
        def __link__(self, link):
            import webbrowser
            if link == 'Github':
                webbrowser.open_new_tab("http://github.com/NetoJocelino")
            elif link == 'Homepage':
                webbrowser.open_new_tab("http://netojocelino.github.io/")
            elif link == 'Facebook':
                webbrowser.open_new_tab("http://facebook.com/netojocelino")
            else:
                pass
            #
            #
if __name__ == '__main__':
    Phoenix()
