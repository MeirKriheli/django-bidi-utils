DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/bidiutils.db'
INSTALLED_APPS = ['bidiutils']
TEMPLATE_CONTEXT_PROCESSORS = (
    'bidiutils.context_processors.bidi',
)
