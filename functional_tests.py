from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def test_can_start_a_list_and_retrieve_it_later(self): 
    
        self.browser = webdriver.Firefox()
    
        # Maria decidiu utilizar o novo app TODO. Ela entra em sua pagina principal:
        self.browser.get('http://localhost:8000')

        # Ela nota que o titulo da pagina menciona TODO
        self.assertIn('To-Do', self.browser.title)

        # Ela e convidada a entrar com um item TODO imediatamente

        # Ela digita "Estudar testes funcionais" em uma caixa de texto

        # Quando ela aperta enter, a pagina atualiza, e mostra a lista
        # "1: Estudar testes funcionais" como um item da lista TODO
        
        # Ainda existe uma caixa de texto convidando para adicionar outro item
        # Ela digita: "Estudar testes de unidade"

        # A pagina atualiza novamente, e agora mostra ambos os itens na sua lista

        # Maria se pergunta se o site vai lembrar da sua lista. Entao, ela verifica que
        # o site gerou uma URL unica para ela -- existe uma explicacao sobre essa feature

        # Ela visita a URL: a sua lista TODO ainda esta armazenada

        # Satisfeita, ela vai dormir
        
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()