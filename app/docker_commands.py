import subprocess


def docker_compose_exec(service, command):
    """
    :param service: python-app
    :param command: ["flask", "routes"]
    """
    try:
        # Run the command using docker-compose exec
        # docker-compose exec -T avoids allocating a TTY which is necessary for non-interactive commands
        subprocess.run(["docker-compose", "exec", "-T", service] + command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command on {service}: {e}")


def main():
    ask = input(
        "1 for flask routes\n"
        "2 for database migrations\n"
        "3 for database seeding\n"
        "4 for data upgrade\n"
        "5 for dabase migrate and upgrade\n"
        "6 for installing a custom commands\n"
        "7 for installing a custom package\n"
        ": "
    )

    if ask not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid input")
    elif ask == "1":
        docker_compose_exec("python-app", ["flask", "routes"])
    elif ask == "2":
        docker_compose_exec("python-app", ["flask", "db", "migrate"])
    elif ask == "3":
        docker_compose_exec("python-app", ["flask", "db", "seed"])
    elif ask == "4":
        docker_compose_exec("python-app", ["flask", "db", "upgrade"])
    elif ask == "5":
        docker_compose_exec("python-app", ["flask", "db", "migrate"])
        docker_compose_exec("python-app", ["flask", "db", "upgrade"])
    elif ask == "6":
        package_name = input("Enter the package name: ").split(" ")
        docker_compose_exec("python-app", package_name)
    elif ask == "7":
        package_name = input("Enter the package name: ")
        if package_name != "":
            print(f"Installing {package_name}...")
            docker_compose_exec("python-app", ["pip", "install", package_name])
        else:
            print("Invalid input")
    # service = "python-app"
    # command = ["flask", "routes"]
    # Run the Flask database migration in the 'web' service
    # docker_compose_exec("python-app", ["flask", "db", "migrate"])
    # docker_compose_exec(service, command)

    # ... include any other logic you need here ...


if __name__ == "__main__":
    main()
