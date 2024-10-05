import tkinter as tk
from tkinter import messagebox

class Calculadora:
   def __init__(self):
       # Criação de constantes
       self.PADX = 10
       self.PADY = 5
       self.FONT_LABELS = ('Verdana', 12, 'bold')
       self.FONT_ENTRYS = ('Verdana', 14, 'bold')
       self.FONT_BUTTONS = ('Arial', 16, 'bold')

       # Criação de variáveis
       self.number_term = 1


       # Criar a janela principal
       self.janela = tk.Tk()
       self.janela.title("Calculadora Tradicional")


       # Criar um campo de texto para receber o primeiro termo
       label1 = tk.Label(self.janela, text="Termo-1:", font=self.FONT_LABELS, fg='blue')
       label1.grid(row=0, column=0, columnspan=2, padx=self.PADX, pady=self.PADY)
       self.term1 = tk.Entry(self.janela, width=20,font=self.FONT_BUTTONS, fg='green')
       self.term1.grid(row=0, column=2, columnspan=3, padx=self.PADX, pady=self.PADY)


       # Criar um campo de rótulo para receber o operador
       self.operator_var = tk.StringVar()
       self.operator = tk.Label(self.janela, state=tk.ACTIVE, textvariable=self.operator_var,font=self.FONT_BUTTONS)
       self.operator.grid(row=1, column=0, columnspan=5, padx=self.PADX, pady=self.PADY)


       # Criar um campo de texto para receber o segundo termo
       label2 = tk.Label(self.janela, text="Termo-2:", font=self.FONT_LABELS, fg='blue')
       label2.grid(row=2, column=0, columnspan=2, padx=self.PADX, pady=self.PADY)
       self.term2 = tk.Entry(self.janela, width=20,font=self.FONT_BUTTONS, fg='green')
       self.term2.grid(row=2, column=2, columnspan=3, padx=self.PADX, pady=self.PADY)


       # Criar um campo de texto para receber o segundo termo
       label2 = tk.Label(self.janela, text="Resultado:", font=self.FONT_LABELS, fg='blue')
       label2.grid(row=3, column=0, columnspan=2, padx=self.PADX, pady=10)
       self.result = tk.Entry(self.janela, width=20,font=self.FONT_BUTTONS, fg='green')
       self.result.grid(row=3, column=2, columnspan=3, padx=self.PADX, pady=self.PADY)


       # Criar os botões numéricos e operadores



       bt7 = tk.Button(self.janela, text="7", width=6, command=lambda: self.click_bt_number("7"),  font=self.FONT_BUTTONS, fg='red')
       bt7.grid(row=4, column=0, padx=self.PADX, pady=self.PADY)
       bt8 = tk.Button(self.janela, text="8", width=6, command=lambda: self.click_bt_number("8"),font=self.FONT_BUTTONS, fg='red')
       bt8.grid(row=4, column=1, padx=self.PADX, pady=self.PADY)
       bt9 = tk.Button(self.janela, text="9", width=6, command=lambda: self.click_bt_number("9"),font=self.FONT_BUTTONS, fg='red')
       bt9.grid(row=4, column=2, padx=self.PADX, pady=self.PADY)
       btb = tk.Button(self.janela, text="<-", width=6, command=lambda: self.click_left(),font=self.FONT_BUTTONS, fg='red')
       btb.grid(row=4, column=3, padx=self.PADX, pady=self.PADY)
       btc = tk.Button(self.janela, text="Limpar", width=6, command=lambda: self.click_clear(),font=self.FONT_BUTTONS, fg='red')
       btc.grid(row=4, column=4, padx=self.PADX, pady=self.PADY)


       bt4 = tk.Button(self.janela, text="4", width=6, command=lambda: self.click_bt_number("4"),font=self.FONT_BUTTONS, fg='red')
       bt4.grid(row=5, column=0, padx=self.PADX, pady=self.PADY)
       bt5 = tk.Button(self.janela, text="5", width=6, command=lambda: self.click_bt_number("5"),font=self.FONT_BUTTONS, fg='red')
       bt5.grid(row=5, column=1, padx=self.PADX, pady=self.PADY)
       bt6 = tk.Button(self.janela, text="6", width=6, command=lambda: self.click_bt_number("6"),font=self.FONT_BUTTONS, fg='red')
       bt6.grid(row=5, column=2, padx=self.PADX, pady=self.PADY)
       btdiv = tk.Button(self.janela, text="/", width=6, command=lambda: self.click_bt_oper("/"),font=self.FONT_BUTTONS, fg='red')
       btdiv.grid(row=5, column=3, padx=self.PADX, pady=self.PADY)
       btmul = tk.Button(self.janela, text="x", width=6, command=lambda: self.click_bt_oper("x"),font=self.FONT_BUTTONS, fg='red')
       btmul.grid(row=5, column=4, padx=self.PADX, pady=self.PADY)


       bt1 = tk.Button(self.janela, text="1", width=6, command=lambda: self.click_bt_number("1"),font=self.FONT_BUTTONS, fg='red')
       bt1.grid(row=6, column=0, padx=self.PADX, pady=self.PADY)
       bt2 = tk.Button(self.janela, text="2", width=6, command=lambda: self.click_bt_number("2"),font=self.FONT_BUTTONS, fg='red')
       bt2.grid(row=6, column=1, padx=self.PADX, pady=self.PADY)
       bt3 = tk.Button(self.janela, text="3", width=6, command=lambda: self.click_bt_number("3"),font=self.FONT_BUTTONS, fg='red')
       bt3.grid(row=6, column=2, padx=self.PADX, pady=self.PADY)
       btless = tk.Button(self.janela, text="-", width=6, command=lambda: self.click_bt_oper("-"),font=self.FONT_BUTTONS, fg='red')
       btless.grid(row=6, column=3, padx=self.PADX, pady=self.PADY)
       btplus = tk.Button(self.janela, text="+", width=6, command=lambda: self.click_bt_oper("+"),font=self.FONT_BUTTONS, fg='red')
       btplus.grid(row=6, column=4, padx=self.PADX, pady=self.PADY)


       bt0 = tk.Button(self.janela, text="0", width=6, command=lambda: self.click_bt_number("0"),font=self.FONT_BUTTONS, fg='red')
       bt0.grid(row=7, column=1, padx=self.PADX, pady=self.PADY)
       # Botão de igual
       botao_igual = tk.Button(self.janela, text="=", width=6, command=lambda: self.calculate(),font=self.FONT_BUTTONS, fg='red')
       botao_igual.grid(row=7, column=4, padx=self.PADX, pady=self.PADY)


   # Funções para as operações
   def click_bt_number(self, numero):
       # Atualizar o valor no campo de texto do Termo1 ou Termo2
       if self.number_term == 1:
           current_number = self.term1.get()
           self.term1.delete(0, tk.END)
           self.term1.insert(0, current_number + str(numero))
       else:
           current_number = self.term2.get()
           self.term2.delete(0, tk.END)
           self.term2.insert(0, current_number + str(numero))


   def click_left(self):
       # Voltar um número de um dos termos
       if self.number_term == 1:
           current_number = self.term1.get()
           if len(current_number) > 0:
               current_number = current_number[:-1]
               self.term1.delete(0, tk.END)
               self.term1.insert(0, current_number)
       else:
           current_number = self.term2.get()
           if len(current_number) > 0:
               current_number = current_number[:-1]
               self.term2.delete(0, tk.END)
               self.term2.insert(0, current_number)


   def click_clear(self):
       self.term1.delete(0, tk.END)
       self.term2.delete(0, tk.END)
       self.result.delete(0, tk.END)
       self.operator_var.set('')
       self.number_term = 1


   def click_bt_oper(self, oper):
       self.operator_var.set(oper)
       self.number_term = 2


   def calculate(self):
       if self.operator_var.get() != '' and self.term1.get() != '' and self.term2.get() != '':
           term1 = int(self.term1.get())
           term2 = int(self.term2.get())
           if self.operator_var.get() == '/':
               result = term1 / term2
           elif self.operator_var.get() == '+':
               result = term1 + term2
           elif self.operator_var.get() == '-':
               result = term1 - term2
           elif self.operator_var.get() == 'x':
               result = term1 * term2
           self.result.delete(0, tk.END)
           self.result.insert(0, str(result))
       else:
           messagebox.showinfo("Erro", "Por favor, preencha todos os campos.")


   def run(self):
       self.janela.mainloop()




if __name__ == '__main__':
   calc = Calculadora()
   calc.run()
