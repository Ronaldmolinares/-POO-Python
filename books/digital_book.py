from datetime import datetime

from models.book import Book


class DigitalBook(Book):
    MAX_LOAN_DAYS = 7

    def calculate_duration(self) -> str:
        if self.loan_date:
            dias_transcurridos = (datetime.now() - self.loan_date).days
            dias_restantes = self.MAX_LOAN_DAYS - dias_transcurridos
            if dias_restantes > 0:
                return f"Días restantes: {dias_restantes} de {self.MAX_LOAN_DAYS}"
            else:
                return f" Préstamo VENCIDO hace {abs(dias_restantes)} días"
        return f"Préstamo máximo: {self.MAX_LOAN_DAYS} días"
