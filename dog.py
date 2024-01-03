import yaml

dataset_info = {
  "train": "./train/images", 
  "val": "./val/images",
  "nc": 1,
  "names": ["Dog"]
}

yaml_savepath = 'D:\AI project\human_detection_dataset\data.yaml'
with open(yaml_savepath, 'w') as f:
  doc = yaml.dump(
    dataset_info,
    f,
    default_flow_style=None,
    sort_keys=False,
  )
