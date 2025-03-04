"""Dataset Download Module

This module provides functions to download datasets the IroyinSpeech dataset.

Functions:
- download_dataset(url: str, destination: str):
  Downloads a dataset from the given URL to the specified destination directory.
- main - the main function to run the script

Usage:
    To download the dataset, run the script directly.

Example:
    $ python src/download_dataset.py

"""

import os

import opendatasets as opd
from loguru import logger

URL_ = "https://www.kaggle.com/datasets/rileydrizzy/iroyinspeech"
DATA_DIR = "data/raw"


def download_dataset_(url, destination_dir):
    """download the dataset from kaggle using it api

    Parameters
    ----------
    url : str
        dataset kaggle url
    destination_dir : str, path
        directory to download the dataset into
    """

    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir)
    opd.download_kaggle_dataset(url, destination_dir)


def main():
    """
    main function to run the script
    """
    logger.info(f"Commencing downloading the dataset into {DATA_DIR}")
    try:
        download_dataset_(url=URL_, destination_dir=DATA_DIR)
        logger.success(f"Dataset downloaded to {DATA_DIR} successfully.")
    except Exception as error:
        logger.exception(f"Dataset download failed due to: {error}")


if __name__ == "__main__":
    main()
