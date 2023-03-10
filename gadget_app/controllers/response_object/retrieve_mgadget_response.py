from dataclasses import dataclass
from .base_response import BaseResponse
from gadget_app.domain.entity import MGadgetModel
from gadget_app.utils.serializer import mgadget_serialize
from typing import Dict, Any


@dataclass
class RetrieveMGadgetResponse(BaseResponse):
    mgadget: MGadgetModel

    def to_json(self) -> Dict[str, Any]:
        return mgadget_serialize(self.mgadget)
