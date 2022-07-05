from setuptools import setup


setup(
    name="CNH Info Extract",
    version="0.1.0",
    description="A demo which extract information from driving license.",
    author="BRAIN (Brazilian Artificial Inteligence Nuclues)",
    license="LICENSE.txt",
    long_description=open("README.md").read(),
    install_requires=[
        "wheel",
        "paddlepaddle",
        "paddleocr>=2.0.1",
        "protobuf==3.20.*",
        "opencv-python",
        "matplotlib",
        "torch",
        "torchvision",
        "PyYAML",
        "requests",
        "pandas",
        "seaborn",
        "symspellpy",
        "ipython",
        "psutil"
    ]
)
