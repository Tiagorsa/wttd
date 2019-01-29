# wttd

Turma WTTD - Dezembro 2018

[![Build Status](https://www.travis-ci.org/Tiagorsa/wttd.svg?branch=master)](https://www.travis-ci.org/Tiagorsa/wttd)

Exercicio Eventex

#Comandos ativar develop<br>
cd wtdd<br>
python -m venv .wttd<br>
source .wttd/bin/activate<br>
pip install -r requirements-dev.txt<br>
cp contrib/env-sample .env<br>
python manage.py test<br>
heroku git:remote -a eventex-tiagosa<br>
<br>
#Como fazer o deploy<br>
1. Crie uma instância no Heroku <br>
2. Envie as configurações para o Heorku <br>
3. Defina uma SECRET_KEY segura para a instância <br>
3.1. $ manage generate_secret_key <br>
3.2. $ manage migrate <br>
3.3. $ manage createsuperuser <br>
4. Defina DEBUG=False <br>
5. Configure o serviço de email <br>
6. Envie o código para o Heroku <br>

heroku create <minhainstancia> <br>
heroku config:push <br>
manage generate_secret_key <br>
heroku config:set SECRET_KEY = "new scret key" <br>
heroku config:set DEBUG = False <br>
git push heroku master --force <br>
