import logging


class Logger:

    file_path = '/Users/leon/Desktop/Leon_Automations/SauceDemoProject/Reports/LogsFile.log'
    # clean logs file
    with open(file_path, "w") as file:
        file.write("")

    # Create the file handler
    file_handler = logging.FileHandler(file_path)
    log = logging.getLogger(__name__)
    log.addHandler(file_handler)

    # Set the formatter for the file handler
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s - %(message)s")
    file_handler.setFormatter(formatter)

    # Set the logging level for the logger
    log.setLevel(logging.INFO)
