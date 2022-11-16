
from flask import render_template
from flask import redirect

import pywhatkit
import random
import pandas as pd
from datetime import datetime, timedelta

from ..models.Cliente import Cliente

class SenderController:

    def send_message(self):

        result_list = []

        limit_msg_by_day = 500

        list_numbers = [
            '99074366',
            '81502481',
        ]

        msg1 = 'Caro(a) Dele&Dela, cliente \n Esta mensagem é um lembrete para o pagamento de sua fatura'
        msg2 = 'Caro(a) Dele&Dela, cliente \n Esta mensagem é um lembrete para o pagamento de sua fatura'
        msg3 = 'Caro(a) Dele&Dela, cliente \n Esta mensagem é um lembrete para o pagamento de sua fatura'
        msg4 = 'Caro(a) Dele&Dela, cliente \n Esta mensagem é um lembrete para o pagamento de sua fatura'

        list_of_templates = [
            msg1, msg2, msg3 , msg4
        ]


        #cliente = Cliente()  
        #clientes_devedores = cliente.getInfoDevedor()
        #for cliente in clientes_devedores:
        #    print(cliente[0])

        

        for number in list_numbers:

            now = datetime.now() + timedelta(seconds=15)

            number_format = '+55091{}'.format(number)

            pywhatkit.sendwhatmsg_instantly(
                number_format, 
                list_of_templates[random.randrange(0,3)], 
                now.hour, 
                now.minute)

            return redirect('/home')



    def save_log(self, id_cliente: int, sent_message: str):
        pass