"""
Global exception handlers for controller domain
"""

class HttpProviderError(Exception):
    """
    Exception handler for misisng HTTP Provider
    """
    
class IpcProviderError(Exception):
    """
    Exception handler for missing IPC based provider
    """
    
class SocketProviderError(Exception):
    """
    Exception handler for missin Web Socker provider
    """