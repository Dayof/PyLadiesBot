# PyLadiesBot

Telegram Bot para gerenciar grupo do PyLadies Brasil.

## Pacotes utilizados

- Python 3.x
- Telepot 10.3

## Executar Bot

```
$ python3 main.py
```

## Ambiente de Desenvolvimento

O bot foi desenvolvido para ser executado em Python 3. Caso você queira criar uma `virtualenv` com a versão python3, execute:

```
$ virtualenv --python='<caminho para o python3>' env
$ source env/bin/activate
```

Por exemplo:

```
$ virtualenv --python='/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5' env
```

Caso você tenha ambas as versões, e o 2 seja sua versão padrão, você também pode optar por instalar no Python 3 usando:

```
$	pip3 install -r requirements.txt
```

## BotFather: crie seu próprio bot

O BotFather é o responsável pela criação de novos bots no telegram. Então, para que você possa criar seu bot, comece uma conversa com ele (@BotFather) e mande no chat o comando:

	/newbot

O BotFather vai te pedir para escolher o nome e depois o usuário do seu bot. O usuário deve sempre terminar com "bot", por exemplo: TetrisBot or tetris_bot, e precisa ser único.

Quando você criar o seu novo bot, o BotFather te retornará um token. Crie um `config.ini` seguindo o modelo do [config.ini.template](config.ini.template) para colocar o token e username do seu bot. Caso você esqueça seu token, não se preocupe, você poderá recuperá-lo com o comando `/token`.
