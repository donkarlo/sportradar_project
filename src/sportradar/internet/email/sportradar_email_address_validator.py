from utilityx.internet.email.email_address import EmailAddress
from utilityx.internet.email.email_address_validator import EmailAddressValidator
from typing import Union

class SportRadarEmailAddressValidator(EmailAddressValidator):
    def __init__(self, email:Union[str,EmailAddress]):
        super().__init__(email)

    def _do_get_validity(self) -> bool:
        if self._email.get_domain() != "sportradar.com":
            return False
        return True
