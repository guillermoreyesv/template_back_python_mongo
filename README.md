# TEMPLATE_BACK_PYTHON_MONGO

**Description:**
This is a template for create a microservice in python using fastapi + pymongo.

**Technology Stack:**
- **FastAPI:** Utilizing the power of FastAPI for fast development, automatic OpenAPI and JSON Schema generation, and high performance.
- **MongoDB:** Leveraging MongoDB as the database to store and retrieve user, event, and ticket information efficiently.


## 1. Install Virtual Environment
This command installs virtualenv, a tool to create isolated Python environments.
```
pip install virtualenv
```

## 2. Create Virtual Environment
Creates a new virtual environment named venv using Python 3. This environment will isolate dependencies for your project.
```
python3 -m venv venv
```

## 2.5 Pip freeze
Create a requirements.txt only with local libraries.
```
pip freeze --local > requirements.txt
```

## 3. Set Environment Variables
The basic syntax to define an environment variable is as follows:
```
export MONGO_USER=admin
export MONGO_PASS=adminpassword
export MONGO_HOST=localhost
export MONGO_PORT=27017
mongodb://admin:adminpassword@localhost:27017/?authMechanism=DEFAULT
```

## 4. Install Dependencies
Installs project dependencies listed in the requirements.txt file. The --no-cache-dir flag prevents the use of cached packages.
```
pip install --no-cache-dir -r requirements.txt
```

## 5. Run FastAPI using Uvicorn
Starts the FastAPI application using Uvicorn. The --reload flag enables auto-reloading on code changes, and the --port 8001 specifies the port number.
```
uvicorn main:app --reload --port 8001
```

## 6. Build Docker Image
Builds a Docker image for the project and tags it as back-template.
```
docker build -t back-template .
```

## 7. Run Docker Container
Runs a Docker container in detached mode (-d), maps port 8001 on the host to port 8000 in the container, and names the container back-template.
```
docker run -d -p 8001:8000 --name back-template back-template
```

## 8. Run Docker Compose
Uses Docker Compose to start services defined in the docker-compose.yml file in detached mode (-d).
```
docker-compose up -d
```

## 9. URL to use

BaseAPI
http://0.0.0.0:8001/

Documentation (Swagger)
http://0.0.0.0:8001/docs


## 10. View connections in mongodb
Use MongoDB Compass in CLI
```
db.serverStatus().connections
``````
