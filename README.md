# Getting Remote Data Lab 

## Learning Goals

- Learning goal 1.

---

## Instructions

> This is a **test-driven lab**, so please fork and clone the repo.

Run `pipenv install && pipenv shell` to generate and enter your virtual
environment.

```console
$ pipenv install && pipenv shell
```

Change into the `server` directory, where you will run the application and
tests:

```console
$ cd server
```

You can run the application as a script within the `server/` directory:

```console
$ python app.py
```

If you prefer working in a Flask environment, remember to configure it with the
following commands within the `server/` directory:

```console
$ export FLASK_APP=app.py
$ export FLASK_RUN_PORT=5555
$ flask run
```

Run `pytest -x` to run your tests:

```console
$ pytest -x
```

Use these instructions and `pytest`'s error messages to complete your work.

Lab Requirements:

- Implement a Flask application with the following views.

Once all of your tests are passing, commit and push your work using `git` to
submit.

---

## Resources

- [Resource 1](https://www.python.org/doc/essays/blurb/)
- [Reused Resource][reused resource]

[reused resource]: https://docs.python.org/3/
