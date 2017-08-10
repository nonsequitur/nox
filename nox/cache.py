from dogpile.cache import make_region
import getpass

region = make_region().configure(
    'dogpile.cache.dbm',
    arguments={'filename': '/tmp/nox.dbm.'+getpass.getuser()}
)
