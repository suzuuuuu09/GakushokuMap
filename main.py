from maps.GakushokuSample import GakushokuSample


data = [GakushokuSample()]

for rank, gakushoku in enumerate(data, start=1):
    print(f"{rank}位: {gakushoku.get_menu()}")
    print(f"  おすすめ理由: {gakushoku.get_summary()}")
    print(f"  作者: {gakushoku.get_author()}")
