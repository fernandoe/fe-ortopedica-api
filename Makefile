TRAVIS_REPO_SLUG ?= fernandoe/fe-ortopedica-api
TAG ?= local

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

ci.test:
	docker run --rm \
		-e TRAVIS_JOB_ID='${TRAVIS_JOB_ID}' \
		-e TRAVIS_BRANCH='${TRAVIS_BRANCH}' \
		-e COVERALLS_REPO_TOKEN='${COVERALLS_REPO_TOKEN}' \
		-e CODECOV_ENV='${CODECOV_ENV}' \
		-it '${TRAVIS_REPO_SLUG}:${TAG}' /bin/sh -c "pytest -s; coveralls; codecov; env"
