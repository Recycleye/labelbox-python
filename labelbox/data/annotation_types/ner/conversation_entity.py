from typing import Dict, Any

from pydantic import BaseModel, root_validator

from labelbox.data.annotation_types.ner.text_entity import TextEntity
from labelbox.utils import _CamelCaseMixin


class ConversationEntity(TextEntity, _CamelCaseMixin):
    """ Represents a text entity """
    message_id: str