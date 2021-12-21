import os
import re

from azure.storage.blob import BlobServiceClient, ContainerClient
from loguru import logger


def extract_file_path(path: str, container_name: str) -> str:
    """Given a blobstorage url for a file, extract the file path after
        container name.
        Example:
            https:/{storage-account-name}.blob.core.windows.net/{container-name}/images/1001.jpg
        returns
            images/1001.jpg
    """

    file_path_regex = re.compile(f"{container_name}/(.*)")
    return file_path_regex.search(path).group(1)


def create_blobstorage_client(azure_connection: str, azure_container_name: str) -> ContainerClient:
    service = BlobServiceClient.from_connection_string(azure_connection)
    return service.get_container_client(azure_container_name)


def get_connection_string() -> str:
    try:
        return os.environ["AZURE_STORAGE_CONNECTION_STRING"]
    except KeyError as ex:
        logger.exception("Environment variable AZURE_CONNECTION_STRING is not set")

