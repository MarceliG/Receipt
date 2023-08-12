import os

ROOT_DIR = os.path.realpath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
    )
)
PHOTOS_DIR = os.path.realpath(
    os.path.join(
        ROOT_DIR,
        "data",
        "photos",
    )
)
