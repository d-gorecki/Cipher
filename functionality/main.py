from functionality.facade import Manager


# logging.basicConfig(level=logging.INFO, format="")


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
                print("Closing app...")
                manager.running = False
        except (FileNotFoundError, ValueError, IsADirectoryError) as e:
            print(e)
            continue


if __name__ == "__main__":
    main()
