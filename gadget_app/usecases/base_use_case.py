from abc import ABC, abstractmethod

from gadget_app.repositories.base_repository import BaseRepository
from gadget_app.controllers.request_objects import BaseRequest
from gadget_app.controllers.response_object import BaseResponse


class BaseUseCase(ABC):
    @abstractmethod
    def __init__(self, repo: BaseRepository) -> None:
        raise NotImplementedError()

    @abstractmethod
    def handle(self, request: BaseRequest) -> BaseResponse:
        raise NotImplementedError()
