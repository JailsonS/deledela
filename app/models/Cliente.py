
from ..database import engine
from sqlalchemy import text
from datetime import date
from datetime import timedelta
from app.models.ClienteDto import ClienteDto


class Cliente:

    def __init__(self) -> None:
        pass

    def real_br_money_mask(self, my_value):
        a = '{:,.2f}'.format(float(my_value))
        b = a.replace(',','v')
        c = b.replace('.',',')
        return c.replace('v','.')

    def getClientesDevedores(self):

        list_clientes_dto = []
        conn = engine.connect(close_with_result=True)

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
            'pc.CODCLI <> 1 AND ' + 
            'p.VPAGO IS NULL AND ' + 
            ':current_date > TO_DATE(p.DTVENC)' 
        )

        result = conn.execute(sql, {
            'codcob1': 'CRLJ',
            'codcob2': 'COEX',
            'codcob3': 'REN1',
            'codcob4': 'REN2',
            'codcob5': '002',
            'current_date': date.today() - timedelta(days=7)
        })

        #result = result.fetchall()

        # for i in result:
        #     cliente_dto = ClienteDto()
# 
        #     cliente_dto.cod_cliente = i[0]
        #     cliente_dto.nome = i[1]
        #     cliente_dto.tel = i[2]
        #     cliente_dto.debito_parcela = i[3]
        #     cliente_dto.debito_parcela_venc = i[4]
# 
        #     list_clientes_dto.append(cliente_dto)

        return result

    def getEstatisticasValorReceber(self):

        cliente_dto = ClienteDto()
        conn = engine.connect(close_with_result=True)

        sql = text(
            'SELECT ' +
                'COUNT (DISTINCT pc.CODCLI) AS N_CLIENTES, ' + 
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
            'pc.CODCLI <> 1 AND ' + 
            'p.VPAGO IS NULL AND ' + 
            ':current_date > TO_DATE(p.DTVENC) ' + 
            'ORDER BY pc.CLIENTE'
        )

        result = conn.execute(sql, {
            'codcob1': 'CRLJ',
            'codcob2': 'COEX',
            'codcob3': 'REN1',
            'codcob4': 'REN2',
            'codcob5': '002',
            'current_date': date.today() - timedelta(days=7)
        }) 

        result = result.fetchall()

        for i in result:
            cliente_dto.n_clientes_debito = i[0] 
            cliente_dto.debito_total = i[1] 
            cliente_dto.debito_med_por_cliente = i[2]
            cliente_dto.valor_max_parcela = i[3]
            cliente_dto.qtd_med_parcelas_por_cliente = i[4]

        cliente_dto.debito_total = self.real_br_money_mask(cliente_dto.debito_total)
        cliente_dto.debito_med_por_cliente = self.real_br_money_mask(cliente_dto.debito_med_por_cliente)
        cliente_dto.valor_max_parcela = self.real_br_money_mask(cliente_dto.valor_max_parcela)
        cliente_dto.qtd_med_parcelas_por_cliente = round(cliente_dto.qtd_med_parcelas_por_cliente, 0)


        return cliente_dto


    def getInfoDevedor(self):
        conn = engine.connect(close_with_result=True)

        sql = text(
            'SELECT DISTINCT ' +
                'pc.CODCLI AS CODCLI, ' + 
                'pc.CLIENTE AS CLIENTE, ' + 
                'pc.TELCOB AS TEL, ' +
                'CASE WHEN (TO_DATE(p.DTVENC) >= :current_date_plus_3 AND TO_DATE(p.DTVENC) <= :current_date_plus_4) THEN :aviso ELSE :cobranca END AS TIPO ' +  
            'FROM DELEEDELA.PCPREST p ' +
                'INNER JOIN DELEEDELA.PCCLIENT pc ON p.CODCLI = pc.CODCLI ' + 
            'WHERE ' +
                '(' +
                    'p.CODCOB = :codcob1 OR p.CODCOB = :codcob2 OR p.CODCOB = :codcob3 OR p.CODCOB = :codcob4 OR p.CODCOB = :codcob5' +
                ') AND ' +
            'pc.CODCLI <> 1 AND ' + 
            'p.VPAGO IS NULL AND ' +
            '(' + 
                '(TO_DATE(p.DTVENC) >= :current_date_plus_3 AND TO_DATE(p.DTVENC) <= :current_date_plus_4) OR ' +
                '(:current_date > TO_DATE(p.DTVENC))' +
            ')'
        )

        result = conn.execute(sql, {
            'aviso': 'aviso', 'cobranca': 'cobranca',
            'codcob1': 'CRLJ',
            'codcob2': 'COEX',
            'codcob3': 'REN1',
            'codcob4': 'REN2',
            'codcob5': '002',
            'current_date': date.today() - timedelta(days=3),
            'current_date_plus_3': date.today() + timedelta(days=3),
            'current_date_plus_4': date.today() + timedelta(days=4),
        })

        return result
