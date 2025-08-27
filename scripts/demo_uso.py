from nombre_proyecto.utils.distancias import manhattan, euclidea
from nombre_proyecto.clases.hospital import Hospital
from nombre_proyecto.clases.paciente import Paciente

print("manhattan((0,0),(3,4)) =", manhattan((0,0),(3,4)))
print("euclidea((0,0),(3,4))  =", round(euclidea((0,0),(3,4)), 3))

h = Hospital("Hospital Universitario")
h.ingresar(Paciente(1, "Ana", 2, "Revisión"))
h.ingresar(Paciente(2, "Luis", 1, "Trauma"))
print("Pacientes en cola:", len(h))
atendido = h.siguiente()
print("Atendiendo a:", atendido.nombre if atendido else None)
