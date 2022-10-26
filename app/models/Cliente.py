
from ..database import engine
from sqlalchemy import text
from datetime import date
from app.models.ClienteDto import ClienteDto

class Cliente:

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

    def getEstatisticasValorReceber():

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

        return cliente_dto