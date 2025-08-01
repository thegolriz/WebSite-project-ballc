"""Initial migration

Revision ID: 40eb010d589f
Revises: 
Create Date: 2025-03-23 00:34:57.972532

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "40eb010d589f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=150), nullable=True),
        sa.Column("password", sa.String(length=150), nullable=True),
        sa.Column("first_name", sa.String(length=150), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )

    with op.batch_alter_table("note", schema=None) as batch_op:
        batch_op.alter_column(
            "date",
            existing_type=postgresql.TIMESTAMP(),
            type_=sa.DateTime(timezone=True),
            existing_nullable=True,
            existing_server_default=sa.text("now()"),
        )
        batch_op.drop_constraint("note_user_id_fkey", type_="foreignkey")
        batch_op.create_foreign_key(None, "user", ["user_id"], ["id"])

    op.drop_table("users")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("note", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.create_foreign_key(
            "note_user_id_fkey", "users", ["user_id"], ["id"], ondelete="CASCADE"
        )
        batch_op.alter_column(
            "date",
            existing_type=sa.DateTime(timezone=True),
            type_=postgresql.TIMESTAMP(),
            existing_nullable=True,
            existing_server_default=sa.text("now()"),
        )

    op.create_table(
        "users",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("email", sa.VARCHAR(length=150), autoincrement=False, nullable=False),
        sa.Column(
            "password", sa.VARCHAR(length=150), autoincrement=False, nullable=False
        ),
        sa.Column(
            "first_name", sa.VARCHAR(length=150), autoincrement=False, nullable=False
        ),
        sa.PrimaryKeyConstraint("id", name="users_pkey"),
        sa.UniqueConstraint("email", name="users_email_key"),
    )

    # ### end Alembic commands ###
