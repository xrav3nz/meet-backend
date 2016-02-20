"""empty message

Revision ID: deee47c866e1
Revises: 8fd9092f7d83
Create Date: 2016-02-20 17:20:26.603261

"""

# revision identifiers, used by Alembic.
revision = 'deee47c866e1'
down_revision = '8fd9092f7d83'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meetups', sa.Column('password', sa.String(length=9), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('meetups', 'password')
    ### end Alembic commands ###