"""Added Review model

Revision ID: 1d9956f54e63
Revises: e213ddb2a008
Create Date: 2023-09-04 09:45:31.493566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d9956f54e63'
down_revision = 'e213ddb2a008'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('restaurants')
    op.drop_table('customers')
    # ### end Alembic commands ###
