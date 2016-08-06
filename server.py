# server.py
import falcon
import json

class Me:
  def on_get(self, req, res):
    """Handles GET requests"""
    me = {
      'name': 'Falcon API',
      'age': '1 month old',
    }
    res.body = json.dumps(me)

class You:
  def on_post(self, req, res):
    """Handles POST requests"""
    body = req.stream.read()
    req_params = json.loads(body.decode('utf-8'))
    you = {
      name: req_params['name'],
      age:  req_params['age'],
    }
    res.body = json.dumps(you)

api = falcon.API()

api.add_route('/myself', Me())
api.add_route('/yourself', You())

