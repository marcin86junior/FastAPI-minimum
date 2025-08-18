"""Feat: added product model

Revision ID: 75f4d074a111
Revises: 4a23ff369947
Create Date: 2025-08-18 08:28:55.634752

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75f4d074a111'
down_revision: Union[str, None] = '4a23ff369947'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Tworzenie tabeli `products`
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('name', sa.String(), unique=True, nullable=False),
        sa.Column('sku', sa.String(), unique=True, nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('description', sa.String(length=300), nullable=True),
    )

    # Tworzenie tabeli `tags`
    op.create_table(
        'tags',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('name', sa.String(), unique=True, nullable=False),
    )

    # Tworzenie tabeli pośredniej `product_tags`
    op.create_table(
        'product_tags',
        sa.Column('product_id', sa.Integer(), sa.ForeignKey('products.id'), primary_key=True),
        sa.Column('tag_id', sa.Integer(), sa.ForeignKey('tags.id'), primary_key=True),
    )


def downgrade() -> None:
    # Usuwanie tabel w odwrotnej kolejności
    op.drop_table('product_tags')
    op.drop_table('tags')
    op.drop_table('products')
