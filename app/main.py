import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    directory_path = os.path.dirname(destination)

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)
    os.replace(source, destination)
