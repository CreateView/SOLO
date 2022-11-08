.PHONY: download-model
download-model:
	wget -O checkpoints/SOLOv2_LIGHT_448_R18_3x.pth 'https://cloudstor.aarnet.edu.au/plus/s/HwHys05haPvNyAY/download'

.PHONY: build-docker-base
build-docker-base:
	docker build -t solo -f docker/Dockerfile .

.PHONY: build-docker
build-docker:
	docker build -t solo-prod -f docker/Dockerfile.production .
	
.PHONY: run-docker
run-docker:
	docker run --gpus all --rm --shm-size 8G --name solo-prod -v $${PWD}/work_dirs:/SOLO/work_dirs solo-prod:latest
	
.PHONY: stop-rm
stop-rm:	
	docker stop solo-prod
	docker rm solo-prod
