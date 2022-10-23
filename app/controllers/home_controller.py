
from flask import render_template
from ..database import engine

class HomeController:

    def index(self):

        result = engine.execute(
            'SELECT p.CODCLI as cod_cli FROM TEST_DD.PCCLIENT p'
        )

        # listResult = list(result.fetchall())

        # iterar sobre a lista de clientes devedores

        # enviar mensagem via wpp

        return render_template('home.html')
