"""empty message

Revision ID: 5248388d5136
Revises: 319f6c5539d9
Create Date: 2023-10-03 14:50:20.118345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '5248388d5136'
down_revision: Union[str, None] = '319f6c5539d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_password_hashed', sa.Boolean(), server_default=sa.text('0'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_password_hashed')
    # ### end Alembic commands ###