import json
from tqdm import tqdm


def get_image_names(images):
    dic = {}
    for img in images:
        dic[img['id']] = {'height': img['height'], 'width': img['width'], 'file_name': img['file_name']}
    return dic


def norm(bbox, width, height):
    x_c = bbox[0] + bbox[2] / 2.0
    y_c = bbox[1] + bbox[3] / 2.0
    return [x_c / (1.0*width), y_c / (1.0*height), bbox[2] / (1.0*width), bbox[3] / (1.0*height)]


def convert(path):
    with open(path, 'r') as f:
        origin_data = json.load(f)
    annotations = origin_data['annotations']
    images = origin_data['images']
    categories = origin_data['categories']
    
    image_dict = get_image_names(images)
    # category id to class num
    id2class = {p['id']: p['name'] for p in categories}
    
    image_anno = {}
    for i, anno in enumerate(annotations):
        image_id = anno['image_id']
        category = anno['category_id']
        bbox = anno['bbox']     # xywh
        width = image_dict[image_id]['width']
        height = image_dict[image_id]['height']
        image_name = image_dict[image_id]['file_name']
        norm_bbox = norm(bbox, width, height)
        instance = [category-1, *norm_bbox]
        temp_anno = image_anno.get(image_id, [])
        temp_anno.append(instance)
        image_anno[image_name] = temp_anno

    for k, v in tqdm(image_anno.items()):
        txt_name = k.replace('.png', '.txt')
        with open('labels/train/'+txt_name, 'w') as f:
            for line in v:
                f.write('{} {} {} {} {}\n'.format(line[0], line[1], line[2], line[3], line[4]))


if __name__ == '__main__':
    convert('annotations/xray_train.json')