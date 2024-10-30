from typing import List

from server.schemas.project_schemas import NewProjectRequest, ProjectResponse, ProjectRequest
from server.exceptions import NotFound


class ProjectsService:
    last_id: int = 0
    fake_db: list[dict] = []

    def __init__(self):
        # TODO instanciar repo
        pass

    def create(self, new_project: NewProjectRequest) -> ProjectResponse:
        # TODO instanciar repo
        #! 1. Recibir el objeto de tipo NewProjectResponse, convertirlo a dicc y pasarlo a capa repo
        #! 2. Recibir del repo la respuesta dicc u objeto. Convertirlo a ProjectResponse y retornarlo
        #! Codigo de ejemplo:
        project_dict = self.__fake_create(**project_dict)
        return ProjectResponse(project_dict)

    def get_list(self, limit: int, offset: int) -> ProjectResponse:
        # TODO
        #! 1. Recibir los parametros limit y offset y pasarlos a la capa repo
        #! 2. Recibir la lista de dicc u objetos. convertirlos a una lista de ProjectResponse y retornarlos
        #! Codigo de ejemplo:
        project_list = self.__fake_get_list(limit, offset)
        # list comprenhension
        return [ProjectResponse(**project)for project in project_list]

    def get_by_id(self, id: int) -> ProjectResponse:
        # TODO
        #! 1. Recibir el id de los parametros y pasarlos a repo
        #! 2. REcibimos el objeto o dicc del repo, lo convertimos a un ProjectResponse y lo retornamos
        #! Codigo de ejemplo:
        project = self.__fake_get_by_id(id)
        if project is None:
            raise NotFound(f'Proyecto con id {id} no encontrado')
        return ProjectResponse(**project)

    def update(self, id: int, new_data: ProjectRequest) -> ProjectResponse:
        # TODO
        #! 1. Recibimos los parametros, convertimos el new data a dicc y lo pasamos al repo
        #! 2. Recibimos el objeto o dicc actualizado del repo y lo convertimos ProjectResponse y lo retornamos
        #! Codigo de ejemplo:
        update_project = self.__fake_update(
            id, new_data.model_dump(exclude_none=True))
        if update_project is None:
            raise NotFound(
                f'Proyecto con id {id} no encontrado para actualizarse')
        return ProjectResponse(**update_project)

    def delete(self, id: int) -> None:
        # TODO
        #! 1. Pasamos el id al repo y lo retornamos
        #! Codigo de ejemplo:
        if not self.__fake_delete(id):
            raise NotFound(
                f'Proyecto con id {id} no encontrado para eliminarse')

    # ? FAKE METHODS

    def __fake_create(self, new_project: dict) -> dict:
        from datetime import datetime
        now = datetime.now()
        ProjectsService.last_id += 1
        new_project.update(
            id=ProjectsService.last_id,
            created_at=now,
            update_at=now,
        )
        ProjectsService.fake_db.append(new_project)
        return new_project

    def __fake_get_list(self, limit: int, offset: int) -> list[dict]:
        db_size = len(ProjectsService.fake_db)
        first_index = min(db_size, offset)
        last_index = max(db_size)
        return ProjectsService.fake_db[first_index:last_index]

    def __fake_get_by_id(self, id: int) -> dict | None:
        for project in ProjectsService.fake_db:
            if project['id'] == id:
                return project

    def __fake_update(self, id: int, new_data: dict) -> dict | None:
        from datetime import datetime
        now = datetime.now()
        current_project = self.__fake_get_by_id(id)
        if current_project is None:
            return
        current_project.update(**new_data, update_at=now)
        return current_project

    def __fake_delete(self, id: int) -> bool:
        current_project = self.__fake_get_by_id(id)
        if current_project is None:
            return False
        ProjectsService.fake_db.remove(current_project)
