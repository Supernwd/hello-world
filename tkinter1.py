"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *

class Interface(Frame):

	def __init__(self,fenetre, **kwargs):
		Frame.__init__(self, fenetre, width=600, height=400, borderwidth=1, **kwargs)

		self.champ_label = Label(self, text="Pour quel nombre d'étages ?")
		self.master.title("titre.png")
		self.master.geometry("600x400+10+10")
		self.pack(fill=BOTH)
		self.champ_result = Label(self, text="résultat")
		self.entr1 = Entry(self)
		self.bouton_quitter = Button(self, text="partir pour\n une durée indefinie", command=self.quit)
		self.bouton_lancer = Button(self, text="proceder", command=self.calcule)
		self.can = Canvas(self,width=200, height=200, bg='white')
		self.champ_label.grid(row = 1, column = 1, columnspan = 2)
		self.champ_result.grid(row = 2, column = 4, columnspan = 2)
		self.bouton_quitter.grid(row = 3,column = 1)
		self.bouton_lancer.grid(row = 3,column = 2)
		self.entr1.grid(row = 2, column = 1)
		self.can.grid(row = 3, column = 4, columnspan = 1, rowspan = 3, padx = 5,pady = 5)


	def calcule(self):
		a=2
		n=0
		lim=int(self.entr1.get())-1
		while(n<lim):
			n = n+1
			a=a+3*n+2
		text = a	
		self.champ_result["text"]=text
		


if __name__ =="__main__":
# On crée une fenêtre, racine de notre interface
	fenetre = Tk()
	interface=Interface(fenetre)
	interface.mainloop()
	interface.destroy()