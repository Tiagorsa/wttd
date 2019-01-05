# wttd

Turma WTTD - Dezembro 2018

Exercicio Eventex

cd wtdd
python -m venv .wttd
source .wttd/bin/activate
pip -install -r requirements-dev.txt
cd contrib/env-sample .env
python manage.py test

#Como fazer o deploy
1. Crie uma instância no Heroku
2. Envie as configurações para o Heorku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o Heroku

heroku create <minhainstancia>
heroku config:push
heroku config:set SECRET_KEY='<new scret key>'
heroku config:set DEBUG=False
git push heroku master --force
