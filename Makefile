.PHONY: download-model
download-model:
	wget -O checkpoints/SOLOv2_LIGHT_448_R18_3x.pth 'https://cloudstor.aarnet.edu.au/plus/s/HwHys05haPvNyAY/download'

.PHONY: build-docker-base
build-docker-base:
	docker build -t solo -f docker/Dockerfile.base .

.PHONY: build-docker-train
build-docker-train:
	docker build -t solo-train -f docker/Dockerfile.train .
	
.PHONY: build-docker-test
build-docker-test:
	docker build -t solo-test -f docker/Dockerfile.test .
	
.PHONY: run-docker-train
run-docker-train:
	docker run --gpus all --rm --shm-size 8G --name solo-train -v $${PWD}/work_dirs:/SOLO/work_dirs solo-train:latest
	
.PHONY: run-docker-test
run-docker-test:
	docker run --gpus all --rm --name solo-test -v $${PWD}/work_dirs:/SOLO/work_dirs solo-test:latest
