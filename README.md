# Default
Convierte CSV to XLSX


Requiere
- pipenv install pandas
- pipenv install openpyxl


# ejecutar con python
pipenv shell
cd src
python main.py

# ejectura con docker
docker build -t matiasfranci/hello-cloud .
docker run -it matiasfranci/hello-cloud:latest .

# ejecutar con docker-compose
docker-compose up -d

# docker push
docker push matiasfranci/hello-cloud:latest

# ejecutar con kubectl
kubectl apply -f job.yml