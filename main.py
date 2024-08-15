"""main module"""


def main() -> None:
    """main function"""
    tables = [
        {
            "id": 1,
            "pos": 2,
            "is_free": True,
        },
        {
            "id": 2,
            "pos": 2,
            "is_free": False,
        },
    ]
    book_the_table(tables, 1)


def book_the_table(
    tables: list[dict[str, int | bool]],
    number: int,
) -> None:
    """books the table by number

    Args:
        tables (list[dict[str, int | bool]]): list of tables
        number (int): number of table
    """
    for table in tables:
        if table.get("id") == number:
            if not table.get("is_free"):
                raise PermissionError("Столик вже був зайнятий")
            table["is_free"] = not table.get("is_free")
            print("Столик тепер зайнятий :)")
            break


if __name__ == "__main__":
    main()
