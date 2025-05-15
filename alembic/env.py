from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
#Importacion Para cargar variables del archivo .env. Así no metemos datos sensibles en el código.
import os
from dotenv import load_dotenv

# Importamos la clase Base que es la base (valga la redundancia 😅) de todos los modelos.
from app.db.base_class import Base

# Cargar los modelos aca
from app.models.user import User
from app.models.task import Task


# Con esto colocamos lo que nos viene en el .env a el archivo alembic.ini en la variable sqlalchemy.url
# osea cargamos la variable DATABASE_URL desde el .env y la usamos para darle la URL de conexión a Alembic.
load_dotenv()
config = context.config
config.set_main_option('sqlalchemy.url', os.environ.get('DATABASE_URL'))



if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# aca nos venimos 
target_metadata = Base.metadata



def run_migrations_offline() -> None:


    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
