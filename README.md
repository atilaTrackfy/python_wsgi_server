# python_wsgi_server

# Heroku upload

  1. $ pip freeze > requirements.txt
  2. $ echo "web: gunicorn server:api" > Procfile
  3. $ git add . && git commit -m "Procfile adn requirements.txt updated"
  4. $ heroku create
  5. $ git push heroku master

# API Test
  
  - Get:  curl http://xxxxxx/myself
  - Post: curl curl -H 'Content-Type:application/json' -d "{\"name\":\"koma\",\"age\":\"27\"}" http://xxxxxx/myself
