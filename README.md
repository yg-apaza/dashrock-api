# DashRock

> **URL de la API en Cloud Run: https://dashrock-api-ffsw7gfw5q-uc.a.run.app**
>
> **Documentacion de la API aqui: https://www.postman.com/test2gh/workspace/rocket/collection/247432-1075857e-1548-4e3b-a2c1-e4478cc2d560?action=share&creator=247432**

## Requerimientos

- Python 3.8 o superior
- VS Code o su IDE favorito
- Postman y una cuenta en Postman. Unirse [aqui](https://app.getpostman.com/join-team?invite_code=c4b0075a6d44af142ae2eb28f274aba7&target_code=a2ce38ed2a0b30522c0a3b9a356cf414)
- [GCloud CLI](https://cloud.google.com/sdk/docs/install)

## Instalar (Entorno de desarrollo)

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install --upgrade pip`
4. `pip install -r requirements.txt`
5. Copiar archivo `.env` dentro de `/app`, se debe llamar exactamente `.env`
6. Sigue las indicaciones en la seccion [Authentication > If you're developing locally](https://googleapis.dev/python/google-api-core/latest/auth.html) para autenticarte localmente con GCP

Finalmente ejecutar `python main.py`

## Deployar con Cloud Run (Entorno de produccion)

El archivo Dockerfile se puede construir y ejecutar con:

- `docker image build -t dashrock-api:1.0.0 .`
- `docker run dashrock-api:1.0.0`

En Google Cloud Run funciona ya que las credenciales estan precargadas. Para hacer un deploy, ejecutar:

```
gcloud run deploy --set-env-vars "GCP_PROJECT=" --set-env-vars "GCP_DATASET=" --set-env-vars "SECRET_KEY=" --set-env-vars "^@^BACKEND_CORS_ORIGINS=" --set-env-vars "PRODUCTION=true"
```

## Notas adicionales

### Agregar nueva variable de entorno

- Para agregar una nueva variable de entorno en entorno de de desarrollo local editar el archivo [app/settings.py](app/settings.py)
- En entorno de produccion deployar y agregar la nueva variable:
```
gcloud run deploy --set-env-vars "NUEVA_VARIABLE=value" 
```

Las variables de entorno añadidas se vuelven a reagregar en el siguiente deploy, por lo que solo es necesario setear las variables una vez.

### Debugging

- Agregar breakpoint: `import ipdb; ipdb.set_trace()`
- `c`: continuar
- `n`: siguiente linea
- `s`: entrar dentro de funcion
- `q`: quit, salir de ipdb

### Migraciones de la BD

1. `alembic revision --autogenerate -m "Migration message"`
2. `alembic upgrade head`