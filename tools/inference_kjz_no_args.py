from mmdet.apis import init_detector, inference_detector, show_result_pyplot, show_result_ins
import mmcv


config='configs/fish_solov2_r50_fpn_8gpu_3x_v2.py'
checkpoint='/SOLO/work_dirs/solov2_release_r50_fpn_8gpu_3x_v2/epoch_50.pth'
img='data/fish/image_set/2022-08-31-16-04-34.jpg'
img_out='work_dirs/2022-08-31-16-04-34_annotated.jpg'

# build the model from a config file and a checkpoint file
model = init_detector(config, checkpoint, device='cuda:0')

# test a single image
result = inference_detector(model, img)
show_result_ins(img, result, model.CLASSES, score_thr=0.25, out_file=img_out)


