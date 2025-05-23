

---

# 📝 To-Do App Backend con FastAPI

Este proyecto es el backend de una aplicación de tareas (To-Do App) desarrollada con **FastAPI**. Permite gestionar usuarios y tareas con una arquitectura robusta, moderna y segura mediante autenticación con JWT.

## 🚀 Tecnologías Usadas

* ⚡ **FastAPI** – Framework rápido y moderno para construir APIs.
* 🐘 **PostgreSQL** – Base de datos relacional potente y confiable.
* 🧮 **SQLAlchemy + Alembic** – ORM y herramientas para migraciones de base de datos.
* ✅ **Pydantic** – Validación de datos con modelos.
* 🔐 **JWT (JSON Web Tokens)** – Autenticación segura de usuarios.
* 🔄 **Uvicorn** – Servidor ASGI para desarrollo y producción.
* 🔒 **Passlib (bcrypt)** – Encriptación de contraseñas.

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

4. **Configura el entorno**

Crea un archivo `.env` con tus variables de entorno:

```
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_base
SECRET_KEY=tu_clave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
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

### 🧑‍💼 Autenticación

| Método | Ruta             | Descripción                    |
| ------ | ---------------- | ------------------------------ |
| POST   | `/auth/register` | Registrar un nuevo usuario     |
| POST   | `/auth/login`    | Iniciar sesión y obtener token |

> 💡 Todos los endpoints protegidos requieren incluir el token en el header:
> `Authorization: Bearer <token>`

### 📋 Tareas

| Método | Ruta                 | Descripción                | Protección |
| ------ | -------------------- | -------------------------- | ---------- |
| GET    | `/tasks`             | Obtener todas las tareas   | ✅ Privado  |
| POST   | `/tasks/create`      | Crear nueva tarea          | ✅ Privado  |
| PUT    | `/tasks/update/{id}` | Actualizar tarea existente | ✅ Privado  |
| DELETE | `/tasks/delete/{id}` | Eliminar tarea por ID      | ✅ Privado  |

### 👤 Usuarios

| Método | Ruta            | Descripción               | Protección |
| ------ | --------------- | ------------------------- | ---------- |
| POST   | `/users/create` | Crear usuario (admin)     | ✅ Privado  |
| GET    | `/users`        | Listar todos los usuarios | ✅ Privado  |

## 📄 Documentación automática

FastAPI genera automáticamente documentación interactiva:

* Swagger UI: [`http://localhost:8000/docs`](http://localhost:8000/docs)
* ReDoc: [`http://localhost:8000/redoc`](http://localhost:8000/redoc)

## 📦 Estructura del proyecto

```
app/
│
├── main.py            # Punto de entrada principal
├── models/            # Modelos SQLAlchemy
├── schemas/           # Esquemas Pydantic
├── crud/              # Operaciones de base de datos
├── routes/            # Rutas protegidas y públicas
├── auth/              # Lógica de autenticación y seguridad
├── core/              # Configuración y utilidades generales
└── database/          # Conexión y setup de la base de datos
```

## ✅ Estado del Proyecto

✔️ Autenticación JWT implementada
✔️ Encriptación de contraseñas con bcrypt
✔️ Protección de rutas privadas
✔️ Gestión de tareas y usuarios funcional
✔️ Arquitectura modular y escalable

## 💡 Próximas mejoras (ideas)

* 👥 Roles y permisos de usuario (admin/user)
* 📩 Notificaciones por email
* 📱 Versión móvil del frontend
* 🔍 Filtros y búsquedas para tareas

## 👨‍💻 Autor

**Yeison Andrés Marroquín Bernal (Andres.dev)**
*Desarrollador Full Stack*

