TRAVIS_REPO_SLUG ?= fernandoe/fe-ortopedica-api
TAG ?= local

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

ci.test:
	docker run --rm -it '${TRAVIS_REPO_SLUG}:${TAG}' pytest -s || true
