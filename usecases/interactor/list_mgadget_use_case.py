from repositories import MGadgetRepository
from controllers.request_objects import ListMGadgetRequest
from controllers.response_object import ListMGadgetResponse
from ..base_use_case import BaseUseCase


class ListMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository) -> None:
        self._repo = repo

    def handle(self, request: ListMGadgetRequest) -> ListMGadgetResponse:
        mgadgets = self._repo.all()

        return ListMGadgetResponse(mgadgets)
