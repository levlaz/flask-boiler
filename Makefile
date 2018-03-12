## help		: Display this help and exit.
.PHONY: help
help: Makefile
	@sed -n 's/^##//p' $<

## deps 	: Install python dependencies including development
.PHONY: deps
deps:
	pipenv install --dev

## docs		: Generate sphinx documentation.
.PHONY: docs
docs:
	$(MAKE) -C docs html

## docker 	: Build new docker container.
.PHONY: docker
docker:
	docker build . -t #CHANGEME

## run 		: Run the Flask application.
.PHONY: run
run:
	export FLASK_APP=run.py && \
	export FLASK_DEBUG=true && \
	flask run --host=0.0.0.0

## run-docker	: Run latest docker image.
.PHONY: run-docker
run-docker:
	docker run -it -p 5000:5000 #CHANGEME

## test		: Run test suite.
.PHONY: test
test:
	coverage run -m unittest discover tests