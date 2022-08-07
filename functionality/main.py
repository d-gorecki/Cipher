from functionality.facade import Manager
import logging
import time

logging.basicConfig(level=logging.INFO, format="")


def main():
    """Main function"""
    manager = Manager()
    while manager.running:
        try:
            manager.exit = manager.user_request_handler()
            if manager.exit:
                break
            continue_: str = input("Continue?(y/n):\n>>> ")
            if continue_ == "n":
                logging.info("Closing app...")
                manager.running = False
        except FileNotFoundError as e:
            logging.warning(e)
            time.sleep(5)
            continue


if __name__ == "__main__":
    main()
