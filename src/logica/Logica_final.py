import imp
from sqlalchemy import func
from src.modelo.carrera import Carrera
from src.modelo.competidor import Competidor
from src.modelo.apostador import Apostador
from src.modelo.apuesta import Apuesta
from src.modelo.declarative_base import engine, Base, session

class Logica_final():


    def __init__(self):
        Base.metadata.create_all(engine)
        

    def dar_carreras(self):
        carreras = [elem.__dict__ for elem in session.query(Carrera).all()]
        return carreras

    def dar_carrera(self, id_carrera):
        if id_carrera == -1:
            carrera = session.query(Carrera).filter(Carrera.id == session.query(func.max(Carrera.id)))
        else:
            carrera = session.query(Carrera).get(id_carrera).__dict__
        return carrera

    def dar_carrera_nombre(self, nombre):
        carrera = session.query(Carrera).filter(Carrera.Nombre == nombre).first()
        carrera = carrera.__dict__
        return carrera   


    def crear_carrera(self, nombre):
        if not nombre or len(nombre) > 200:
            return False
        busqueda = session.query(Carrera).filter(Carrera.Nombre == nombre).all()
        if len(busqueda) == 0:
            carrera = Carrera(Nombre=nombre, Competidores=[], Abierta=True)
            session.add(carrera)
            session.commit()
            return True
        else:
            return False
        

    def editar_carrera(self, id, nombre):
        self.carreras[id]['Nombre'] = nombre
        """busqueda = session.query(Carrera).filter(Carrera.Nombre == nombre, Carrera.id != id).all()
        if len(busqueda) == 0:
            carrera = session.query(Carrera).filter(Carrera.id == id).first()
            carrera.Nombre = nombre
            session.commit()
            return True
        else:
            return False"""

    def terminar_carrera(self, id, ganador):
        self.carreras[id]['Ganador'] = ganador

    def eliminar_carrera(self, id):
        del self.carreras[id]

    def dar_apostadores(self):
        apostadores = [elem.__dict__ for elem in session.query(Apostador).all()]
        return apostadores

    def dar_apostador_por_id(self, apostador_id):
        return session.query(Apostador).filter_by(id=apostador_id).first().__dict__     

    def dar_apostador_por_nombre(self, apostador_nombre):
        return session.query(Apostador).filter(Apostador.Nombre == apostador_nombre).first().__dict__

    def aniadir_apostador(self, nombre):
        if not nombre or len(nombre) > 200:
            return False
        busqueda = session.query(Apostador).filter(Apostador.Nombre == nombre).all()
        if len(busqueda) == 0:
            apostador = Apostador(Nombre=nombre)
            session.add(apostador)
            session.commit()
            return True
        else:
            return False
    
    def editar_apostador(self, id, nombre):
        self.apostadores[id]['Nombre'] = nombre
    
    def eliminar_apostador(self, id):
        del self.apostadores[id]

    def dar_competidores_carrera(self, id):
        #return self.carreras[id]['Competidores'].copy()
        competidores = [elem.__dict__ for elem in session.query(Competidor).filter_by(carrera=id).all()]
        return competidores

    def dar_competidor(self, id_carrera, id_competidor):
        return self.carreras[id_carrera]['Competidores'][id_competidor].copy()

    def dar_competidor_por_id(self, competidor_id):
        return session.query(Competidor).filter_by(id=competidor_id).first().__dict__    

    def dar_competidor_por_nombre(self, competidor_nombre, id_carrera):
        return session.query(Competidor).filter(Competidor.Nombre == competidor_nombre, Competidor.carrera == id_carrera).first().__dict__ 

    def aniadir_competidor(self, id, nombre, probabilidad):
        if not nombre or len(nombre) > 200 or probabilidad < 0 or probabilidad > 1:
            return False
        busqueda = session.query(Competidor).filter(Competidor.Nombre == nombre).all()
        if len(busqueda) == 0:
            competidor = Competidor(Nombre=nombre, Probabilidad=probabilidad, carrera=id)
            session.add(competidor)
            session.commit()
            return True
        else:
            return False
        #self.carreras[id]['Competidores'].append({'Nombre':nombre, 'Probabilidad':probabilidad})

    def editar_competidor(self, id_carrera, id_competidor, nombre, probabilidad):
        self.carreras[id_carrera]['Competidores'][id_competidor]['Nombre']=nombre
        self.carreras[id_carrera]['Competidores'][id_competidor]['Probabilidad']=probabilidad
    
    def eliminar_competidor(self, id_carrera, id_competidor):
        del self.carreras[id_carrera]['Competidores'][id_competidor]

    def dar_apuestas_carrera(self, id_carrera):
        apuestas=[]
        res_apuestas = [elem.__dict__ for elem in session.query(Apuesta).filter_by(Carrera=id_carrera).all()]
        for res_apuesta in res_apuestas:
            apuesta = {}
            apuesta['Apostador'] = self.dar_apostador_por_id(res_apuesta['Apostador'])['Nombre']
            apuesta['Carrera'] = self.dar_carrera(res_apuesta['Carrera'])['Nombre']
            apuesta['Valor'] = res_apuesta['Valor']
            apuesta['Competidor'] = self.dar_competidor_por_id(res_apuesta['Competidor'])['Nombre']
            apuestas.append(apuesta)
        return apuestas
        #nombre_carrera =self.carreras[id_carrera]['Nombre']
        #return list(filter(lambda x: x['Carrera']==nombre_carrera, self.apuestas))

    def dar_apuesta(self, id_carrera, id_apuesta):
        return self.dar_apuestas_carrera(id_carrera)[id_apuesta].copy()

    def crear_apuesta(self, apostador, id_carrera, valor, competidor):
        id_competidor = self.dar_competidor_por_nombre(competidor, id_carrera)['id']
        id_apostador = self.dar_apostador_por_nombre(apostador)['id']
        apuesta = Apuesta(Carrera=id_carrera, Competidor=id_competidor, Apostador=id_apostador, Valor=valor)
        session.add(apuesta)
        session.commit()
        #n_apuesta = {}
        #n_apuesta['Apostador'] = apostador
        #n_apuesta['Carrera'] = self.carreras[id_carrera]['Nombre']
        #n_apuesta['Valor'] = valor
        #n_apuesta['Competidor'] = competidor
        #self.apuestas.append(n_apuesta)

    def editar_apuesta(self, id_apuesta, apostador, carrera, valor, competidor):
        self.apuestas[id_apuesta]['Apostador'] = apostador
        self.apuestas[id_apuesta]['Carrera'] = carrera
        self.apuestas[id_apuesta]['Valor'] = valor
        self.apuestas[id_apuesta]['Competidor'] = competidor

    def eliminar_apuesta(self, id_carrera, id_apuesta):
        nombre_carrera =self.carreras[id_carrera]['Nombre']
        i = 0
        id = 0
        while i < len(self.apuestas):
            if self.apuestas[i]['Carrera'] == nombre_carrera:
                if id == id_apuesta:
                    self.apuestas.pop(i)
                    return True
                else:
                    id+=1
            i+=1
        
        return False
                

        del self.apuesta[id_apuesta]

    def dar_reporte_ganancias(self, id_carrera, id_competidor):
        self.carreras[id_carrera]['Abierta']=False
        n_carrera = self.carreras[id_carrera]['Nombre']
        
        for ganancias in self.ganancias:
            if ganancias['Carrera'] == n_carrera:
                return ganancias['Ganancias'], ganancias['Ganancias de la casa']

