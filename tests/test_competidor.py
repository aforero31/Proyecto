import unittest

from src.logica.Logica_final import Logica_final
from src.modelo.competidor import Competidor
from src.modelo.carrera import Carrera
from src.modelo.declarative_base import Session

class CompetidorTestCase(unittest.TestCase):
    def setUp(self):
        '''Iniciar la lógica'''
        self.logica = Logica_final()
        self.logica.crear_carrera("CarreraBase")
        
        '''Abre la sesión'''
        self.session = Session()
        self.idCarrera = [element.__dict__["id"] for element in self.session.query(Carrera).filter(Carrera.Nombre == "CarreraBase").all()]
        self.idCarrera = self.idCarrera[0]

    def test_aniadir_competidor(self):
        self.logica.aniadir_competidor(self.idCarrera, "Competidor1", 0.5)
        busqueda = self.session.query(Competidor).filter(Competidor.carrera == self.idCarrera, Competidor.Nombre == "Competidor1").all()
        self.assertEqual(len(busqueda), 1)

    def test_aniadir_competidor_nombre_vacio(self):
        competidor = self.logica.aniadir_competidor(self.idCarrera, "", 0.5)
        busqueda = self.session.query(Competidor).all()
        self.assertEqual(len(busqueda), 0)
        self.assertFalse(competidor)

    def test_aniadir_competidor_prob_negativa(self):
        competidor = self.logica.aniadir_competidor(self.idCarrera, "Competidor1", -0.5)
        busqueda = self.session.query(Competidor).all()
        self.assertEqual(len(busqueda), 0)
        self.assertFalse(competidor)
    
    def test_aniadir_competidor_prob_mayor_uno(self):
        competidor = self.logica.aniadir_competidor(self.idCarrera, "Competidor1", 2.5)
        busqueda = self.session.query(Competidor).all()
        self.assertEqual(len(busqueda), 0)
        self.assertFalse(competidor)
    
    def test_aniadir_competidor_nombre_largo(self):
        competidor = self.logica.aniadir_competidor(self.idCarrera, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras lorem ligula, volutpat sit amet sem in, placerat molestie justo. Sed eget dolor a ligula finibus vestibulum ut pretium eros. Pellentesque efficitur non quam ut ultrices.", 0.5)
        busqueda = self.session.query(Competidor).all()
        self.assertEqual(len(busqueda), 0)
        self.assertFalse(competidor)

    def test_aniadir_competidor_nombre_repetido(self):
        self.logica.aniadir_competidor(self.idCarrera, "Competidor1", 0.5)
        competidor2 = self.logica.aniadir_competidor(self.idCarrera, "Competidor1", 0.5)
        busqueda = self.session.query(Competidor).all()
        self.assertEqual(len(busqueda), 1)
        self.assertFalse(competidor2)

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






