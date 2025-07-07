import logging
from typing import List, Any

def configure_logger(log_file: str, logger_name:str) -> logging.Logger:
    """
    Configure and return a logger with both file and console handlers.

    Args:
      log_file(str): The name of the log file.
      logger_name(str): The name of the logger.

    Returns:
      logging.Logger: Configure logger instance
    """
    #Create a logger
    logger = logging.getLogger(logger_name)
   
    # Set logging level
    logger.setLevel(logging.INFO)

    # Level      | Severity   | Description
    # ---------- | ---------- | ----------------------------------------------------------
    # DEBUG      | Lowest     | Detailed diagnostic information for debugging.
    # INFO       | Low        | Informational messages that confirm normal operation.
    # WARNING    | Medium     | Potential issues that might require attention.
    # ERROR      | High       | Errors that prevent part of the program from functioning.
    # CRITICAL   | Highest    | Serious errors causing application-wide issues or crashes.

    #File handler for loggin to a file
    file_handler = logging.FileHandler(log_file, mode="a")
    file_handler.setFormatter(
        logging.Formatter ("%(asctime)s:%(levelname)s:%(name)s:%(message)s")   )
    
    #Console handler for logging to the console
    console_handler = logging.StreamHandler()

    #Set format
    console_handler.setFormatter(logging.Formatter ("%(asctime)s:%(levelname)s:%(name)s:%(message)s"))

    #Add handlers to my logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def search_item(item: List[Any], item_to_find: Any, logger: logging.logger) -> int:

    """
    Search for an item in a list and returm its index.
    Args:
     items(List[Any]): list of items to search within
     item_to_find(Any): the item to find
     logger(logging.Logger): logger instance for logging messages

    Returns:
     int: the icdex of the item in the list
    
    Raises:
      ValueError: if the item is not found.

    """

    if not item:
        logger.warning("List is empty")
        raise ValueError("Cannot search in an empty list.")
    try:
        index = item.index(item_to_find)
        logger.info(f"Item {item_to_find} found at index {index}")
        return index
    except ValueError as e:
        logger.error(f"Item {item_to_find} not found in the list. Error: {e}", exc_info = True)
        raise # Re raise the same ValueError


def main():
    log_file = "cf7_2.log"

    #configure logger
    logger = configure_logger(log_file, 'search_app2')

    employee_names = ["Katerina", "Bob", "Manos", "Marika"]

    employee_to_find = "Soula"

    try:
        index = search_item(employee_names, employee_to_find, logger)
        print(f"Employee {employee_to_find} found at index {index}")
    except ValueError:
        print(f"Employee {employee_to_find} was not found in the list.")


if __name__ == "__main__":
    main()