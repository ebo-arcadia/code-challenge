from dataclasses import dataclass, field
import uuid


@dataclass(order=True, frozen=True)
class Home:
    sort_index: int = field(init=False, repr=False)
    address: str = ""
    year_built: int = 0
    bedroom: int = 0
    listing: list = field(default_factory=list)
    id: str = field(init=False, repr=False, default_factory=uuid.uuid4)

    def __post_init__(self):
        object.__setattr__(self, "sort_index", self.year_built)


home_a = Home(address="1213 Jefferson Blvd", year_built=1920, bedroom=5, listing=["jeff@gmail.com", "Adams@yahoo.com"])
home_b = Home(address="1213 Jefferson Blvd", year_built=2022, bedroom=7, listing=["jeff@gmail.com", "Adams@yahoo.com"])

print(home_a)
print(home_b)
print(home_a > home_b)
