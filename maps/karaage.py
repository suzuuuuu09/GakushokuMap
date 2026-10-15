from maps.AbstractGakushoku import AbstractGakushoku


class Karaage(AbstractGakushoku):
    def get_menu(self) -> str:
        return "からあげ定食"

    def get_summary(self) -> str:
        return "濃厚な特選だれでご飯が進み、ボリュームもある架空のおすすめです。"

    def get_author(self) -> str:
        return "みなと"
