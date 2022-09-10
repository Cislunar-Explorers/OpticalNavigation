from distutils.core import setup

setup(
    name="optical-navigation",
    version="0.1",
    author="SSDS",
    author_email="arn45@cornell.edu",
    description="Cislunar Explorers optical navigation framework",
    install_requires=["numpy", "matplotlib", "pytest",
                      "scipy", "astropy", "pandas", "jsonschema"],
    package_dir={"": "src"},
)
