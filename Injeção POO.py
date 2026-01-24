class EmailService:

    def enviar(self, msg):
        print('Enviando email: {}'.format(msg))

class Usuario:
    def __init__(self,servicoInjetado):
        self.servicoInjetado = servicoInjetado

    def mandaremail(self):
        self.servicoInjetado.enviar("Olá, tudo bem?")

servico = EmailService()
usuario = Usuario(servico)
usuario.mandaremail()