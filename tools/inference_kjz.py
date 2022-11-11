from mmdet.apis import init_detector, inference_detector, show_result_pyplot, show_result_ins
import mmcv
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='MMDet test detector')
    parser.add_argument('config', help='test config file path')
    parser.add_argument('checkpoint', help='checkpoint file')
    parser.add_argument('--img', help='image')
    parser.add_argument('--img-out', help='output image')
    args = parser.parse_args()
    return args

args = parse_args()

# build the model from a config file and a checkpoint file
model = init_detector(args.config, args.checkpoint, device='cuda:0')

# test a single image
result = inference_detector(model, args.img)
show_result_ins(args.img, result, model.CLASSES, score_thr=0.25, out_file=args.img_out)


