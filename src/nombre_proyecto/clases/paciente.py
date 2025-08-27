from dataclasses import dataclass
from typing import Optional

@dataclass
class Paciente:
    id: int
    nombre: str
    prioridad: int  # 1=alta, 2=media, 3=baja
    diagnostico: Optional[str] = None

    def es_urgente(self) -> bool:
        return self.prioridad == 1

    def __repr__(self) -> str:
        return f"Paciente(id={self.id}, nombre='{self.nombre}', prioridad={self.prioridad})"
