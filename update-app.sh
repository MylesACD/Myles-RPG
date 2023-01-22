git pull origin
docker-compose -f docker-compose-prod.yml build app
docker-compose -f docker-compose-prod.yml up --no-deps -d app