from typing import Protocol


class ApplicantProtocol(Protocol):
    def request_book(self, title: str) -> str:
        """Metodo que debe implementar cualquier solicitante"""
        ...
