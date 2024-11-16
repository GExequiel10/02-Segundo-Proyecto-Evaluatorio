from typing import List

from server.schemas.user_schemas import NewUserRequest, UserResponse, UserRequest
from server.exceptions import NotFound
from server.repository import UsersRepository


class UsersService:

    def __init__(self):
        self.user_repo = UsersRepository()

    def create(self, new_user: NewUserRequest) -> UserResponse:
        user_dict = self.user_repo.create(new_user.model_dump())
        return UserResponse(**user_dict)

    def get_list(self, limit: int, offset: int) -> List[UserResponse]:
        user_list = self.user_repo.get_list(limit, offset)
        return [UserResponse(**user)for user in user_list]

    def get_by_id(self, id: int) -> UserResponse:
        user = self.user_repo.get_by_id(id)
        if user is None:
            raise NotFound(f'Usuario con id {id} no encontrado')
        return UserResponse(**user)

    def update(self, id: int, new_data: UserRequest) -> UserResponse:
        update_user = self.user_repo.update(
            id, new_data.model_dump(exclude_none=True))
        if update_user is None:
            raise NotFound(
                f'Usuario con id {id} no encontrado para actualizarse')
        return UserResponse(**update_user)

    def delete(self, id: int) -> None:
        if not self.user_repo.delete(id):
            raise NotFound(
                f'Usuario con id {id} no encontrado para eliminarse')
