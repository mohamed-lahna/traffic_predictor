from abc import ABC, abstractmethod
from pydantic import BaseModel
import pandas as pd


class Dataloader(BaseModel, ABC):
    """Data loader abstract class"""

    @abstractmethod
    def load_data(self) -> pd.DataFrame:
        """data loader abstract method

        Returns:
            pd.DataFrame: Pandas DataFrame
        """
        pass


class CSVLoader(Dataloader):
    """CSV data loader implementation

    Attributes:
        path (str): source path
    """

    path: str

    def load_data(self) -> pd.DataFrame:
        """CSV data loader implementation
        Returns:
            pd.DataFrame: Pandas DataFrame
        """
        return pd.read_csv(self.path)


class DataSaver(BaseModel, ABC):
    @abstractmethod
    def save_data(self, data: pd.DataFrame) -> None:
        """data saver abstract method

        Args:
            data (pd.DataFrame): Pandas DataFrame
        """
        pass


class CSVSaver(DataSaver):
    """CSV data saver implementation

    Attributes:
        path (str): destination path
    """

    path: str

    def save_data(self, data: pd.DataFrame) -> None:
        """CSV data saver implementation

        Args:
            data (pd.DataFrame): Pandas DataFrame
        """
        data.to_csv(self.path, index=False)
