from pathlib import Path
from typing import Iterable


def load_documents(directory: Path) -> Iterable[Path]:
    return [path for path in directory.iterdir() if path.is_file()]
