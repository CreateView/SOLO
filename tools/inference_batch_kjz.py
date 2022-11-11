from mmdet.apis import init_detector, inference_detector, show_result_pyplot, show_result_ins
import mmcv
import argparse
import glob, os


def parse_args():
    parser = argparse.ArgumentParser(description='MMDet test detector')
    parser.add_argument('config', help='test config file path')
    parser.add_argument('checkpoint', help='checkpoint file')
    parser.add_argument('--img-path', help='image dir')
    parser.add_argument('--output-dir', help='output image dir')
    args = parser.parse_args()
    return args

args = parse_args()


if not os.path.isdir(args.output_dir):	
    os.makedirs(args.output_dir)

imgs = glob.glob(args.img_path + '/*.jpg')

# build the model from a config file and a checkpoint file
model = init_detector(args.config, args.checkpoint, device='cuda:0')

for img in imgs:
    new_image_name = os.path.join(args.output_dir, os.path.basename(img)) 
    result = inference_detector(model, img)
    show_result_ins(img, result, model.CLASSES, score_thr=0.25, out_file=new_image_name)
    print('image written:', new_image_name)


