
from flask import render_template

from ..models.Cliente import Cliente

class HomeController:

    def index(self):
        
        cliente = Cliente()
        
        cliente_info_debito = cliente.getEstatisticasValorReceber()

        return render_template('pages/home.html', info_cliente=cliente_info_debito)

    def send_notification(self):
        pass