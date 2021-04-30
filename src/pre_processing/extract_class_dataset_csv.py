import pandas as pd
import os
import argparse

def extract_class(class_ids, dataset_path, save_data_dir, save_data_file):
  """Extract subset of classes from full dataset of either train, val, or test

  Parameters:
  class_ids (list of int): class ids to extract from dataset
  dataset_path (str): path to train, test, val csvs
  save_data_dir (str): path to directory to save the new csvs
  save_data_file (str): name of the csv file to save

  """
  df = pd.read_csv(dataset_path, names=["video_name", "class_id"])
  df = df[df['class_id'].isin(class_ids)]
  if save_data_dir and not os.path.exists(save_data_dir):
    os.mkdir(save_data_dir)
  df.to_csv("{}/{}.csv".format(save_data_dir, save_data_file), index=False, header=False)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-c", "--class_ids", nargs="+", help="class ids to extract", type=int)
  args = parser.parse_args()
  class_ids = args.class_ids
  dataset_names = ["train_labels", "val_ground_truth", "test_ground_truth"]
  save_data_dir = "../../data/{}_class".format(len(class_ids))
  for dataset_name in dataset_names:
    dataset_path = "../../data/complete/{}.csv".format(dataset_name)
    extract_class(class_ids, dataset_path, save_data_dir, dataset_name)