import re
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Framework :: AsyncIO",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Communications",
    "Topic :: Documentation",
    "Topic :: Documentation :: Sphinx",
    "Topic :: Internet",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

extras_require = {
    "docs": [
        "sphinx",
        "sphinxcontrib_trio",
        "sphinx-rtd-theme",
    ],
}

packages = [
    "discord.ext.ipc",
]

project_urls = {
    "Documentation": "https://nextcord-ext-ipc.readthedocs.io",
    "Issue Tracker": "https://github.com/nextcord/nextcord-ext-ipc/issues",
    "Source": "https://github.com/nextcord/nextcord-ext-ipc",
}

_version_regex = r"^version = ('|\")((?:[0-9]+\.)*[0-9]+(?:\.?([a-z]+)(?:\.?[0-9])?)?)\1$"

with open("discord/ext/ipc/__init__.py") as stream:
    match = re.search(_version_regex, stream.read(), re.MULTILINE)

version = match.group(2)

if match.group(3) is not None:
    try:
        import subprocess

        process = subprocess.Popen(["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += out.decode("utf-8").strip()

        process = subprocess.Popen(["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except (Exception) as e:
        pass


setuptools.setup(
    author="Nextcord Developers",
    classifiers=classifiers,
    description="A Nextcord extension for inter-process communication.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require=extras_require,
    install_requires=None,
    license="Apache Software License",
    name="discord-ext-ipc",
    packages=packages,
    project_urls=project_urls,
    python_requires=">=3.6.0",
    url="https://github.com/nextcord/nextcord-ext-ipc",
    version=version,
)
