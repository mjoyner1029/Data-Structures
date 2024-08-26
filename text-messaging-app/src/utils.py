# src/utils.py
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def format_timestamp(timestamp):
    """
    Formats a datetime object into a string suitable for logging or display.
    
    :param timestamp: A datetime object to format.
    :return: A formatted string representation of the datetime.
    """
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")

def log_info(message):
    """
    Logs an informational message to the console.
    
    :param message: The message to log.
    """
    logging.info(message)

def log_error(message):
    """
    Logs an error message to the console.
    
    :param message: The message to log.
    """
    logging.error(message)
