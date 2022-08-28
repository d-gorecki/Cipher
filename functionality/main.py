from functionality.facade import Manager


# logging.basicConfig(level=logging.INFO, format="")


def main():
    """Main function"""
    manager: Manager = Manager()
    manager.run_app()


if __name__ == "__main__":
    main()
