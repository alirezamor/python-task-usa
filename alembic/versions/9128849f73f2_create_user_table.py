"""create_user_table

Revision ID: 9128849f73f2
Revises: 
Create Date: 2023-12-05 12:38:39.792091

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9128849f73f2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')
