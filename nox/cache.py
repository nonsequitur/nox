from dogpile.cache import make_region
import os

region = make_region().configure(
    'dogpile.cache.dbm',
    arguments={'filename': os.environ['HOME'] + '/.cache/nox.dbm'}
)
