from dataclasses import dataclass
from .base_response import BaseResponse
from domain.entity import MGadgetModel
from utils import mgadget_serialize
from typing import List, Dict, Any


@dataclass
class ListMGadgetResponse(BaseResponse):
    mgadgets: List[MGadgetModel]

    def to_json(self) -> Dict[str, Any]:
        return {
            'datas': [mgadget_serialize(mgadget) for mgadget in self.mgadgets]
        }
