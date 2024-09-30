from abc import ABC, abstractmethod

class CacheAbstract(ABC):
    """Cache operations abstraction."""

    @abstractmethod
    async def get(self, key: str):
        """Get value by key."""

    @abstractmethod
    async def set(self, key: str, value: any, ttl: int):
        """Set value with TTL."""
