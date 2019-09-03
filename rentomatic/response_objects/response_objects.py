class ResponseSuccess:
    SUCCESS = "Success"

    def __init__(self, value=None):
        self.type = self.SUCCESS
        self.value = value

    def __bool__(self):
        return True


class ResponseFailure:
    RESOURCE_ERROR = "ResourceError"
    PARAMETERS_ERROR = "ParametersError"
    SYSTEM_ERROR = "SystemError"

    def __init__(self, type, message):
        self.type = type
        self.message = self._format_message(message)

    def __bool__(self):
        return False

    def _format_message(self, message):
        if isinstance(message, Exception):
            return f"{message.__class__.__name__}: {message}"
        return message

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    @classmethod
    def build_from_invalid_request_object(cls, request_object):
        message = "\n".join(["{}: {}".format(error["parameter"], error["message"]) for error in request_object.errors])
        return cls(cls.PARAMETERS_ERROR, message)

    @classmethod
    def build_resource_error(cls, message=None):
        return cls(cls.RESOURCE_ERROR, message)

    @classmethod
    def build_parameters_error(cls, message=None):
        return cls(cls.PARAMETERS_ERROR, message)

    @classmethod
    def build_system_error(cls, message=None):
        return cls(cls.SYSTEM_ERROR, message)
