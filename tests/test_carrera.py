import unittest

from src.logica.Logica_final import Logica_final
from src.modelo.competidor import Competidor
from src.modelo.carrera import Carrera
from src.modelo.declarative_base import Session

class CarreraTestCase(unittest.TestCase):
    def setUp(self):
        '''Iniciar la lógica'''
        self.logica = Logica_final()

        
        '''Abre la sesión'''
        self.session = Session()
            
    def test_listar_carreras_sin_carreras(self):
        self.logica.dar_carreras()
        busqueda = self.session.query(Carrera).all()
        self.assertEqual(len(busqueda), 0)

    def test_listar_carreras(self):
        self.logica.crear_carrera("Carrera1")
        self.logica.crear_carrera("Carrera2")

        self.logica.dar_carreras()
        busqueda = self.session.query(Carrera).all()
        self.assertEqual(len(busqueda), 2)

    def test_crear_carrera(self):
        carrera = self.logica.crear_carrera("NuevaCarrera")
        busqueda = self.session.query(Carrera).filter(Carrera.Nombre == "NuevaCarrera").all()
        self.assertEqual(len(busqueda), 1)
        self.assertTrue(carrera)
    
    def test_crear_carrera_nombre_repetido(self):
        self.logica.crear_carrera("NuevaCarrera")
        carrera2 = self.logica.crear_carrera("NuevaCarrera")
        busqueda = self.session.query(Carrera).all()
        self.assertEqual(len(busqueda), 1)
        self.assertFalse(carrera2)

    
    def test_crear_carrera_nombre_vacio(self):
        carrera = self.logica.crear_carrera("")
        busqueda = self.session.query(Carrera).all()
        self.assertEqual(len(busqueda), 0)
        self.assertFalse(carrera)
    
    def test_crear_carrera_nombre_largo(self):
        nombre_largo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras lorem ligula, volutpat sit amet sem in, placerat molestie justo. Sed eget dolor a ligula finibus vestibulum ut pretium eros. Pellentesque efficitur non quam ut ultrices."
        carrera = self.logica.crear_carrera(nombre_largo)
        busqueda = self.session.query(Carrera).all()
        self.assertEqual(len(busqueda), 0)
        self.assertFalse(carrera)

    def test_crear_carrera_suma_prob_uno(self):
        self.assertEqual(1,0)
    
    def test_crear_carrera_suma_prob_mayor_uno(self):
        self.assertEqual(1,0)
        
    def tearDown(self):
        '''Abre la sesión'''    
        self.session = Session()
        
        '''Consulta todas las carreras'''
        carreras = self.session.query(Carrera).all()
        '''Borra todas las carreras'''
        for carrera in carreras:
            self.session.delete(carrera)
        
        '''Consulta todos los competidores'''
        competidores = self.session.query(Competidor).all()
        '''Borra todos los competidores'''
        for competidor in competidores:
            self.session.delete(competidor)
        
        self.session.commit()
        self.session.close()





