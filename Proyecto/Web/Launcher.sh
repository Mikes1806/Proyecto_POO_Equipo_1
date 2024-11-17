
# Show env vars
grep -v '^#' .env

# Export env vars
export $(grep -v '^#' .env | xargs)

docker-compose down
docker-compose build
docker-compose up