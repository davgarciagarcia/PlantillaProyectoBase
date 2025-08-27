from typing import List, Optional
from .paciente import Paciente

class Hospital:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self._pacientes: List[Paciente] = []

    def ingresar(self, p: Paciente) -> None:
        self._pacientes.append(p)
        self._pacientes.sort(key=lambda x: x.prioridad)

    def siguiente(self) -> Optional[Paciente]:
        return self._pacientes.pop(0) if self._pacientes else None

    def __len__(self) -> int:
        return len(self._pacientes)

    def __repr__(self) -> str:
        return f"Hospital('{self.nombre}', pacientes={len(self)})"
