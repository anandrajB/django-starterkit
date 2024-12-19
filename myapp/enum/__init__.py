from enum import StrEnum


class BaseEnum(StrEnum):

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return f"{self.value}"

    def __eq__(self, other: object) -> bool:
        return self.value == other if isinstance(other, str) else super().__eq__(other)
