<img src='./images/escudo.png' width='30%' style="float:left" width="40%">

# Plantilla de Proyecto — Sistemas Inteligentes aplicados a la Salud

Proyecto base para VS Code con Python: scripts, paquetes, clases, notebooks y pruebas.

## Requisitos
- Python >= 3.10
- VS Code + extensiones: **Python**, **Pylance**, **Jupyter**

## Configuración 
- Cambia el nombre de la carpeta `src/nombre_proyecto` de acuerdo a tu proyecto
- Modifica `pyproyect.toml` de acuerdo a tus datos y a los datos del proyecto:
```
    [project]
    name = "nombre_proyecto"
    version = "0.1.0"
    description = "Plantilla para Proyecto Sistemas Inteligentes aplicados a la Salud"
    authors = [{ name = "tuNombre", email = "tuCorreo@ubu.es" }]
```

## Instalación (Windows)
```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -e . 
pip install -r requirements.txt
#pytest -q #Opcional
```

## Instalación (macOS/Linux)
```bash
python -m venv .venv
# python3 -m venv .venv
source .venv/bin/activate
pip install -e . 
pip install -r requirements.txt
#pytest -q #Opcional
```

## Estructura
- `src/` paquetes del proyecto (`utils`, `clases`).
- `scripts/` ejemplos ejecutables.
- `notebooks/` cuadernos Jupyter.
- `.vscode/` configuración (depuración, tareas, tests).
- `tests/` pruebas unitarias (`pytest`).--> *Esta carpeta es opcional*

## Uso rápido
```bash
# Script con argumentos
python scripts/script_basico.py --nombre "Ana" --repeticiones 2

# Demostración de clases y utilidades
python scripts/demo_uso.py
```

## Notebooks
Abrir `notebooks/Guia_VSCode_Ampliada.ipynb` y seleccionar el kernel del entorno `.venv`.
