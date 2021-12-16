"""add user table

Revision ID: af9c6959e6e0
Revises: 1255a5816db8
Create Date: 2021-12-13 15:33:27.409136

"""
from sqlalchemy.sql.schema import PrimaryKeyConstraint, UniqueConstraint
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af9c6959e6e0'
down_revision = '1255a5816db8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), 
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
                              
    pass

def downgrade():
    op.drop_table('users')
    pass
