# Fake ServiceNow API con Webhook

El propósito de esta aplicación es simular la API de ServiceNow para fines de desarrollo y pruebas. Puedes utilizar esta aplicación para imitar el comportamiento de la API de ServiceNow sin necesidad de conectarte a una instancia real de ServiceNow. La aplicación envía automáticamente los nuevos tickets generados y los Business Services y Business Groups existentes a un webhook.

## Endpoints

Los siguientes endpoints están disponibles en esta aplicación:

1. **GET /az/tickets/**: Este endpoint devuelve la lista de todos los tickets.

## Webhook

El webhook se activa cada vez que se generan nuevos tickets o se actualizan los Business Services o Business Groups existentes. La función `post_updated_tickets` en el archivo `main.py` se encarga de enviar los datos al webhook.

Asegúrate de reemplazar la URL en la variable `url` en la función `post_updated_tickets` con la URL de tu endpoint en az-watch.

## Configuración e instalación

Sigue estos pasos para configurar la aplicación:

1. Crea un entorno virtual:

```
python3 -m venv env
```

2. Activa el entorno virtual:

- En Linux o macOS:
```
source env/bin/activate
```

- En Windows:
```
.\env\Scripts\activate
```

3. Instala las dependencias del archivo `requirements.txt`:
```
pip install -r requirements.txt
```

4. Ejecuta la aplicación:
```
uvicorn main:app --reload
```

Ahora, la aplicación debería estar ejecutándose en `http://127.0.0.1:8000/`.
