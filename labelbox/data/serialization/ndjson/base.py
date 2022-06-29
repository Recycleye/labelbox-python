from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, validator, Field

from labelbox.utils import camel_case
from ...annotation_types.types import Cuid


class DataRow(BaseModel):
    id: str = None

    @validator('id', pre=True, always=True)
    def validate_id(cls, v):
        if v is None:
            raise ValueError(
                "Data row ids are not set. Use `LabelGenerator.add_to_dataset`, `LabelList.add_to_dataset`, or `Label.create_data_row`. "
                "You can also manually assign the id for each `BaseData` object"
            )
        return v


class NDJsonBase(BaseModel):
    uuid: str = None
    data_row: DataRow

    @validator('uuid', pre=True, always=True)
    def set_id(cls, v):
        return v or str(uuid4())

    class Config:
        allow_population_by_field_name = True
        alias_generator = camel_case


class NDAnnotation(NDJsonBase):
    schema_id: Optional[Cuid] = None
    name: Optional[str] = None

    @validator('name', pre=True, always=True)
    def validate_name(cls, v, values):
        if v is None and 'schema_id' not in values:
            raise ValueError("Name is not set. Either set name or schema_id.")

    @validator('schema_id', pre=True, always=True)
    def validate_id(cls, v, values):
        if v is None and 'name' not in values:
            raise ValueError(
                "Schema ids or names are not set. Use `LabelGenerator.assign_feature_schema_ids`, `LabelList.assign_feature_schema_ids`, or `Label.assign_feature_schema_ids`."
            )
        return v

    def dict(self, *args, **kwargs):
        res = super().dict(*args, **kwargs)
        if self.name is None:
            res.pop('name')
        if self.schema_id is None:
            res.pop('schemaId')
        return res