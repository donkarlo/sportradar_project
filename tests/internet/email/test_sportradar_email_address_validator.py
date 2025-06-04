import pytest
from sportradar.internet.email.sportradar_email_address_validator import SportRadarEmailAddressValidator


class TestSportradarEmailAddressValidator:
    @pytest.mark.parametrize(
        "input_email, expected_validity",
        [
            ("someone@sportradar.com", True),
            ("anotherone@sport.at", False),
            ("dead.red", False),
        ]
    )
    def test_get_validity(self, input_email, expected_validity):
        email_validator = SportRadarEmailAddressValidator(input_email)
        assert email_validator.get_validity() == expected_validity
