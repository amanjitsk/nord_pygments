from setuptools import setup

setup(
    name="nord_pygments",
    version="0.1",
    py_modules=["nord_pygments", "ansi", "flattened"],
    license="BSD-3",
    entry_points={
        "pygments.styles": [
            "nord = nord_pygments:NordStyle",
            "terminal = ansi:AnsiStyle",
            "flattened-light = flattened:FlattenedLightStyle",
            "flattened-dark = flattened:FlattenedDarkStyle",
        ]
    },
)
