from functionality.facade import Manager


def main():
    """Main function"""
    manager = Manager()
    running: bool = True

    while running:
        if manager.user_request_handler():
            continue_ = input("Continue? [y/n]")
            if continue_ == "n":
                running = False
        else:
            running = False


if __name__ == "__main__":
    main()
