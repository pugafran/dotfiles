import pickle as pkl
from typing import Optional

from pandas import (
    DataFrame as DataFrame,
    Index as Index,
    Series as Series,
)

def load_reduce(self) -> None: ...
def load_newobj(self) -> None: ...
def load_newobj_ex(self) -> None: ...
def load(fh, encoding: Optional[str] = ..., is_verbose: bool = ...): ...
