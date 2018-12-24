from app import db

class BaseDocument(db.Document):
    meta = {'abstract': True}

    @property
    def get_id(self):
        return str(self.id)


    @classmethod
    def post(cls, params):
        return cls(**params).save()

    @classmethod
    def get(cls, id):
        resource = cls.objects(id=id).first()
        if not resource:
            raise ValueError(f'{cls.__name__} does not exist')

        return resource

    @classmethod
    def update(cls, id, params):
        resource = cls.get(id)
        return resource.update_one(**params)

    @classmethod
    def index(cls):
        return cls.objects()

    @classmethod
    def delete(cls, id):
        resource = cls.get(id)
        resource.delete()
