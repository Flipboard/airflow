#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""add priority_weight_strategy to task_instance

Revision ID: 624ecf3b6a5e
Revises: bd5dfbe21f88
Create Date: 2023-10-29 02:01:34.774596

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "624ecf3b6a5e"
down_revision = "bd5dfbe21f88"
branch_labels = None
depends_on = None
airflow_version = "2.8.0"


def upgrade():
    """Apply add priority_weight_strategy to task_instance"""
    with op.batch_alter_table("task_instance") as batch_op:
        batch_op.add_column(sa.Column("priority_weight_strategy", sa.String(length=1000)))


def downgrade():
    """Unapply add priority_weight_strategy to task_instance"""
    with op.batch_alter_table("task_instance") as batch_op:
        batch_op.drop_column("priority_weight_strategy")
