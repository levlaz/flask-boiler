# flask-boiler
Boilerplate for Flask Projects

For use with latest flask and python 3.6

## Usage

1. Find all the instances of #CHANGEME and add the name of your project.
2. Optionally rename the app folder to be the name of your application.
3. Create a new pipenv `pipenv --python 3.6`
3. Install python depenencies with `make deps`
4. Run your application using `make run`
5. Run tests with `make test`

## Makefile

Handy Makefile to make all of the below dead simple.

## Dependency Management

This uses [pipenv](https://github.com/pypa/pipenv) to manage dependencies.

## app

The app directory contains code for your application.

The app uses the [factory pattern](http://flask.pocoo.org/docs/0.12/patterns/appfactories/).


## Docs

Uses [sphinx](http://www.sphinx-doc.org/en/master/) to generate documentation for a project.

Follow these steps to quickly get started:

```
cd docs
sphinx-quickstart
```

Enter the information for your project.

If you want to use the autodoc feature of sphinx be sure to update the generated `conf.py` file and append the path to your source code.

```
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__name__), '..'))
```

## Tests

Uses the built in unit test library in python to run tests. Has some boilerplate tests in place to get you started.

You can run the tests with `make test`

## Code Coverage

Uses the coverage library to create code coverage reports.

Code coverage happens automatically when you run the tests. To generate a report you can run `coverage html`.

If you use CircleCI (below) then the coverage reports will be stored as artficats of your build.

## Continuous Integration

Ready to go configuration for using python with CircleCI 2.0.

## Docker

Ready to go Dockerfile for packaging up your application in a container.

Change the Makefile from `#CHANGEME` to a name for your docker image. (i.e `org/repo`)

You can then run `make docker` to build the image and `make docker-run` to run the image. You can go to `localhost:5000` in your browser once its running to see your app.
