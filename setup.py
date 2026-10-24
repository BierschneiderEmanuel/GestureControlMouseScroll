import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))

VERSION = "1.0.2"
DESCRIPTION = "Control the mouse cursor and scrolling with hand gestures"

with open(os.path.join(HERE, "README.md"), encoding="utf-8") as handle:
    LONG_DESCRIPTION = handle.read()

with open(os.path.join(HERE, "requirements.txt"), encoding="utf-8") as handle:
    REQUIRED = [
        line.strip()
        for line in handle
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="gesturecontrolmousescroll",
    version=VERSION,
    author="Emanuel Bierschneider",
    author_email="emanuel.bierschneider@gmx.de",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/BierschneiderEmanuel/GestureControlMouseScroll",
    project_urls={
        "Homepage": "http://www.emanuelbierschneider.de/",
        "Source": "https://github.com/BierschneiderEmanuel/GestureControlMouseScroll",
    },
    license="MIT",
    # setup.py sits beside the package rather than inside it, so this finds
    # gesturecontrolmousescroll. Run from within the package directory it
    # found nothing, and the wheel shipped metadata and no code at all.
    packages=find_packages(exclude=("tests", "tests.*")),
    # The keyword is install_requires. It used to read install_reqs, which
    # setuptools silently ignores, so no dependency was ever declared.
    install_requires=REQUIRED,
    # mediapipe needs absl-py>=2.3, which is Python 3.8+.
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "gesturecontrolmousescroll=gesturecontrolmousescroll:main",
        ],
    },
    keywords=["mediapipe", "opencv", "gesture", "mouse", "hand tracking", "computer vision"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Topic :: Multimedia :: Video :: Capture",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
)
