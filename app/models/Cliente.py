
from ..database import engine
from sqlalchemy import text
from datetime import date
from app.models.ClienteDto import ClienteDto


class Cliente:

    def __init__(self) -> None:
        pass

    def real_br_money_mask(self, my_value):
        a = '{:,.2f}'.format(float(my_value))
        b = a.replace(',','v')
        c = b.replace('.',',')
        return c.replace('v','.')

    def getClientesDevedores():

        sql = text(
            'SELECT ' +
                'pc.CODCLI AS CODCLI, ' + 
                'pc.CLIENTE AS CLIENTE, ' + 
                'pc.TELCELENT AS TEL, ' + 
                'p.VALOR AS VALOR, ' + 
                'p.DTVENC AS DTVENC ' +
            'FROM DELEEDELA.PCPREST p ' +
                'INNER JOIN DELEEDELA.PCCLIENT pc ON p.CODCLI = pc.CODCLI ' + 
            'WHERE ' +
                '(' +
                    'p.CODCOB = :codcob1 OR p.CODCOB = :codcob2 OR p.CODCOB = :codcob3 OR p.CODCOB = :codcob4 OR p.CODCOB = :codcob5' +
                ') AND ' +
            'p.VPAGO IS NULL AND ' + 
            'TO_DATE(p.DTVENC) < :current_date'
        )

        result = engine.execute(sql, {
            'codcob1': 'CRLJ',
            'codcob2': 'COEX',
            'codcob3': 'REN1',
            'codcob4': 'REN2',
            'codcob5': '002',
            'current_date': date.today()
        })

        result = list(result.fetchone())

        return result

    def getEstatisticasValorReceber(self):

        cliente_dto = ClienteDto()

        sql = text(
            'SELECT ' +
                'SUM(p.VALOR) AS DEBITO_TOTAL, ' + 
                'SUM(p.VALOR) / COUNT ( DISTINCT p.CODCLI) AS MED_POR_CLI, ' + 
                'MAX(p.VALOR) AS V_MAX, ' + 
                'COUNT(p.VALOR) / COUNT ( DISTINCT p.CODCLI) AS N_MED_PARC_POR_CLI ' + 
            'FROM DELEEDELA.PCPREST p ' +
                'INNER JOIN DELEEDELA.PCCLIENT pc ON p.CODCLI = pc.CODCLI ' + 
            'WHERE ' +
                '(' +
                    'p.CODCOB = :codcob1 OR p.CODCOB = :codcob2 OR p.CODCOB = :codcob3 OR p.CODCOB = :codcob4 OR p.CODCOB = :codcob5' +
                ') AND ' +
            'p.VPAGO IS NULL AND ' + 
            'TO_DATE(p.DTVENC) < :current_date'
        )

        result = engine.execute(sql, {
            'codcob1': 'CRLJ',
            'codcob2': 'COEX',
            'codcob3': 'REN1',
            'codcob4': 'REN2',
            'codcob5': '002',
            'current_date': date.today()
        }) 

        result = result.fetchall()

        for i in result:
            cliente_dto.debito_total = i[0] 
            cliente_dto.debito_med_por_cliente = i[1]
            cliente_dto.valor_max_parcela = i[2]
            cliente_dto.qtd_med_parcelas_por_cliente = i[3]

        cliente_dto.debito_total = self.real_br_money_mask(cliente_dto.debito_total)
        cliente_dto.debito_med_por_cliente = self.real_br_money_mask(cliente_dto.debito_med_por_cliente)
        cliente_dto.valor_max_parcela = self.real_br_money_mask(cliente_dto.valor_max_parcela)
        cliente_dto.qtd_med_parcelas_por_cliente = round(cliente_dto.qtd_med_parcelas_por_cliente, 0)


        return cliente_dto