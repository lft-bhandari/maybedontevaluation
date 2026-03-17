import os


def read_tool(file_path: str) -> str:
    """
    Read and return the contents of a .txt file.

    Args:
        file_path: Path to the file to read.

    Returns:
        The text content of the file.

    Raises:
        ValueError: If the file is not a .txt file.
        FileNotFoundError: If the file does not exist.
        OSError: If there is an error opening/reading the file.
    """
    _, ext = os.path.splitext(file_path)
    if ext.lower() != ".txt":
        raise ValueError("read_tool currently supports only .txt files.")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
