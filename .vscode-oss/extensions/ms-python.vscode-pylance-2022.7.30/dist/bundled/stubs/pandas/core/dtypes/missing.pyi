from typing import (
    List,
    Union,
    overload,
)

import numpy as np

from pandas._typing import (
    ArrayLike as ArrayLike,
    DataFrame as DataFrame,
    Index as Index,
    Scalar as Scalar,
    Series as Series,
)

isposinf_scalar = ...
isneginf_scalar = ...

@overload
def isna(obj: DataFrame) -> DataFrame: ...
@overload
def isna(obj: Series) -> Series[bool]: ...
@overload
def isna(obj: Union[Index, List, ArrayLike]) -> np.ndarray: ...
@overload
def isna(obj: Scalar) -> bool: ...

isnull = isna

@overload
def notna(obj: DataFrame) -> DataFrame: ...
@overload
def notna(obj: Series) -> Series[bool]: ...
@overload
def notna(obj: Union[Index, List, ArrayLike]) -> np.ndarray: ...
@overload
def notna(obj: Scalar) -> bool: ...

notnull = notna

def array_equivalent(left, right, strict_nan: bool = ...) -> bool: ...
def na_value_for_dtype(dtype, compat: bool = ...): ...
def remove_na_arraylike(arr): ...
def is_valid_nat_for_dtype(obj, dtype) -> bool: ...
