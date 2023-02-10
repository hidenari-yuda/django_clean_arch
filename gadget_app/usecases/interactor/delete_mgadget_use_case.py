import logging

from gadget_app.repositories import MGadgetRepository
from gadget_app.domain.exceptions import UnexpectedError
from gadget_app.controllers.request_objects import DeleteMGadgetRequest
from gadget_app.controllers.response_object import DeleteMGadgetResponse
from ..base_use_case import BaseUseCase


class DeleteMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository) -> None:
        self._repo = repo

    def handle(self, request: DeleteMGadgetRequest) -> DeleteMGadgetResponse:
        try:
            self._repo.delete(request.id)
        except Exception as e:
            logging.exception(e)

            raise UnexpectedError('Failed to delete gadget.')

        return DeleteMGadgetResponse()
