import pytest

import settings
from app.nglogic.model.nglogic_api_data_model import nglogic_api_data

TEST_DATA_PATH = settings.BASE_DIR / "app" / "nglogic" / "tests" / "test_data" / "test_input.txt"

DEFAULT_API_URL_BASE = "/nglogic"


@pytest.fixture(autouse=True)
def fx_nglogic_api_test_data():
    nglogic_api_data.initialize(TEST_DATA_PATH)
