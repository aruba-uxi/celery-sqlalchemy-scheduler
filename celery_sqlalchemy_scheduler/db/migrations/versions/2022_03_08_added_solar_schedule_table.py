"""added solar schedule table

Revision ID: bc68e9cf43a6
Revises: d059fa14cb14
Create Date: 2022-03-08 10:04:25.882967

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "bc68e9cf43a6"
down_revision = "d059fa14cb14"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "celery_solar_schedule",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("event", sa.String(length=24), nullable=True),
        sa.Column("latitude", sa.Float(), nullable=True),
        sa.Column("longitude", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        schema="scheduler",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("celery_solar_schedule", schema="scheduler")
    # ### end Alembic commands ###
