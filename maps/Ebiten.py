from maps.AbstractGakushoku import AbstractGakushoku


class Ebiten(AbstractGakushoku):
    def get_menu(self) -> str:
        return "えび天丼"

    def get_summary(self) -> str:
        return "ボリューム満点のえび天丼に味噌汁も付いてきます。"

    def get_author(self) -> str:
        return "渡会哲也"
