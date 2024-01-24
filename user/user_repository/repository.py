from .repository_interface import UserRepositoryInterface
from django.contrib.auth import get_user_model

class UserRepository(UserRepositoryInterface):
    def get_by_id(self, user_id: str):
        return self.User.objects.get(id=user_id)

    def get_all(self):
        return self.User.objects.all()

    def create(self, data):
        return self.User.objects.create_user(**data)
