.PHONY: download-model-light
download-model-light:
	wget -O checkpoints/SOLOv2_LIGHT_448_R18_3x.pth 'https://cloudstor.aarnet.edu.au/plus/s/HwHys05haPvNyAY/download'
	
.PHONY: download-model-heavy
download-model-heavy:
	wget -O checkpoints/SOLOv2_R50_3x.pth 'https://cloudstor.aarnet.edu.au/plus/s/nkxN1FipqkbfoKX/download'

.PHONY: build-docker-base
build-docker-base:
	docker build -t solo -f docker/Dockerfile.base .

.PHONY: build-docker-train
build-docker-train:
	docker build -t solo-train -f docker/Dockerfile.train .
		
.PHONY: run-docker-train
run-docker-train:
	docker run --gpus all --rm --shm-size 8G --name solo-train -v $${PWD}/work_dirs:/SOLO/work_dirs solo-train:latest
	
.PHONY: run-docker-interact
run-docker-interact:
	docker run --gpus all -it -v $${PWD}/work_dirs:/SOLO/work_dirs solo-train:latest bash
