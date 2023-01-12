from ddtrace import config, patch


def ddtrace_config():
    patch(fastapi=True)
    # Override service name
    config.fastapi["service_name"] = "poc-service-python"
    # Override request span name
    config.fastapi["request_span_name"] = "poc.service.python.request"
