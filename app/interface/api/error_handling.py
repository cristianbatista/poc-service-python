from fastapi import status
from fastapi.exceptions import RequestValidationError
from fastapi.logger import logger
from fastapi.responses import JSONResponse
from starlette.requests import Request

from app.interface.api.error_schema import ApiError, RequestValidationApiError
from app.shared.root_exception import RootException


def init_error_handling(app):
    @app.exception_handler(Exception)
    async def default_exception_handler(request: Request, exc: Exception):
        api_error = ApiError(developer_message=str(exc))
        api_error_dict = api_error.dict()

        log_extra = {
            "api_error": api_error_dict,
            "request": {"method": request.method, "path": request.url.path},
        }
        logger.exception(api_error.developer_message, extra=log_extra)

        return JSONResponse(status_code=500, content=api_error_dict)

    @app.exception_handler(RootException)
    async def base_exception_handler(request: Request, exc: RootException):
        api_error = ApiError(
            developer_message=str(exc.message), user_message=str(exc.message)
        )
        api_error_dict = api_error.dict()

        log_extra = {
            "api_error": api_error_dict,
            "request": {"method": request.method, "path": request.url.path},
        }
        logger.exception(api_error.developer_message, extra=log_extra)

        return JSONResponse(status_code=400, content=api_error_dict)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        request_validation_error = RequestValidationApiError(
            developer_message=str(exc),
            errors=exc.errors(),
        )
        request_validation_error_dict = request_validation_error.dict()

        log_extra = {
            "request_validation_error": request_validation_error_dict,
            "request": {"method": request.method, "path": request.url.path},
        }
        logger.exception(request_validation_error.developer_message, extra=log_extra)

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=request_validation_error_dict,
        )
