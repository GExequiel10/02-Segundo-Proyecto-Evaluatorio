"""agrega valor por defecto a columna price

Revision ID: 6f4b65a361d4
Revises: 204a2ad6967a
Create Date: 2024-11-15 17:09:07.453244

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f4b65a361d4'
down_revision: Union[str, None] = '204a2ad6967a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###