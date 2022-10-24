
from flask import render_template

from ..models.Cliente import Cliente

class HomeController:

    def index(self):
        
        cliente = Cliente
        
        lista_clientes_devedores = cliente.getClientesDevedores()
    

        # listResult = list(result.fetchall())

        # iterar sobre a lista de clientes devedores

        # enviar mensagem via wpp

        return render_template('home.html')
