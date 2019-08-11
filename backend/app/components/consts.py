from enum import IntEnum


class StatusCodes(IntEnum):
    # enum class for DB Queue pattern
    QUEUED = 0
    IN_PROCESS = 2
    COMPLETE = 3
    ERROR = 99
