class ParkingError(Exception):
    """Base business error for parking domain."""


class NotFoundError(ParkingError):
    pass


class ConflictError(ParkingError):
    pass


class ValidationError(ParkingError):
    pass
