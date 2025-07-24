import logging
from typing import Optional, Tuple

from app.nglogic.model.nglogic_api_data_model import nglogic_api_data

logger = logging.getLogger(__name__)

LOWER_VALUE_STATUS = "LOWER"
GREATER_VALUE_STATUS = "GREATER"
NOT_EXACT_VALUE_STATUS = "NOT_EXACT"
EXACT_VALUE_STATUS = "EXACT"

MIN_MAX_VALUE_THRESHOLD = 25


class ValueOutsideRangeError(ValueError):
    ...


def get_index(value: int) -> Tuple[Optional[int], Optional[str]]:
    if not nglogic_api_data.data:
        return None, None

    if value < nglogic_api_data.MIN_VALUE:
        if value < nglogic_api_data.MIN_VALUE - MIN_MAX_VALUE_THRESHOLD:
            raise ValueOutsideRangeError(
                f"Value {value} is too small. Minimum value is {nglogic_api_data.MIN_VALUE - MIN_MAX_VALUE_THRESHOLD}"
            )

        return nglogic_api_data.data[nglogic_api_data.MIN_VALUE], LOWER_VALUE_STATUS

    elif value > nglogic_api_data.MAX_VALUE:
        if value > nglogic_api_data.MAX_VALUE + MIN_MAX_VALUE_THRESHOLD:
            raise ValueOutsideRangeError(
                f"Value {value} is too hi. Maximum value is {nglogic_api_data.MAX_VALUE + MIN_MAX_VALUE_THRESHOLD}"
            )

        return nglogic_api_data.data[nglogic_api_data.MAX_VALUE], GREATER_VALUE_STATUS

    try:
        return nglogic_api_data.data[value], EXACT_VALUE_STATUS

    except KeyError:
        nearest_key = nglogic_api_data.get_nearest_key(value)
        logger.warning(
            f"Specified value: {value} not exists in datasource. Returning nearest index: {nearest_key}"
        )
        return (
            nglogic_api_data.data[nearest_key],
            NOT_EXACT_VALUE_STATUS,
        )
