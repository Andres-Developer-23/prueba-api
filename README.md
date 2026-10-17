# 🚀 Prueba API

API REST de ejemplo construida con **FastAPI** para gestionar un catálogo simple de productos.
Proyecto de práctica con estructura `src/`, validaciones con Pydantic y despliegue en **Render**.

## ✨ Características

- FastAPI con `uv` como gestor de paquetes
- Validación de datos con Pydantic v2
- Arquitectura por capas: `routes/` · `schemas.py` · `storage.py`
- Documentación interactiva automática (Swagger / ReDoc)

## 📦 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Mensaje de bienvenida |
| `GET` | `/products/` | Lista los productos (limitable con `?limit=`) |
| `GET` | `/products/{product_id}` | Detalle de un producto por ID |
| `POST` | `/products/` | Crea un producto (devuelve `201`) |
| `DELETE` | `/products/{product_id}` | Elimina un producto por ID |

### Ejemplo de creación

```bash
curl -X POST http://localhost:8000/products/ \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Teclado", "precio": 25.5, "stock": 10}'
```

Respuesta:
```json
{"id": 1, "nombre": "Teclado", "descripcion": null, "precio": 25.5, "stock": 10}
```

## 🏁 Inicio rápido (local)

Requisitos: [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/Andres-Developer-23/prueba-api.git
cd prueba-api
uv sync
uv run fastapi run src/practicas/main.py
```

La API queda disponible en `http://localhost:8000`:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 📁 Estructura del proyecto

```
prueba-api/
├── src/
│   └── practicas/
│       ├── main.py          # App FastAPI + rutas raíz
│       ├── routes/
│       │   └── products.py  # Endpoints de productos
│       ├── schemas.py       # Modelos Pydantic
│       └── storage.py       # Almacén en memoria
├── pyproject.toml
├── render.yaml              # Configuración de despliegue en Render
└── uv.lock
```

## ☁️ Despliegue

Desplegada en **Render** vía Blueprint (`render.yaml`):
https://prueba-api-xxxx.onrender.com

> ⚠️ Los datos se guardan **en memoria**: se pierden al reiniciar o redesplegar.
> En el free tier la app se duerme tras ~15 min de inactividad (~50 s en despertar).

## 🛠️ Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic v2](https://docs.pydantic.dev/)
- [uv](https://docs.astral.sh/uv/)
- Despliegue: [Render](https://render.com/)
