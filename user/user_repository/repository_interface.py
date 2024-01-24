from abc import ABC, abstractmethod
from typing import List
from django.contrib.auth import get_user_model

class UserRepositoryInterface(ABC):
    User = get_user_model()

    @abstractmethod
    def get_by_id(self, user_id: str) -> User:
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def create(self, data) -> User:
        pass

    def update(self, data) -> User:
        pass

    def delete(self, user_id: str) -> None:
        pass
