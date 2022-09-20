from typing import (
    Any,
    Mapping,
    Sequence,
)

from pandas.core.base import PandasObject
from pandas.core.frame import DataFrame

class DatabaseError(IOError): ...

def execute(sql, con, cur=..., params=...): ...
def read_sql_table(
    table_name: str,
    con,
    schema: str | None = ...,
    index_col: str | Sequence[str] | None = ...,
    coerce_float: bool = ...,
    parse_dates: Sequence[str] | Mapping[str, str] | None = ...,
    columns: Sequence[str] | None = ...,
    chunksize: int | None = ...,
) -> DataFrame: ...
def read_sql_query(
    sql,
    con,
    schema: str | None = ...,
    index_col: str | Sequence[str] | None = ...,
    coerce_float: bool = ...,
    params=...,
    parse_dates: Sequence[str] | Mapping[str, str] | None = ...,
    chunksize: int | None = ...,
) -> DataFrame: ...
def read_sql(
    sql: str | Any,
    con: str | Any,
    index_col: str | Sequence[str] | None = ...,
    coerce_float: bool = ...,
    params: Sequence[str] | tuple[str, ...] | Mapping[str, str] | None = ...,
    parse_dates: Sequence[str]
    | Mapping[str, str]
    | Mapping[str, Mapping[str, Any]]
    | None = ...,
    columns: Sequence[str] = ...,
    chunksize: int = ...,
) -> DataFrame: ...
def to_sql(
    frame,
    name,
    con,
    schema=...,
    if_exists: str = ...,
    index: bool = ...,
    index_label=...,
    chunksize=...,
    dtype=...,
    method=...,
) -> None: ...
def has_table(table_name, con, schema=...): ...

table_exists = has_table

def pandasSQL_builder(con, schema=..., meta=..., is_cursor: bool = ...): ...

class SQLTable(PandasObject):
    name = ...
    pd_sql = ...
    prefix = ...
    frame = ...
    index = ...
    schema = ...
    if_exists = ...
    keys = ...
    dtype = ...
    table = ...
    def __init__(
        self,
        name,
        pandas_sql_engine,
        frame=...,
        index: bool = ...,
        if_exists: str = ...,
        prefix: str = ...,
        index_label=...,
        schema=...,
        keys=...,
        dtype=...,
    ) -> None: ...
    def exists(self): ...
    def sql_schema(self): ...
    def create(self) -> None: ...
    def insert_data(self): ...
    def insert(self, chunksize=..., method=...) -> None: ...
    def read(
        self, coerce_float: bool = ..., parse_dates=..., columns=..., chunksize=...
    ): ...

class PandasSQL(PandasObject):
    def read_sql(self, *args, **kwargs) -> None: ...
    def to_sql(
        self,
        frame,
        name,
        if_exists: str = ...,
        index: bool = ...,
        index_label=...,
        schema=...,
        chunksize=...,
        dtype=...,
        method=...,
    ) -> None: ...

class SQLDatabase(PandasSQL):
    connectable = ...
    meta = ...
    def __init__(self, engine, schema=..., meta=...) -> None: ...
    def run_transaction(self) -> None: ...
    def execute(self, *args, **kwargs): ...
    def read_table(
        self,
        table_name,
        index_col=...,
        coerce_float: bool = ...,
        parse_dates=...,
        columns=...,
        schema=...,
        chunksize=...,
    ): ...
    def read_query(
        self,
        sql,
        index_col=...,
        coerce_float: bool = ...,
        parse_dates=...,
        params=...,
        chunksize=...,
    ): ...
    def to_sql(
        self,
        frame,
        name,
        if_exists: str = ...,
        index: bool = ...,
        index_label=...,
        schema=...,
        chunksize=...,
        dtype=...,
        method=...,
    ) -> None: ...
    @property
    def tables(self): ...
    def has_table(self, name, schema=...): ...
    def get_table(self, table_name, schema=...): ...
    def drop_table(self, table_name, schema=...) -> None: ...

class SQLiteTable(SQLTable):
    def __init__(self, *args, **kwargs): ...
    def sql_schema(self): ...
    def insert_statement(self): ...

class SQLiteDatabase(PandasSQL):
    is_cursor = ...
    con = ...
    def __init__(self, con, is_cursor: bool = ...) -> None: ...
    def run_transaction(self) -> None: ...
    def execute(self, *args, **kwargs): ...
    def read_query(
        self,
        sql,
        index_col=...,
        coerce_float: bool = ...,
        params=...,
        parse_dates=...,
        chunksize=...,
    ): ...
    def to_sql(
        self,
        frame,
        name,
        if_exists: str = ...,
        index: bool = ...,
        index_label=...,
        schema=...,
        chunksize=...,
        dtype=...,
        method=...,
    ) -> None: ...
    def has_table(self, name, schema=...): ...
    def get_table(self, table_name, schema=...) -> None: ...
    def drop_table(self, name, schema=...) -> None: ...

def get_schema(frame, name, keys=..., con=..., dtype=...): ...
