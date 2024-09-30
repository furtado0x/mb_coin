from aiocache import Cache
from aiocache.serializers import JsonSerializer

from src.ports.cache import CacheAbstract
from config import settings

class RedisCache(CacheAbstract):
    def __init__(self):
        try:
            self.cache = Cache(
                Cache.REDIS,
                endpoint=settings.redis_host,
                port=settings.redis_port,
                ttl=settings.redis_ttl,
                namespace=settings.redis_namespace,
                serializer=JsonSerializer()
            )
        except Exception as e:
            self.cache = None

    async def get(self, key: str) -> any:
        if not self.cache:
            return None
        try:
            return await self.cache.get(key)
        except Exception as e:
            return None    

    async def set(
        self,
        key: str,
        value: any,
        ttl: int = settings.redis_ttl
    ) -> None:
        if not self.cache:
            return None
        try:
            await self.cache.set(key, value, ttl)
        except Exception as e:
            return None
        
