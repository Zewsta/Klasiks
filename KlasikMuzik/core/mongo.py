from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Mongo Veritabanınıza Bağlanılıyor...‌‌")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Klasik
    LOGGER(__name__).info("Mongo Veritabanınıza Bağlanıldı‌‌.")
except:
    LOGGER(__name__).error("Mongo Veritabanınıza Bağlanılamadı.‌‌")
    exit()

## Klasik Müzik Reklam Aboneliği İçin Veritabanı
MONGODB_CLI = AsyncIOMotorClient(MONGO_DB_URI)
db = MONGODB_CLI["subscriptions"]
