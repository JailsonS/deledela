
from ..database import engine

class HomeController:

    def index(self):

        result = engine.execute(
            'SELECT p.CODCLI as cod_cli FROM TEST_DD.PCCLIENT p'
        )

        listResult = list(result.fetchall())

        print(listResult)
        
        return 'ok'