"""empty message

Revision ID: d9bdee640b78
Revises: 
Create Date: 2021-02-02 12:19:54.726982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9bdee640b78'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('franchisor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('franchisor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['franchisor_id'], ['franchisor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_people_email'), 'people', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_people_email'), table_name='people')
    op.drop_table('people')
    op.drop_table('franchisor')
    # ### end Alembic commands ###
