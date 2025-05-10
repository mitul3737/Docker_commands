# Build the image
docker build -t <your-github-userid>/flask-mysql-app .

# Log in to Docker Hub
docker login

# Push to Docker Hub
docker push <your-github-userid>/flask-mysql-app
