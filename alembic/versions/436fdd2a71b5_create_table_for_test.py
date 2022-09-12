"""create table for test

Revision ID: 436fdd2a71b5
Revises: 
Create Date: 2022-09-10 12:55:08.559508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '436fdd2a71b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'poc_service_python_tbl_test',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(), nullable=False),
        sa.Column('descricao', sa.String(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('poc_service_python_tbl_test')
