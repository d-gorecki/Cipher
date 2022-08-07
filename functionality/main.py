from functionality.facade import Manager
import logging

logging.basicConfig(level=logging.INFO, format="")


def main():
    """Main function"""
    manager = Manager()

    while manager.running:
        manager.exit = manager.user_request_handler()
        if manager.exit:
            break
        continue_: str = input("Continue?(y/n):\n>>> ")
        if continue_ == "n":
            logging.info("Closing app...")
            manager.running = False


if __name__ == "__main__":
    main()
