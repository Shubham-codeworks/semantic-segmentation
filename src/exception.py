import sys
from src.logger import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
    line_number = exc_tb.tb_lineno if exc_tb else "Unknown"
    
    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{line_number}] error message[{str(error)}]"
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self) -> str:
        return self.error_message