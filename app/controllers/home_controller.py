
from ..database import engine

class HomeController:

    def index(self):

        result = engine.execute('SELECT * FROM TEST_DD.PCCLIENT p WHERE ROWNUM <= 5')

        for row in result:
            print(row)