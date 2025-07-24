import pytest

from app.nglogic.api import services
from app.nglogic.api.services import (
    LOWER_VALUE_STATUS,
    NOT_EXACT_VALUE_STATUS,
    GREATER_VALUE_STATUS,
    EXACT_VALUE_STATUS,
    ValueOutsideRangeError,
)
from app.nglogic.model.nglogic_api_data_model import nglogic_api_data


def test_nglogic_api_data_initialization_form_datafile():
    assert len(nglogic_api_data.data) == 10000


def test_min_value_outside_allowed_range():
    with pytest.raises(ValueOutsideRangeError):
        services.get_index(-26)


@pytest.mark.xfail(raises=ValueOutsideRangeError)
def test_max_value_outside_allowed_range():
    with pytest.raises(ValueOutsideRangeError):
        services.get_index(999926)


def test_nglogic_get_index():
    assert services.get_index(-1) == (0, LOWER_VALUE_STATUS)
    assert services.get_index(9) == (0, NOT_EXACT_VALUE_STATUS)
    assert services.get_index(189) == (2, NOT_EXACT_VALUE_STATUS)
    assert services.get_index(1256) == (13, NOT_EXACT_VALUE_STATUS)
    assert services.get_index(999901) == (9999, GREATER_VALUE_STATUS)
    assert services.get_index(999900) == (9999, EXACT_VALUE_STATUS)
    assert services.get_index(200) == (2, EXACT_VALUE_STATUS)
