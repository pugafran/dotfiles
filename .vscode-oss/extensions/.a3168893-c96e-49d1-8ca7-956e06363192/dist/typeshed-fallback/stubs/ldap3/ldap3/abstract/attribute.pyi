from typing import Any

class Attribute:
    key: Any
    definition: Any
    values: Any
    raw_values: Any
    response: Any
    entry: Any
    cursor: Any
    other_names: Any
    def __init__(self, attr_def, entry, cursor) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, item): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @property
    def value(self): ...

class OperationalAttribute(Attribute): ...

class WritableAttribute(Attribute):
    def __iadd__(self, other): ...
    def __isub__(self, other): ...
    def add(self, values) -> None: ...
    def set(self, values) -> None: ...
    def delete(self, values) -> None: ...
    def remove(self) -> None: ...
    def discard(self) -> None: ...
    @property
    def virtual(self): ...
    @property
    def changes(self): ...
