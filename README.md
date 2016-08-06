# python_wsgi_server

# Heroku upload

  1. $ pip freeze > requirements.txt
  2. $ echo "web: gunicorn server:api" > Procfile
  3. $ git add . && git commit -m "Procfile adn requirements.txt updated"
  4. $ heroku create
