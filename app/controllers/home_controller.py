
from flask import render_template

from ..models.Cliente import Cliente

class HomeController:

    def index(self):
        
        cliente = Cliente
        
        lista_clientes_devedores = cliente.getClientesDevedores()
    
        # iterar sobre a lista de clientes devedores

        # enviar mensagem via wpp

        return render_template('pages/login.html')
