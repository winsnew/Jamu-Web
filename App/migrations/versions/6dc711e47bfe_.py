"""empty message

Revision ID: 6dc711e47bfe
Revises: 
Create Date: 2023-05-03 10:57:03.708451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dc711e47bfe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('createdAt', sa.Integer(), nullable=True),
    sa.Column('updateAt', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_product_id'), ['id'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('createdAt', sa.Integer(), nullable=True),
    sa.Column('updateAt', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_id'))

    op.drop_table('user')
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_product_id'))

    op.drop_table('product')
    # ### end Alembic commands ###
