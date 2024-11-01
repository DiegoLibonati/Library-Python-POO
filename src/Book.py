class Book:
    def __init__(
        self, name: str, description: str,
        author: str, units: int, banner_url: str = ""
    ) -> None:
        self.__name = name
        self.__description = description
        self.__author = author
        self.__units = units
        self.__banner_url = banner_url

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def author(self) -> str:
        return self.__author
    
    @property
    def units(self) -> int:
        return self.__units
    
    @property
    def banner_url(self) -> str:
        return self.__banner_url
    
    @property
    def stock(self) -> bool:
        return bool(self.units)
    
    def __str__(self) -> str:
        print(f"----- Book {self.name} -----")
        return (
            f"Book Name: {self.name}\n"
            f"Book Description: {self.description}\n"
            f"Book Author: {self.author}\n"
            f"Book Units: {self.units}\n"
            f"Book Banner: {self.banner_url}\n\n"
        )

    def decrease_unit(self) -> None:
        if not self.stock: return

        new_units = self.units - 1

        if new_units <= 0:
            self.__units = 0
            return

        self.__units = new_units

    def increase_unit(self) -> None:
        self.__units += 1

    def edit_banner(self, banner_url: str) -> None:
        self.__banner_url = banner_url

def main() -> None:
    book = Book(name="Drácula", description="Es una novela de fantasía gótica escrita por Bram Stoker, publicada en 1897.", author="Bram Stoker", units=20)
    print(book)


if __name__ == "__main__":
    main()