"""Setup configuration for IFS Fractal Generator.

This allows the package to be installed in development mode,
making imports work correctly for tests.
"""

from setuptools import setup, find_packages

setup(
    name="ifs-fractal-generator",
    version="0.1.0",
    description="IFS Fractal Generator for Blender Geometry Nodes",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        # Runtime dependencies (minimal for now)
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-xdist>=3.3.0",
            "pytest-mock>=3.11.0",
            "pytest-timeout>=2.1.0",
            "fake-bpy-module-latest>=20230117",
            "jsonschema>=4.19.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
            "isort>=5.12.0",
            "pre-commit>=3.3.3",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics :: 3D Modeling",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)

