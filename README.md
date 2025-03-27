# Sistema de Ruta Óptima con Búsqueda Heurística (A*)

Este proyecto implementa un sistema inteligente que encuentra la **mejor ruta** entre dos puntos en una red de transporte, utilizando el **algoritmo A\*** (búsqueda heurística). Se basa en una **base de conocimiento** representada como un grafo de conexiones.

También incluye una visualización del grafo y la ruta óptima con `matplotlib` y `networkx`.

---

## Requisitos del sistema

- Python 3.8 o superior  
- pip  
- Git (para clonar el repositorio)

---

## 1. Crear un entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar el entorno
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar el sistema

Desde la raiz del proyecto ejecutar:

```bash
python app/main.py
```

## Ejecucion de pruebas

Para correr las pruebas unitarias

```bash
pytest --maxfail=1 --disable-warnings -q
```

## Estructura del proyecto

```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── algoritmo_a_star.py
│   ├── base_conocimiento.py
│   └── main.py
├── requirements.txt
└── test
    ├── __init__.py
    └── test_algoritmo.py
```