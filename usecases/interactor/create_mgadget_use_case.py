import logging
from dataclasses import asdict

from repositories import MGadgetRepository
from domain.exceptions import UnexpectedError
from controllers.request_objects import CreateMGadgetRequest
from controllers.response_object import CreateMGadgetResponse
from ..base_use_case import BaseUseCase


class CreateMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository) -> None:
        self._repo = repo

    def handle(self, request: CreateMGadgetRequest) -> CreateMGadgetResponse:
        try:
            mgadget_id = self._repo.create(asdict(request))
        except Exception as e:
            logging.exception(e)

            raise UnexpectedError("Failed to create gadget.")

        return CreateMGadgetResponse(mgadget_id)
