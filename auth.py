class AuthenticationDummy:
    def __init__(self):
        self.user = None
    
    def login(self):
        self.user = {
            'name': 'John Smith',
            'mail': 'John.Smith@solidigmtechnology.com',
            }
        
    def logout(self):
        self.user = None

auth = AuthenticationDummy()