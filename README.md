# wttd

Turma WTTD - Dezembro 2018

[![Build Status](https://www.travis-ci.org/Tiagorsa/wttd.svg?branch=master)](https://www.travis-ci.org/Tiagorsa/wttd)

Exercicio Eventex

#Comandos ativar develop
cd wtdd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
heroku git:remote -a eventex-tiagosa

#Como fazer o deploy
1. Crie uma instância no Heroku
2. Envie as configurações para o Heorku
3. Defina uma SECRET_KEY segura para a instância
3.1. $ manage generate_secret_key 
3.2. $ manage migrate
3.3. $ manage createsuperuser
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o Heroku

heroku create <minhainstancia>
heroku config:push
heroku config:set SECRET_KEY='<new scret key>'
heroku config:set DEBUG=False
git push heroku master --force
