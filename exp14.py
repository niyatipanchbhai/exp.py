import logging

logging.basicConfig(
    filename="program.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")

def calculate():

    try:

        logging.debug("Calculation started")

        a = 10
        b = 2

        result = a / b

        print("Division Result:", result)

        logging.info("Calculation completed successfully")

    except ZeroDivisionError:

        logging.error("Cannot divide by zero")

    except Exception:

        logging.exception("An unexpected error occurred")

calculate()

try:

    a = 10
    b = 0

    result = a / b

except ZeroDivisionError:

    logging.exception("Division by zero exception occurred")

logging.info("Program ended")

print("\nCheck program.log file for log details.")
