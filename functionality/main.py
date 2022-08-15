from functionality.facade import Manager
import logging
import time

logging.basicConfig(level=logging.INFO, format="")


def main():
    """Main function"""
    manager: Manager = Manager()
    while manager.running:
        try:
            manager.exit = manager.user_request_handler()
            if manager.exit:
                break
            continue_: str = input("Continue?(y/n):\n>>> ")
            if continue_ == "n":
                logging.info("Closing app...")
                manager.running = False
        except FileNotFoundError:
            logging.warning("File not found\nReturning to main menu...")
            continue
        except ValueError:
            logging.warning("Wrong value\nReturning to main menu...")
            continue
        except IsADirectoryError:
            logging.warning("Passed file name is directory\nReturning to main menu...")


if __name__ == "__main__":
    main()
