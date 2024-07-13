import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from skin_cancer.utils.utils import get_logger

def create_split_data(csv_path: str, test_split_ratio: float = 0.1, val_split_ratio: float = 0.2)-> None:
    logger = get_logger(Path(__file__).name)
    
    
    df = pd.read_csv(f"{csv_path}metadata.csv")
    
    
    df_train, df_test = train_test_split(df, test_size=test_split_ratio, random_state=42, stratify=df["target"])
    logger.info(f"Splitted train and test data:{df_train.shape=}, {df_test.shape=}")
    df_train, df_val = train_test_split(df_train, test_size=val_split_ratio, random_state=42, stratify=df_train["target"])
    logger.info(f"Splitted train and val data:{df_train.shape=}, {df_val.shape=}")
    
    df_train.to_csv(f"{csv_path}train-metadata.csv")
    df_val.to_csv(f"{csv_path}val-metadata.csv")
    df_test.to_csv(f"{csv_path}test-metadata.csv")
    
    logger.info(f"saved train, val and test data under {csv_path}.")
    
    