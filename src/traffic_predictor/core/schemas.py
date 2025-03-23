import pandera as pa
from pandera.typing import Series


class BaseDataSchema(pa.DataFrameModel):
    """Mandatory core features"""

    timestamp: Series[pa.DateTime] = pa.Field(nullable=False)
    traffic: Series[int] = pa.Field(nullable=False, ge=0)

    class Config:
        strict = True
        coerce = True
