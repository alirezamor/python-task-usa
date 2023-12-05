"""create_task_table

Revision ID: c2972ae42a74
Revises: 9128849f73f2
Create Date: 2023-12-05 12:39:53.208898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision: str = 'c2972ae42a74'
down_revision: Union[str, None] = '9128849f73f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False),
        sa.Column('status', sa.String, nullable=False),
        sa.Column('custom_fields', JSONB, nullable=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
    )

    # Create an index on custom_fields->>'name'
    op.create_index('idx_custom_fields_name', 'tasks', [sa.text("(custom_fields->>'name')")], postgresql_using='gin')
    #
    # Create an index on the name field
    op.create_index('idx_task_name', 'tasks', ['name'])

    # Ensure there's an index on the foreign key
    op.create_index('idx_task_user_id', 'tasks', ['user_id'])

    # Ensure there's an index on the status
    op.create_index('idx_task_status', 'tasks', ['status'])


def downgrade() -> None:
    op.drop_index('idx_custom_fields_name', 'tasks')
    op.drop_index('idx_task_name', 'tasks')
    op.drop_index('idx_task_user_id', 'tasks')
    op.drop_index('status', 'tasks')
    op.drop_table('tasks')
