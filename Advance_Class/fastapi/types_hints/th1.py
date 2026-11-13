def get_full_name(first_name: str, last_name: str) -> str:
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("tony", "stark"))
print(get_full_name("steve", "rogers"))


def get_info(name:str, age:int) -> str:
    info = name.title() + " is old: " + str(age)
    return info

print(get_info("tony", 45))


from typing import Any

def test(data: Any) -> Any:
    return data

print(test("Hello"))


# Collection or Generic Type Hints

def process_items(items: list[str]) -> None:
    for item in items:
        print(item)

process_items(["ironman", "captain america", "thor"])


def process_items1(items_t: tuple[int, int, str], items_s: set[str]) -> tuple[tuple[int, int, str], set[str]]:
    return items_t, items_s


processed_items = process_items1((1, 2, "three"), {"four", "five", "six"})
print(processed_items)


def process_items2(items_d: dict[str, int]):
    for item_name, item_value in items_d.items():
        print(f"{item_name}: {item_value}")

process_items2({"ironman": 1, "captain america": 2, "thor": 3})


def process_items3(items_l: list[dict[str, int | str]]) -> None:
    print("Processing items...")
    for item in items_l:
        for key, value in item.items():
            print(f"{key}: {value}")

process_items3([
    {"name": "ironman", "power": 100},
    {"name": "captain america", "power": 80},
    {"name": "thor", "power": "120"}
])


def test3(items: int | str):
    print(f"Item: {items}")

test3(42)
test3("Hello")



