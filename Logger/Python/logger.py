import logging
import logging.handlers
from typing import Optional, Union, Any


formatters_bank: dict[str, logging.Formatter] = {}
handlers_bank: dict[str, Union[logging.FileHandler, logging.handlers.SocketHandler]] = {}  # noqa: E501


def _filter_dict(dict: dict[str, Any]) -> dict[str, Any]:
    filtered = {}
    for k, v in dict.items():
        if v is not None:
            if isinstance(v, (str, list)):
                if len(v) > 0:
                    filtered.update({k: v})
            if isinstance(v, bool):
                filtered.update({k: v})
    return filtered


def create_logger(logger_name: str):
    logging.getLogger(logger_name)


def set_logger_level(logger_name: str, level: str):
    logging.getLogger(logger_name).setLevel(level)


def create_file_handler(
        handler_name: str,
        file_path: str,
        mode: str = 'a',
        encoding: Optional[str] = None,
        delay: bool = False,
        errors: Optional[str] = None
        ):
    kwargs = _filter_dict(locals())
    name = kwargs.pop('handler_name')
    filename = kwargs.pop('file_path')
    global handlers_bank
    handler = logging.FileHandler(filename=filename, **kwargs)
    handlers_bank.update({name: handler})


def create_socket_handler(handler_name: str, host: str, port: int):
    global handlers_bank
    handler = logging.handlers.SocketHandler(host=host, port=port)
    handlers_bank.update({handler_name: handler})


def set_handler_level(handler_name: str, level: str):
    global handlers_bank
    handlers_bank.get(handler_name).setLevel(level=level)


def add_handler(logger_name: str, handler_name: str):
    global handlers_bank
    handler = handlers_bank.get(handler_name)
    logging.getLogger(logger_name).addHandler(handler)


def create_formatter(
        formatter_name: str,
        format: str,
        date_format: Optional[str],
        style: Optional[str],
        validate: bool = True
        ):
    kwargs = _filter_dict(locals())
    name = kwargs.pop('formatter_name')
    fmt = kwargs.pop('format')
    datefmt = kwargs.pop('date_format', None)
    global formatters_bank
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt, **kwargs)
    formatters_bank.update({name: formatter})


def set_formatter(handler_name: str, formatter_name: str):
    global handlers_bank, formatters_bank
    handler = handlers_bank.get(handler_name)
    formatter = formatters_bank.get(formatter_name)
    handler.setFormatter(formatter)


def info(logger_name: str, message: str):
    logging.getLogger(logger_name).info(message)


def debug(logger_name: str, message: str):
    logging.getLogger(logger_name).debug(message)


def warning(logger_name: str, message: str):
    logging.getLogger(logger_name).warning(message)


def error(logger_name: str, message: str):
    logging.getLogger(logger_name).error(message)


def critical(logger_name: str, message: str):
    logging.getLogger(logger_name).critical(message)
