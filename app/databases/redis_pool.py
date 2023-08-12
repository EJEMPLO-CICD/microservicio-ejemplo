from orm.config.database_config import DatabaseConfig
from orm.config.redis_connection import RedisConnection

from app.config.environment import get_environment_variables

s = get_environment_variables()

redis_config = (DatabaseConfig()
                .set_host(s.REDIS_HOST)
                .set_port(s.REDIS_PORT)
                .set_password(s.REDIS_PASSWORD)
                .set_database(s.REDIS_DB)
                .build())

redis_connection = RedisConnection(redis_config)
redis_session = redis_connection.get_redis_conn()