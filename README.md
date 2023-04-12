# Fake ServiceNow API

The purpose of this application is to simulate the ServiceNow API for development and testing purposes. You can use this application to mimic the behavior of the ServiceNow API without needing to connect to a real ServiceNow instance.

## Endpoints

The following endpoints are available in this application:

1. **GET /az/business_services**: This endpoint returns the list of Business Services along with their associated Business Group.

## Setup and Installation

Follow these steps to set up the application:

1. Create a virtual environment:

```
python3 -m venv env
```

2. Activate the virtual environment:

- On Linux or macOS:

  ```
  source env/bin/activate
  ```

- On Windows:

  ```
  .\env\Scripts\activate
  ```

3. Install the dependencies from the `requirements.txt` file:

```
pip install -r requirements.txt
```

4. Run the application:

```
uvicorn main:app --reload
```

Now, the application should be running on `http://127.0.0.1:8000/`.
