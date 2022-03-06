import sys
from PyQt5.QtWidgets import QApplication
from src.vista.InterfazEPorra import App_EPorra
#from src.logica.Logica_mock import Logica_mock
from src.logica.Logica_final import Logica_final

if __name__ == '__main__':
    # Punto inicial de la aplicación

    #logica = Logica_mock()
    logica = Logica_final()

    #print(logica.dar_apuestas_carrera(1))

    
    app = App_EPorra(sys.argv, logica)
    sys.exit(app.exec_())