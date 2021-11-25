class DiscordException(Exception):
    """Base exception class for discord
    Ideally speaking, this could be caught to handle any exceptions raised from this library.
    """

    pass

class IPCError(DiscordException):
    """Base IPC exception class"""

    pass


class NoEndpointFoundError(IPCError):
    """Raised upon requesting an invalid endpoint"""

    pass


class ServerConnectionRefusedError(IPCError):
    """Raised upon a server refusing to connect / not being found"""

    pass


class JSONEncodeError(IPCError):
    """Raise upon un-serializable objects are given to the IPC"""

    pass


class NotConnected(IPCError):
    """Raised upon websocket not connected"""

    pass
