
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


        # format info
        all_info = self.get_all_info_formatted(clientes_devedores)


        # filter info
        log_file_remove = log_file.query('mes_envio == ' + datetime.now().strftime('%m'))
        info_filtered = all_info[~all_info['id_cliente'].isin(log_file_remove['id_cliente'].values)]

        # send message 
        self.send(info_filtered)

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


    def send(self, df: pd.DataFrame):

        msg1 = 'Dele&Dela\n Bom dia {}, tudo bem ?\n' \
            'Informamos que a parcela do seu crediário consta vencida a 7 dias. ' \
            'Efetue a regularização o mais breve possível. Pagando em dia você evita pagar juros, esperamos por você. ' \
            'Qualquer dúvida entre em contato com o financeiro, número 91 999600861.\n'\
            'Obs.: Caso já tenha efetuado o pagamento desconsidere a mensagem.'\
            ' Tenha uma excelente semana!'

        msg2 = 'Dele&Dela\n Bom dia {}, tudo bem ?\n' \
            'Informamos que a parcela do seu crediário consta vencida a 7 dias. ' \
            'Efetue a regularização o mais breve possível. Pagando em dia você evita pagar juros, esperamos por você. ' \
            'Qualquer dúvida entre em contato com o financeiro, número 91 999600861.\n'\
            'Obs.: Caso já tenha efetuado o pagamento desconsidere a mensagem.'\
            ' Tenha uma excelente semana!'

        list_of_templates = [
            msg1, msg2
        ]

        for index, row in df.iloc[:self.limit_msg_by_day].iterrows():
            now = datetime.now() + timedelta(seconds=15)

            number_format = '+550{}'.format(row['contato'])
            # number_format = '+550{}'.format('91981502481')
            pywhatkit.sendwhatmsg_instantly(
                number_format, 
                list_of_templates[random.randrange(0,1)].format(row['nome_cliente']), 
                now.hour, 
                now.minute)





    def get_all_info_formatted(self, clientes_devedores) -> pd.DataFrame:

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

        return all_info