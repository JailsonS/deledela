
from ..database import engine

class HomeController:

    def index(self):

        result = engine.execute(
            'SELECT p.CODCLI as cod_cli FROM TEST_DD.PCCLIENT p'
        )

        for row in result:
            print(row['cod_cli'])
        
        return 'ok'