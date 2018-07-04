from api import api
from api.views.auth import Auth

api.add_url_rule('/register', methods=['POST'], view_func=Auth.register, strict_slashes=False)
api.add_url_rule('/login', methods=['POST'], view_func=Auth.login, strict_slashes=False)
