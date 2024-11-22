import requests

class TestFuncionarios():
    url_base_funcionarios = 'http://localhost:8000/api/v1/funcionarios/'
    novo_funcionario = {
            'nome' : 'Fulano',
            'cpf' : '12345678910',
            'email' : 'mail@mail.com',
            'cargo' : 'Estag',
            'meta' : '10'
        }
    header_auth = {'Authorization':'Token Token_numero'}
    def test_get_funcionarios(self):
        resposta =  requests.get(url= self.url_base_funcionarios)
        assert resposta.status_code == 200
    
    def test_post_funcionarios_sem_auth(self):        
        request_test = requests.post(url=self.url_base_funcionarios, data=self.novo_funcionario)
        assert request_test.status_code == 403

    def test_post_funcionario_com_auth(self):
        request_test= requests.post(url=self.url_base_funcionarios, headers=self.header_auth, data=self.novo_funcionario)
        assert request_test.status_code == 201