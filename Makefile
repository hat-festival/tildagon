APP = $(shell basename $$(pwd))

build:
	docker build \
		--build-arg APP=${APP} \
		--tag ${APP} .

run:
	docker run \
		--name ${APP} \
		--hostname ${APP} \
		--volume $(shell pwd):/opt/${APP} \
		--interactive \
		--tty \
		--rm \
		${APP} \
		bash
