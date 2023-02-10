import logging

from gadget_app.repositories import MGadgetRepository
from gadget_app.domain.exceptions import UnexpectedError
from gadget_app.controllers.request_objects import UpdateMGadgetRequest
from gadget_app.controllers.response_object import UpdateMGadgetResponse
from ..base_use_case import BaseUseCase


class UpdateMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository) -> None:
        self._repo = repo

    def handle(self, request: UpdateMGadgetRequest) -> UpdateMGadgetResponse:
        try:
            self._repo.update(request.data)
        except Exception as e:
            logging.exception(e)

            raise UnexpectedError("Failed to update gadget.")

        return UpdateMGadgetResponse()
