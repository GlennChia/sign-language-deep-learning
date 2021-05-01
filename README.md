# Sign Language Deep Learning project

# 1. Table of contents <a name="TOC"></a>

1. [Table of contents](#TOC)
2. [Directory structure](#DS)
3. [Running the code](#INSTRUCTIONS)

# 2. Directory structure <a name="DS"></a>

# 3. Running the code <a name="INSTRUCTIONS"></a>

## 3.1 Setting up Python environment

1. Configure python environment
   ```bash
   python -m venv venv
   ```
2. Activate the environment
   ```bash
   venv\Scripts\activate
   ```
3. Install required packages
   ```bash
   pip install -r requirements.txt
   ```

## 3.2 Setting up Conda environment

1. configure the conda enviornment
   ```bash
   conda env create -f environment.yml
   ```
2. To use environment
   ```bash
   conda activate sign-language-dl
   ```
3. Open jupyter noteboook
   ```bash
   jupyter-notebook
   ```
4. To exit environment
   ```bash
   conda deactivate
   ```
5. To destroy envionment
   ```bash
   conda info --envs
   conda env remove --name sign-language-dl
   ```

## 3.3 Pre-processing

The full dataset consists of 225 classes. To decrease the time taken to train and make the problem easier to tackle, reduce the number of classes to a specified amount.

First extract the class IDs and their label mappings

```bash
cd ./src/pre_processing
python extract_class_id_label_csv.py -c 169 24 208
```

Then extract a subset of classes from the train, val, and test

```bash
cd ./src/pre_processing
python extract_class_dataset_csv.py -c 169 24 208
```

Then copy the subset of the dataset to the new directory

```bash
cd ./src/pre_processing
python copy_dataset_files.py
```
