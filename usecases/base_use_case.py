from abc import ABC, abstractmethod

from repositories.base_repository import BaseRepository
from controllers.request_objects import BaseRequest
from controllers.response_object import BaseResponse


class BaseUseCase(ABC):
    @abstractmethod
    def __init__(self, repo: BaseRepository) -> None:
        raise NotImplementedError()

    @abstractmethod
    def handle(self, request: BaseRequest) -> BaseResponse:
        raise NotImplementedError()
