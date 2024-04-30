import unittest

class Alumno:
    def __init__(self,nombre, legajo, edad, mail):
        self.__nombre__ = nombre
        self.__legajo__ = legajo
        self.__edad__ = edad
        self.__mail__ = mail

    def obtener_nombre(self):
        return self.__nombre__

    def cambiar_mail(self, mail):
        self.__mail__= mail

class Materia:
    def __init__(self, nombre, profesores,alumnos:list[Alumno]):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

    def obtener_alumnos(self):
        return self.__alumnos__

class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__
    
    
class TestMateria(unittest.TestCase):
    def test_materia(self):
        nombre = "Calculo 1"
        profesores = "Dario"
        alumno1 = Alumno("Lucas", "62012", "22", "l.zapata")
        alumno2 = Alumno("Mario", "62127", "21", "mag.lopez")
        alumnos = [alumno1,alumno2]
        materia = Materia(nombre, profesores,alumnos)
        self.assertEqual(materia.__nombre__, nombre)
        self.assertEqual(materia.__profesores__, profesores)
        self.assertEqual(materia.__alumnos__, alumnos)

    def test_obtener(self):
        profesores = "Dario"
        alumno1 = Alumno("Lucas", "62012", "22", "l.zapata")
        alumno2 = Alumno("Mario", "62127", "21", "mag.lopez")
        alumnos = [alumno1,alumno2]
        materia = Materia("Calculo 1", profesores,alumnos)

        self.assertEqual(materia.obtener_profesores(), profesores)

    def test_cambiar(self):
        nombre = "Calculo 1"
        alumno1 = Alumno("Lucas", "62012", "22", "l.zapata")
        alumno2 = Alumno("Mario", "62127", "21", "mag.lopez")
        alumnos = [alumno1,alumno2]
        materia = Materia(nombre, "Dario",alumnos)
        materia.cambiar_nombre("Algebra")

        self.assertEqual(materia.__nombre__, "Algebra")

    def test_obtener_alumnos(self):
        alumno1 = Alumno("Lucas", "62080", "22", "l.zapata")
        alumno2 = Alumno("Mario", "62127", "21", "mag.lopez")
        alumno3 = Alumno('Martin','62272','20','m.tarantoviez')
        alumnos = [alumno1,alumno2,alumno3]
        
        materia = Materia('Calculo 1','Dario',alumnos)
        self.assertEqual(materia.obtener_alumnos(),alumnos)

class TestProfesor(unittest.TestCase):
    def test_profesor(self):
        profesores = Profesor("Dario", "JTP", "23321")
        self.assertEqual(profesores.__nombre__, "Dario")
        self.assertEqual(profesores.__cargo__, "JTP")
        self.assertEqual(profesores.__legajo__, "23321")

    def test_obtener_nombre(self):
        profesores = Profesor("Dario", "JTP", "23321")
        self.assertEqual(profesores.obtener_nombre(), "Dario")

    def test_obtener_cargo(self):
        profesores = Profesor("Dario", "JTP", "23321")
        self.assertEqual(profesores.obtener_cargo(), "JTP")

    def test_obtener_legajo(self):
        profesores = Profesor("Dario", "JTP", "23321")
        self.assertEqual(profesores.obtener_legajo(), "23321")

class TestAlumno(unittest.TestCase):
    def test_alumno(self):
        alumno = Alumno("Lucas", "62012", "22", "l.zapata")
        self.assertEqual(alumno.__nombre__, "Lucas")
        self.assertEqual(alumno.__legajo__, "62012")
        self.assertEqual(alumno.__edad__, "22")
        self.assertEqual(alumno.__mail__, "l.zapata") 

    def test_obtener_nombre(self):
        alumno = Alumno("Lucas", "62012", "22", "l.zapata")
        self.assertEqual(alumno.obtener_nombre(), "Lucas")

    def test_cambiar_mail(self):
        mail = "l.zapata"
        alumno = Alumno("Lucas", "62012", "22", mail)
        alumno.cambiar_mail("luc.zap")
        self.assertEqual(alumno.__mail__, "luc.zap")
    
    
if __name__ == '__main__':
    unittest.main()