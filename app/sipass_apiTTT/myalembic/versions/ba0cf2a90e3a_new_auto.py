"""new_auto

Revision ID: ba0cf2a90e3a
Revises: 16413da9f2f7
Create Date: 2022-11-28 18:24:18.890564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba0cf2a90e3a'
down_revision = '16413da9f2f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('signup', sa.Column('yes_name', sa.String(length=33), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('signup', 'yes_name')
    # ### end Alembic commands ###