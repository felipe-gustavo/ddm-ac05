from yoyo import read_migrations
from yoyo import get_backend
from .connection import DATABASE

backend = get_backend(DATABASE)
migrations = read_migrations(
    'src/shared/infra/database_migration/yoyo/migrations')

with backend.lock():
    backend.apply_migrations(backend.to_apply(migrations))
