impori flask  import  Flask
import secrets

class MyApp()
def __init__(self):
        self.app= flask   (__name__, template_folder='templates', static_folder='viwews/templetes', static_folder='views/static')
        self.app.config['SECRET_KEY'] = secrets.token_hex(16)


        from controllers.auth.routs import auth_blueprint
        from controllers.main.routs import main_blueprint



        def run(self):
                return self.app.run(debug=True