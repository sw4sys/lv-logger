import logging
import logging.handlers
from typing import Optional, Any


def _filter_dict(dict: dict[str, Any]) -> dict[str, Any]:
    filtered = {}
    for k, v in dict.items():
        if v is not None and k != 'logger':
            if isinstance(v, (str, list)):
                if len(v) > 0:
                    filtered.update({k: v})
            if isinstance(v, bool):
                filtered.update({k: v})
    return filtered


def create_logger(name: str):
    return logging.getLogger(name)


def set_logger_level(logger: logging.Logger, level: str):
    logger.setLevel(level)
    return logger


def create_file_handler(
        file_path: str,
        mode: str = 'a',
        encoding: Optional[str] = None,
        delay: bool = False,
        errors: Optional[str] = None
        ):
    kwargs = _filter_dict(locals())
    filename = kwargs.pop('file_path')
    return logging.FileHandler(filename=filename, **kwargs)


def create_socket_handler(host: str, port: int):
    return logging.handlers.SocketHandler(host=host, port=port)


def set_handler_level(handler: logging.Handler, level: str):
    handler.setLevel(level)
    return handler


def add_handler(logger: logging.Logger, handler: logging.Handler):
    logger.addHandler(handler)
    return logger


def create_formatter(
        format: str,
        date_format: Optional[str],
        style: Optional[str],
        validate: bool = True
        ):
    kwargs = _filter_dict(locals())
    fmt = kwargs.pop('format')
    datefmt = kwargs.pop('date_format', None)
    return logging.Formatter(fmt=fmt, datefmt=datefmt, **kwargs)


def set_formatter(handler: logging.Handler, formatter: logging.Formatter):
    handler.setFormatter(formatter)
    return handler


def info(logger: logging.Logger, message: str):
    logger.info(message)
    return logger


def debug(logger: logging.Logger, message: str):
    logger.debug(message)
    return logger


def warning(logger: logging.Logger, message: str):
    logger.warning(message)
    return logger


def error(logger: logging.Logger, message: str):
    logger.error(message)
    return logger


def critical(logger: logging.Logger, message: str):
    logger.critical(message)
    return logger


if __name__ == '__main__':
    pass
