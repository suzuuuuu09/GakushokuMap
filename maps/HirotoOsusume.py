from maps.AbstractGakushoku import AbstractGakushoku


class HirotoOsusume(AbstractGakushoku):
    def get_menu(self) -> str:
        return "セブンイレブン：たんぱく質が摂れるチキン＆チリ"

    def get_summary(self) -> str:
        return "シンプルな味だが、チリの味がおいしい"

    def get_author(self) -> str:
        return "ヒロト"
