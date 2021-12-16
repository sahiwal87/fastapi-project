"""add content column to posts table

Revision ID: 1255a5816db8
Revises: 8e6f46e855d4
Create Date: 2021-12-13 15:25:28.057873

"""
from sqlalchemy.sql.expression import null
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1255a5816db8'
down_revision = '8e6f46e855d4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
