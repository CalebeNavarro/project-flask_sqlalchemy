"""columns weight, height, length, width altered for not null

Revision ID: 00fbdb3c3ccc
Revises: 9a6c8eb30815
Create Date: 2021-10-18 14:33:11.779427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00fbdb3c3ccc'
down_revision = '9a6c8eb30815'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("UPDATE products SET weight = '' WHERE weight is NULL")
    op.execute("UPDATE products SET height = '' WHERE height is NULL")
    op.execute("UPDATE products SET length = '' WHERE length is NULL")
    op.execute("UPDATE products SET width = '' WHERE width is NULL")
    op.alter_column('products', 'weight',
               existing_type=sa.VARCHAR(length=16),
               nullable=False)
    op.alter_column('products', 'height',
               existing_type=sa.VARCHAR(length=16),
               nullable=False)
    op.alter_column('products', 'length',
               existing_type=sa.VARCHAR(length=16),
               nullable=False)
    op.alter_column('products', 'width',
               existing_type=sa.VARCHAR(length=16),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shipping_companies', 'minimum_shipping_price',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('products', 'width',
               existing_type=sa.VARCHAR(length=16),
               nullable=True)
    op.alter_column('products', 'length',
               existing_type=sa.VARCHAR(length=16),
               nullable=True)
    op.alter_column('products', 'height',
               existing_type=sa.VARCHAR(length=16),
               nullable=True)
    op.alter_column('products', 'weight',
               existing_type=sa.VARCHAR(length=16),
               nullable=True)
    # ### end Alembic commands ###
