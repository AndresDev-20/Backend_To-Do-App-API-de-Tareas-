# 📝 To-Do App Backend con FastAPI

Este proyecto es el backend de una aplicación de tareas (To-Do App) desarrollada con **FastAPI**. Permite gestionar usuarios y tareas con una arquitectura robusta y moderna.

## 🚀 Tecnologías Usadas

- ⚡ **FastAPI** – Framework rápido y moderno para construir APIs.
- 🐘 **PostgreSQL** – Base de datos relacional potente y confiable.
- 🧮 **SQLAlchemy + Alembic** – ORM y herramientas para migraciones de base de datos.
- ✅ **Pydantic** – Validación de datos con modelos.
- 🔄 **Uvicorn** – Servidor ASGI para desarrollo y producción.

## 🛠️ Instalación

1. **Clona el repositorio**

```bash
git clone https://github.com/tu_usuario/to-do-app-backend.git
cd to-do-app-backend
```

2. **Crea un entorno virtual y actívalo**

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. **Instala las dependencias**

```bash
pip install -r requirements.txt
```

4. **Configura la base de datos**

Crea un archivo `.env` o edita el archivo de configuración para definir la URL de la base de datos:

```
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_base
```

5. **Ejecuta las migraciones con Alembic**

```bash
alembic upgrade head
```

6. **Inicia el servidor**

```bash
uvicorn app.main:app --reload
```

## 🔗 Endpoints principales

| Método | Ruta                  | Descripción                      |
|--------|-----------------------|----------------------------------|
| GET    | `/tasks`              | Obtener todas las tareas         |
| POST   | `/tasks/create`       | Crear nueva tarea                |
| PUT    | `/tasks/update/{id}`  | Actualizar tarea existente       |
| DELETE | `/tasks/delete/{id}`  | Eliminar tarea por ID            |
| POST   | `/users/create`       | Crear nuevo usuario              |
| GET    | `/users`              | Listar todos los usuarios        |

## 📄 Documentación automática

FastAPI genera automáticamente documentación interactiva:

- Swagger UI: [`http://localhost:8000/docs`](http://localhost:8000/docs)
- ReDoc: [`http://localhost:8000/redoc`](http://localhost:8000/redoc)

## 📦 Estructura del proyecto

```
app/
│
├── main.py            # Punto de entrada principal
├── models/            # Modelos SQLAlchemy
├── schemas/           # Esquemas Pydantic
├── crud/              # Operaciones de base de datos
├── routes/            # Rutas (endpoints)
└── database/          # Configuración de conexión a PostgreSQL
```

## 🧪 Próximas mejoras (ideas)

- 🔐 Autenticación con JWT
- 📥 Registro y login de usuarios
- 👥 Manejo de permisos por usuario
- 🔔 Notificaciones de tareas pendientes

## 👨‍💻 Autor

**Yeison Andrés Marroquín Bernal**  
_Desarrollador Full Stack_

---

¡Gracias por revisar este proyecto! Si te fue útil o interesante, no dudes en dejar una ⭐ en tu repositorio.
