from utilityx.internet.email.email_address import EmailAddress

class SportRadarEmailAddressValidator(EmailAdressValidator):
    def __init__(self, email:Union[str,EmailAdress]):
        super().__init__(email)
