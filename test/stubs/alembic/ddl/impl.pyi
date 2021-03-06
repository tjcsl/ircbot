# Stubs for alembic.ddl.impl (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..util import sqla_compat
from ..util.compat import string_types, text_type, with_metaclass
from typing import Any, Optional


class ImplMeta(type):

    def __init__(cls, classname: Any, bases: Any, dict_: Any) -> None:
        ...


class DefaultImpl:
    __dialect__: str = ...
    transactional_ddl: bool = ...
    command_terminator: str = ...
    dialect: Any = ...
    connection: Any = ...
    as_sql: Any = ...
    literal_binds: Any = ...
    output_buffer: Any = ...
    memo: Any = ...
    context_opts: Any = ...

    def __init__(self, dialect: Any, connection: Any, as_sql: Any, transactional_ddl: Any, output_buffer: Any, context_opts: Any) -> None:
        ...

    @classmethod
    def get_by_dialect(cls, dialect: Any):
        ...

    def static_output(self, text: Any) -> None:
        ...

    def requires_recreate_in_batch(self, batch_op: Any):
        ...

    def prep_table_for_batch(self, table: Any) -> None:
        ...

    @property
    def bind(self):
        ...

    def execute(self, sql: Any, execution_options: Optional[Any] = ...) -> None:
        ...

    def alter_column(self,
                     table_name: Any,
                     column_name: Any,
                     nullable: Optional[Any] = ...,
                     server_default: bool = ...,
                     name: Optional[Any] = ...,
                     type_: Optional[Any] = ...,
                     schema: Optional[Any] = ...,
                     autoincrement: Optional[Any] = ...,
                     comment: bool = ...,
                     existing_comment: Optional[Any] = ...,
                     existing_type: Optional[Any] = ...,
                     existing_server_default: Optional[Any] = ...,
                     existing_nullable: Optional[Any] = ...,
                     existing_autoincrement: Optional[Any] = ...) -> None:
        ...

    def add_column(self, table_name: Any, column: Any, schema: Optional[Any] = ...) -> None:
        ...

    def drop_column(self, table_name: Any, column: Any, schema: Optional[Any] = ..., **kw: Any) -> None:
        ...

    def add_constraint(self, const: Any) -> None:
        ...

    def drop_constraint(self, const: Any) -> None:
        ...

    def rename_table(self, old_table_name: Any, new_table_name: Any, schema: Optional[Any] = ...) -> None:
        ...

    def create_table(self, table: Any) -> None:
        ...

    def drop_table(self, table: Any) -> None:
        ...

    def create_index(self, index: Any) -> None:
        ...

    def create_table_comment(self, table: Any) -> None:
        ...

    def drop_table_comment(self, table: Any) -> None:
        ...

    def create_column_comment(self, column: Any) -> None:
        ...

    def drop_index(self, index: Any) -> None:
        ...

    def bulk_insert(self, table: Any, rows: Any, multiinsert: bool = ...) -> None:
        ...

    def compare_type(self, inspector_column: Any, metadata_column: Any):
        ...

    def compare_server_default(self, inspector_column: Any, metadata_column: Any, rendered_metadata_default: Any, rendered_inspector_default: Any):
        ...

    def correct_for_autogen_constraints(self, conn_uniques: Any, conn_indexes: Any, metadata_unique_constraints: Any, metadata_indexes: Any) -> None:
        ...

    def render_ddl_sql_expr(self, expr: Any, is_server_default: bool = ..., **kw: Any):
        ...

    def correct_for_autogen_foreignkeys(self, conn_fks: Any, metadata_fks: Any) -> None:
        ...

    def autogen_column_reflect(self, inspector: Any, table: Any, column_info: Any) -> None:
        ...

    def start_migrations(self) -> None:
        ...

    def emit_begin(self) -> None:
        ...

    def emit_commit(self) -> None:
        ...

    def render_type(self, type_obj: Any, autogen_context: Any):
        ...
