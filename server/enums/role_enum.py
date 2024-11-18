from enum import Enum


class RoleEnum(str, Enum):
    SUPER = 'superadmin'
    ADMIN = 'admin'
    COMMON = 'common'


ADMIN_ROLES = [RoleEnum.ADMIN, RoleEnum.SUPER]
COMMON_ROLES = [RoleEnum.COMMON]
ALL_ROLLES = [RoleEnum.ADMIN, RoleEnum.SUPER, RoleEnum.COMMON]
