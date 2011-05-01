from registration.backends.default import DefaultBackend

class Web2Backend(DefaultBackend):
    """ Like default, except:
        1. Requires only email and password (email is username)
        2. ReCaptcha
    """
    def register(self, request, **kwargs):
        email, password = kwargs['email'], kwargs['password1']
        super(Web2Backend, self).__init__(username=email, *args, **kwargs)