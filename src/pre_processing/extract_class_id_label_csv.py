import pandas as pd
import os
import argparse

def extract_class(class_ids, meta_data_path, save_data_path):
  """Extract subset of classes from full dataset

  Parameters:
  class_ids (list of int): class ids to extract from dataset
  meta_data_path (str): path to SignList_ClassId_TR_EN.csv that has complete dataset
  save_data_dir (str): path to directory to save the filtered dataframe

  """
  df = pd.read_csv(meta_data_path)
  df = df[df["ClassId"].isin(class_ids)]
  df.reset_index(inplace=True, drop=True)
  if save_data_dir and not os.path.exists(save_data_dir):
    os.mkdir(save_data_dir)
  df.to_csv(save_data_dir + "/SignList_ClassId_TR_EN.csv", index=False)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-c", "--class_ids", nargs="+", help="class ids to extract", type=int)
  args = parser.parse_args()
  class_ids = args.class_ids
  meta_data_path = "../../data/complete/SignList_ClassId_TR_EN.csv"
  save_data_dir = "../../data/{}_class".format(len(class_ids))
  extract_class(class_ids, meta_data_path, save_data_dir)