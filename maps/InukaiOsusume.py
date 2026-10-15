from maps.AbstractGakushoku import AbstractGakushoku


class InukaiOsusume(AbstractGakushoku):
    def get_menu(self) -> str:
        return "セブンイレブンのさけるチーズ"

    def get_summary(self) -> str:
        return "チーズっておいしいよね"

    def get_author(self) -> str:
        return "犬飼"
