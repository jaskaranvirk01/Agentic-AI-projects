import logging

import httpx
from tenacity import (
    RetryCallState,
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from llm.rate_limiter import RateLimiter

logger = logging.getLogger(__name__)

rate_limiter = RateLimiter(
    requests_per_second=2,
)

RETRY_STATUS_CODES = {
    429,  # Too Many Requests
    500,  # Internal Server Error
    502,  # Bad Gateway
    503,  # Service Unavailable
    504,  # Gateway Timeout
}


def is_retryable_exception(exception: Exception) -> bool:
    """
    Return True only for transient HTTP errors that are worth retrying.
    """

    if not isinstance(exception, httpx.HTTPStatusError):
        return False

    return exception.response.status_code in RETRY_STATUS_CODES


def log_retry(retry_state: RetryCallState) -> None:
    """
    Log retry information before the next retry attempt.
    """

    exception = retry_state.outcome.exception()

    attempt = retry_state.attempt_number

    wait_time = (
        retry_state.next_action.sleep
        if retry_state.next_action
        else 0
    )

    if isinstance(exception, httpx.HTTPStatusError):
        status_code = exception.response.status_code

        logger.warning(
            "\n"
            "================ RETRY =================\n"
            "Attempt      : %s\n"
            "Status Code  : %s\n"
            "Waiting      : %.2f seconds\n"
            "Reason       : %s\n"
            "========================================",
            attempt,
            status_code,
            wait_time,
            exception,
        )

    else:
        logger.warning(
            "\n"
            "================ RETRY =================\n"
            "Attempt      : %s\n"
            "Waiting      : %.2f seconds\n"
            "Reason       : %s\n"
            "========================================",
            attempt,
            wait_time,
            exception,
        )


@retry(
    retry=retry_if_exception(is_retryable_exception),
    wait=wait_exponential(
        multiplier=2,
        min=2,
        max=60,
    ),
    stop=stop_after_attempt(5),
    before_sleep=log_retry,
    reraise=True,
)
def invoke_llm(model, prompt):
    """
    Central wrapper for every LLM invocation.
    """

    rate_limiter.acquire()

    return model.invoke(prompt)
