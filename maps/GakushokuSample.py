from maps.AbstractGakushoku import AbstractGakushoku


class GakushokuSample(AbstractGakushoku):
    def get_menu(self) -> str:
        return "味噌カツ定食"

    def get_summary(self) -> str:
        return "濃厚な味噌だれでご飯が進み、ボリュームもある架空のおすすめです。"

    def get_author(self) -> str:
        return "サンプル"
