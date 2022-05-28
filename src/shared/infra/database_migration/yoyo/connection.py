import config.environment as env

DATABASE = 'mysql://{username}:{password}@{host}:{port}/{dbname}'.format(
    username=env.DB_SQL_USERNAME,
    password=env.DB_SQL_PASSWORD,
    host=env.DB_SQL_HOST,
    port=env.DB_SQL_OUTPORT,
    dbname=env.DB_SQL_DBNAME,
)
