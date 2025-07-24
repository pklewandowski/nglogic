import logging
import traceback

from rest_framework import status
from rest_framework.response import Response

import settings

logger = logging.getLogger(__name__)


def rest_api_wrapper(fn):
    def _wrapped(ref, request, **kwargs):
        try:
            response_data, response_status, errmsg = fn(ref, request, **kwargs) or {}

            if errmsg:
                logger.error(errmsg)

        except Exception as ex:
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
            _traceback = traceback.format_exc()

            logger.error(_traceback)

            response_data = {
                'errmsg': str(ex),
                'errtype': ex.__class__.__name__,
            }

            if settings.DEBUG:
                response_data['traceback'] = _traceback

        return Response(data=response_data, status=response_status)

    return _wrapped
