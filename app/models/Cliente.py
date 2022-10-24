
from ..database import engine
from sqlalchemy import text
from datetime import date


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