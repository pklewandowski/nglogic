docker compose down -v --rmi all --remove-orphans
docker compose build --no-cache
docker compose up --force-recreate --remove-orphans