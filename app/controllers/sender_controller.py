
from flask import render_template
from flask import redirect

import pywhatkit
import random
import pandas as pd
import socket   

from datetime import datetime, timedelta
from ..models.Cliente import Cliente

class SenderController:

    def __init__(self) -> None:

        self.limit_msg_by_day = 500
        self.list_numbers = []
        self.list_ids = []
        self.list_names = []
        self.ipadress = socket.gethostbyname(socket.gethostname())  
        


    def send_message(self):      

        log_file = pd.read_csv('log_notificacoes.csv')


        cliente = Cliente()  
        clientes_devedores = cliente.getInfoDevedor()

        # condition, it avoids NUll values
        gen = (cliente for cliente in clientes_devedores if cliente[2] is not None)
    
        # load list of formatted numbers
        for cliente in gen:
            phone = cliente[2].replace(' ', '').replace('-', '')
            if len(phone) == 9:
                phone = '91' + phone
            if len(phone) == 11:
                self.list_numbers.append(phone)
                self.list_ids.append(cliente[0])
                self.list_names.append(cliente[1])
        
        # transform to dataframe
        all_info = pd.DataFrame({
            'id_cliente': self.list_ids, 
            'nome_cliente': self.list_names,
            'contato': self.list_numbers
        })

        # filter info
        log_file_remove = log_file.query('mes_envio == ' + datetime.now().strftime('%m'))
        info_filtered = all_info[~all_info['id_cliente'].isin(log_file_remove['id_cliente'].values)]

        # send message 
        # self.send(info_filtered['contato'].values)

        # save log
        self.save_log(target_df=info_filtered, log_file=log_file)

        return redirect('/home')


    def save_log(self, target_df: pd.DataFrame, log_file: pd.DataFrame) -> None:

        self.list_numbers = []
        self.list_ids = []
        self.list_names = []

        if target_df.empty is False:
            now = datetime.now()

            target_df['data_envio'] = now.strftime('%d-%m-%Y %H:%M:%S')
            target_df['mes_envio'] = now.strftime('%m')
            target_df['ip'] =  self.ipadress

            log = pd.concat([log_file, target_df])
            log = log.set_index('id_cliente')

            log.to_csv('log_notificacoes.csv')
            

    def send(self, list_numbers):

        msg1 = 'Caro(a) cliente Dele&Dela, \n Esta mensagem é um lembrete para o pagamento de sua fatura'
        msg2 = 'Caro(a) cliente Dele&Dela, \n Estamos enviando um lembrete para o pagamento de sua fatura'
        msg3 = 'Caro(a) cliente Dele&Dela, \n Não esqueça de realizar o pagamento da sua fatura'
        msg4 = 'Caro(a) cliente Dele&Dela, \n Esta mensagem é um lembrete para o pagamento de sua fatura'

        list_of_templates = [
            msg1, msg2, msg3 , msg4
        ]

        for number in list_numbers[:self.limit_msg_by_day]:

            now = datetime.now() + timedelta(seconds=15)

            number_format = '+550{}'.format(number)
            pywhatkit.sendwhatmsg_instantly(
                number_format, 
                list_of_templates[random.randrange(0,3)], 
                now.hour, 
                now.minute)