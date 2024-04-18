from setuptools import find_packages, setup

setup(
    name="base_dagster",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-snowflake",
        "dbt-snowflake",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)