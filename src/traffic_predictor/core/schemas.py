import pandera as pa
from pandera.typing import Series


class BaseInputs(pa.DataFrameModel):
    """Model base inputs"""

    timestamp: Series[pa.DateTime] = pa.Field(nullable=False)

    class Config:
        strict = True
        coerce = True


class Outputs(pa.DataFrameModel):
    """Model outputs"""

    traffic: Series[int] = pa.Field(nullable=False, ge=0)

    class Config:
        strict = True
        coerce = True
