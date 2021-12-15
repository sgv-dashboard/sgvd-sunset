echo '[INFO] Make sure to be logged into heroku'
heroku container:login

docker build . --tag registry.heroku.com/sgvd-sunset/web
docker push registry.heroku.com/sgvd-sunset/web
heroku container:release web --app=sgvd-sunset