import logging
from typing import Any, Callable, Dict, Tuple

logger = logging.getLogger()


def logger_wrapper(func: Callable[..., Any]):
    def wrapper(self: Any, *args: Tuple[Any], **kwargs: Dict[Any, Any]) -> Any:
        logger.info(f"{self.__class__.__name__}::{func.__name__} -- start")
        result = func(self, *args, **kwargs)
        logger.info(f"{self.__class__.__name__}::{func.__name__} -- end")
        return result

    return wrapper
