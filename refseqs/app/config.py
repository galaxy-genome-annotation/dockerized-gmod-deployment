import os
SQLALCHEMY_DATABASE_URI = "postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}".format(**os.environ)
