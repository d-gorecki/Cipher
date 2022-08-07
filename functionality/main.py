from functionality.facade import Manager
import logging

logging.basicConfig(level=logging.INFO, format="")


def main():
    """Main function"""
    manager = Manager()
    manager_exit: bool

    while manager.running:
        manager_exit = manager.user_request_handler()
        if manager_exit:
            break
        continue_: str = input("Continue?(y/n):\n>>> ")
        if continue_ == "n":
            logging.info("Closing app...")
            manager.running = False


if __name__ == "__main__":
    main()
