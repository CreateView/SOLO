from mmdet.apis import init_detector, inference_detector, show_result_pyplot, show_result_ins
import mmcv
import argparse
import glob, os

config='configs/fish_solov2_r50_fpn_8gpu_3x_v2.py'
checkpoint='/SOLO/work_dirs/solov2_release_r50_fpn_8gpu_3x_v2/epoch_50.pth'
img_path='data/fish-test'
output_dir='work_dirs/test-inference'

if not os.path.isdir(output_dir):	
    os.makedirs(output_dir)

# build the model from a config file and a checkpoint file
model = init_detector(config, checkpoint, device='cuda:0')

imgs = glob.glob(img_path + '/*.jpg')

for img in imgs:
    new_image_name = os.path.join(output_dir, os.path.basename(img)) 
    result = inference_detector(model, img)
    show_result_ins(img, result, model.CLASSES, score_thr=0.25, out_file=new_image_name)
    print('image written:', new_image_name)
