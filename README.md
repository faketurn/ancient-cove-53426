# Python: 始める方法

HerokuではBarebones Djangoアプリが簡単に利用できます。

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## ローカルで実行する

Pythonがインストールされているか確認してください。 [installed properly](http://install.python-guide.org) また、[Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) と [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup)をインストールしてください。

## heroku-pythonのコマンド

```sh
# herokuコマンドを利用するためにログインが必要
$ heroku login

# サーバーに保存するためのコマンド
$ git push heroku master

# サーバーを開く（ブラウザが開くコマンド）
$ heroku open

# Pipfileにアプリの依存関係が記録されています
# デプロイされると、Herokuはこのファイルを読み込み
# 適切なPythonの依存関係をインストールします。
# これをローカルで行うには、Pipenvを使用します。

# --threeオプションで、Python3を明示します。
$ pipenv --three

# 依存関係をインストールします。
$ pipenv install

# アプリをローカルで実行するためにvirtualenvを有効にします。
$ pipenv shell

# Djangoはローカルアセットを使用しているので、collectstaticを実行する必要があります。
$ pthon manage.py collectstatic

# Heroku CLIのアプリをローカルで起動します。
$ heroku local web -f Procfile.windows
# Unixの場合は
$ heroku local web

(http：// localhost：5000)[http：// localhost：5000]を開いて確認できます。

```

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pipenv install

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
