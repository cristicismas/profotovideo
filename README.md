# ProFotoVideo

![Profotovideo Image](https://cristicismas.github.io/images/profotovideo.png)

### Startup

.env:

1. ALLOWED_HOSTS=localhost
2. SECRET_KEY=your_secret_key
3. DATABASE_URL=sqlite:///db.sqlite3

```sh
pipenv shell
pipenv install

python manage.py migrate
python manage.py runserver
```
