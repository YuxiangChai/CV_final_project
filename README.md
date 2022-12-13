# Final Project

## Dataset

We use the dataset called PIDray. More information can be found [here](https://github.com/bywang2018/security-dataset).

Original dataset is in COCO format. If you want to run YOLOV5 on this dataset, please convert it to YOLOV5 format, which can be found [here](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data).

PS: you can use `convert.py` to convert the format.

## Train models

### YOLOV5

Install the required packages in `yolov5/requirements.txt`.

Modify the config file in `yolov5/data/xray.yaml`.

And you can directly run the following commands to train a simple model.

```bash
$ cd yolov5
$ python train.py --cos-lr
```

Or you can follow the tutorials in [YOLOV5 official GitHub Repo](https://github.com/ultralytics/yolov5).

### Faster RCNN & Sparse RCNN

Install `mmdetection` developer version following the [tutorial](https://mmdetection.readthedocs.io/en/latest/get_started.html#installation)

Run the following commands to train a model.

```bash
$ cd configs
$ python path/to/mmdetection/tools/train.py [model_config.py]
```

`[model_config.py]` means any config file in the `configs/` folder.

For more information, please refer to [official MMDetection GitHub Repo](https://github.com/open-mmlab/mmdetection/tree/e71b499608e9c3ccd4211e7c815fa20eeedf18a2).

## Evaludate models

### YOLOV5

```bash
$ cd yolov5
$ python val.py
```

### Faster RCNN & Sparse RCNN

```bash
$ cd configs
$ python path/to/mmdetection/tools/test.py [model_config.py] [model.pth] --eval bbox
```

`[model_config.py]` means any config file in the `configs/` folder.

`[model.pth]` means any checkpoint saved in the work directory.

## Report

Please review `report.pdf`