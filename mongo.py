from django.conf import settings
from pymongo import MongoClient

class MongoConn(object):
    clients = {}

    @classmethod
    def client(cls, name='default'):
        if name not in cls.clients:
            if name not in settings.MONGODB:
                return None
            cls.clients[name] = cls(settings.MONGODB.get(name))
        return cls.clients.get(name)

    def __init__(self, db_config):
        self.conn = MongoClient(host=db_config.get('HOST'), port=db_config.get('PORT'))
        self.db_name = db_config.get('NAME')
        self._db = None

    @property
    def db(self):
        if not self._db:
            self._db = self.get_db()
        return self._db

    def get_db_name(self):
        """
        :rtype: string
        """
        return self.db_name
        
    
    def get_db(self, db_name=None):
        """
        :param db_name:
        :rtype: pymongo.database.Database
        """
        return self.conn[db_name or self.get_db_name()]

    def get_collection(self, collection_name):
        """
        :param string collection_name:
        :rtype: pymongo.collection.Collection
        """
        return self.db[collection_name]