# Ecommerce Flask

---

## Recursos

### Contenido de archivo .env

```py
FLASK_APP='main.py'
FLASK_DEBUG=True
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000
ENVIRONMENT='development'

DATABASE_URL='postgresql://postgres:mysql@localhost:5432/flask_boilerplate'

JWT_SECRET='tecsup'

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=''
MAIL_PASSWORD=''

AWS_ACCESS_KEY_ID=''
AWS_ACCESS_KEY_SECRET=''
AWS_REGION=''

MERCADOPAGO_MAIN_ACCESS_TOKEN=''
MERCADOPAGO_CHILD_ACCESS_TOKEN=''
```

### Documentación

- SQLAlchemy
  - [Metodos usados para el modelo](https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.all)
  - [Tipo de datos](https://docs.sqlalchemy.org/en/14/core/types.html)
  - [Nuevos metodos para el modelo](https://github.com/absent1706/sqlalchemy-mixins/blob/master/README.md)
- FlaskRestX
  - [Tipo de datos](https://flask-restx.readthedocs.io/en/latest/_modules/flask_restx/fields.html)
  - [Response](https://flask-restx.readthedocs.io/en/latest/marshalling.html)
  - [Request Parsing](https://flask-restx.readthedocs.io/en/latest/parsing.html)
  - [Swagger](https://flask-restx.readthedocs.io/en/latest/swagger.html)
- FlaskJWTExtended
  - [BlackList](https://flask-jwt-extended.readthedocs.io/en/stable/blocklist_and_token_revoking/)
  - [Proteccion de rutas](https://flask-jwt-extended.readthedocs.io/en/stable/optional_endpoints/)

### Conexión URI a PGSQL

```py
postgresql://usuario:password@ip_servidor:puerto/nombre_bd
```

### Migraciones

- Iniciar las migraciones (Ejecuta una sola vez)

```sh
flask db init
```

- Crear una migración (Cuando se crea un modelo nuevo o se modifica uno anterior)

```sh
flask db migrate -m "Comentario"
```

- Subir los cambios a nuestra BD

```sh
flask db upgrade
```

### Seeders

- Ejecutar todos los seeders

```sh
flask seed run
```
