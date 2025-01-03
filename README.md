#MedicSearch
MedicSearch é uma aplicação web desenvolvida com Django para busca e gerenciamento de profissionais médicos. Este projeto foi criado como parte do aprendizado do livro "Django de A a Z".

Funcionalidades
Cadastro e autenticação de usuários
Busca de médicos por especialidade e localização
Perfis de médicos com informações detalhadas
Sistema de avaliação e comentários
Agendamento de consultas (futura implementação)
Tecnologias Utilizadas
Python 3.x
Django 3.x
SQLite (banco de dados padrão)
HTML, CSS, JavaScript
Bootstrap para front-end
Instalação
Clone o repositório:
git clone https://github.com/seu-usuario/MedicSearch.git

Entre no diretório do projeto:
cd MedicSearch

Crie um ambiente virtual e ative-o:
python -m venv venv

source venv/bin/activate # No Windows use venv\Scripts\activate

Instale as dependências:
pip install -r requirements.txt

Execute as migrações:
python manage.py migrate

Crie um superusuário:
python manage.py createsuperuser

Inicie o servidor de desenvolvimento:
python manage.py runserver

Uso
Após iniciar o servidor, acesse http://localhost:8000 em seu navegador. Use as credenciais do superusuário para acessar o painel de administração em http://localhost:8000/admin/.

Estrutura do Projeto
medicSearch/: Aplicação principal
profiles/: Gerenciamento de perfis de usuários
ratings/: Sistema de avaliações
appointments/: Sistema de agendamentos (futura implementação)
Contribuição
Contribuições são bem-vindas! Por favor, leia o arquivo CONTRIBUTING.md para detalhes sobre nosso código de conduta e o processo para enviar pull requests.

Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE.md para detalhes.

Agradecimentos
Autor do livro "Django de A a Z" por fornecer a base de conhecimento para este projeto.
Comunidade Django por recursos e suporte contínuos.