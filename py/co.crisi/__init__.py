from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version('cipher-sorcery-venture')
except PackageNotFoundError:
    __version__ = '(local)'

del PackageNotFoundError
del version
