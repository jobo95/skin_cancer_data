from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass


@dataclass
class Config:
    dvc_remote_name: str = "gcs-storage"
    dvc_remote_url: str = "gs://skincancerjo/data/raw"
    dvc_raw_data_folder: str = "data/raw"

    csv_path: str = "/app/data/raw/isic-2024-plus-2018-2020-malign/"
    test_split_ratio: float = 0.1
    val_split_ratio: float = 0.2

def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)
