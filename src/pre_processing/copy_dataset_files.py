from shutil import copyfile
import pandas as pd
import os
import argparse

def copy_data(source_dir, video_name, save_dir):
  """Copy video data from the source_dir to save_dir

  Parameters:
  source_dir (str): path to the video source
  video_name (str): name of the video to copy
  save_dir (str): path to the directory to copy the videos

  """
  if save_dir and not os.path.exists(save_dir):
    os.mkdir(save_dir)
  video_formats = ["color", "depth"]
  for video_format in video_formats:
    copyfile("{}/{}_{}.mp4".format(source_dir, video_name, video_format),
             "{}/{}_{}.mp4".format(save_dir, video_name, video_format))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-c", "--num_classes", help="number of classes to copy", type=int)
  args = parser.parse_args()
  num_classes = args.num_classes
  dataset_details = {
    "train": "train_labels",
    "val": "val_ground_truth",
    "test": "test_ground_truth",
  }
  for dataset, dataset_name in dataset_details.items():
    source_dir = "../../data/complete/{}".format(dataset)
    save_dir = "../../data/{}_class/{}".format(num_classes, dataset)
    df = pd.read_csv("../../data/{}_class/{}.csv".format(num_classes, dataset_name), names=["video_name", "class_id"])
    df.apply(lambda row : copy_data(source_dir, row['video_name'], save_dir), axis = 1)