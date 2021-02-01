import setuptools

with open("../README.md", "r", encoding="utf-8") as fh:
    longDesc = fh.read()

setuptools.setup(
    name="imager-pkg-dq",
    version="0.0.1",
    author="Daniel Q",
    author_email="dquilitzsch@outlook.de",
    description="An web-based Image Viewer divided in microservices",
    long_description=longDesc,
    long_description_content_type="text/markdown",
    url="https://github.com/alirionx/imager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        #"License :: OSI Approved :: AppScape License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)