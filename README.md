# ProFotoVideo

![Profotovideo Image](https://cristicismas.github.io/images/profotovideo.png)

### Startup

.env:

```
ALLOWED_HOSTS=localhost
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3
```

setup:

```sh
pipenv shell
pipenv install

python manage.py migrate
python manage.py runserver
```
