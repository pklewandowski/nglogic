import logging
from typing import Optional

from rest_framework import views, status

from app.nglogic.api import services
from app.nglogic.api.serializers import NglogicApiSerializer
from app.nglogic.api.services import ValueOutsideRangeError
from app.nglogic.model.nglogic_api_data_model import nglogic_api_data
from utils.decorators import rest_api_wrapper

logger = logging.getLogger(__name__)


class NglogicAPIView(views.APIView):
    @staticmethod
    def _collect_data(idx: Optional[int], value: Optional[int], message: Optional[str]):
        return {"idx": idx, "value": value, "message": message}

    @staticmethod
    def _set_message(idx_status: Optional[str]):
        match idx_status:
            case services.EXACT_VALUE_STATUS:
                message = "Value is an exact match. Request completed"
            case services.NOT_EXACT_VALUE_STATUS:
                message = "Value was not found in datasource. Nearest index returned"
            case services.LOWER_VALUE_STATUS:
                message = "Value is negative. Returning min possible index"
            case services.GREATER_VALUE_STATUS:
                message = "Value is to big. Returning max possible index"
            case _:
                message = "Request completed"

        return message

    @rest_api_wrapper
    def get(self, request, value: int):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")

        if not nglogic_api_data.data:
            logger.error("No data in datasource")
            errmsg = "The datasource is empty. Returning nothing"

            return (
                self._collect_data(None, value, errmsg),
                status.HTTP_400_BAD_REQUEST,
                errmsg,
            )

        try:
            idx, idx_status = services.get_index(value)

        except ValueOutsideRangeError as ex:
            errmsg = str(ex)

            return (
                self._collect_data(None, value, message=errmsg),
                status.HTTP_422_UNPROCESSABLE_ENTITY,
                errmsg,
            )

        nglogic_serializer = NglogicApiSerializer(
            data=self._collect_data(idx, value, self._set_message(idx_status))
        )

        nglogic_serializer.is_valid(raise_exception=True)

        return nglogic_serializer.data, status.HTTP_200_OK, None
