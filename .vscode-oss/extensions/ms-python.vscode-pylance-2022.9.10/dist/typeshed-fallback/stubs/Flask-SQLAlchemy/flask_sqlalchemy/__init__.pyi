from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Generic, TypeVar

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.query import Query
from sqlalchemy.orm.session import Session

from . import utils as utils
from .model import DefaultMeta as DefaultMeta, Model as Model

models_committed: Any
before_models_committed: Any

class SignallingSession(Session):
    app: Any
    def __init__(self, db, autocommit: bool = ..., autoflush: bool = ..., **options) -> None: ...
    def get_bind(self, mapper: Any | None = ..., clause: Any | None = ...): ...  # type: ignore[override]

def get_debug_queries(): ...

_T = TypeVar("_T")

class BaseQuery(Query[_T]):
    def get_or_404(self, ident, description: Incomplete | None = ...): ...
    def first_or_404(self, description: Incomplete | None = ...): ...
    def paginate(
        self,
        page: Incomplete | None = ...,
        per_page: Incomplete | None = ...,
        error_out: bool = ...,
        max_per_page: Incomplete | None = ...,
    ) -> Pagination[_T]: ...

class Pagination(Generic[_T]):
    query: BaseQuery[_T] | None
    page: int
    per_page: int
    total: int | None
    items: Any
    def __init__(self, query: BaseQuery[_T] | None, page: int, per_page: int, total: int | None, items) -> None: ...
    @property
    def pages(self) -> int: ...
    def prev(self, error_out: bool = ...) -> Pagination[_T]: ...
    @property
    def prev_num(self) -> int | None: ...
    @property
    def has_prev(self) -> bool: ...
    def next(self, error_out: bool = ...) -> Pagination[_T]: ...
    @property
    def has_next(self) -> bool: ...
    @property
    def next_num(self) -> int | None: ...
    def iter_pages(
        self, left_edge: int = ..., left_current: int = ..., right_current: int = ..., right_edge: int = ...
    ) -> Generator[int | None, None, None]: ...

def get_state(app): ...

class SQLAlchemy:
    Query: Any
    use_native_unicode: Any
    session: scoped_session
    Model: Model
    app: Any
    def __init__(
        self,
        app: Any | None = ...,
        use_native_unicode: bool = ...,
        session_options: Any | None = ...,
        metadata: Any | None = ...,
        query_class=...,
        model_class=...,
        engine_options: Any | None = ...,
    ) -> None: ...
    @property
    def metadata(self): ...
    def create_scoped_session(self, options: Any | None = ...): ...
    def create_session(self, options): ...
    def make_declarative_base(self, model, metadata: Any | None = ...): ...
    def init_app(self, app): ...
    def apply_pool_defaults(self, app, options): ...
    def apply_driver_hacks(self, app, sa_url, options): ...
    @property
    def engine(self): ...
    def make_connector(self, app: Any | None = ..., bind: Any | None = ...): ...
    def get_engine(self, app: Any | None = ..., bind: Any | None = ...): ...
    def create_engine(self, sa_url, engine_opts): ...
    def get_app(self, reference_app: Any | None = ...): ...
    def get_tables_for_bind(self, bind: Any | None = ...): ...
    def get_binds(self, app: Any | None = ...): ...
    def create_all(self, bind: str = ..., app: Any | None = ...) -> None: ...
    def drop_all(self, bind: str = ..., app: Any | None = ...) -> None: ...
    def reflect(self, bind: str = ..., app: Any | None = ...) -> None: ...
    def __getattr__(self, name: str) -> Any: ...  # exposes dynamically classes of SQLAlchemy

class FSADeprecationWarning(DeprecationWarning): ...
