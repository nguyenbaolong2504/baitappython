_list= [1, 2, 3, 4, 5, 6, 7, 8, 9]
tich_chan =([x for x in _list if x % 2 == 0])
print(" các số chẵn trong danh sách:", tich_chan)
tich_le = ([x for x in _list if x % 2 != 0])
print(" các số lẻ trong danh sách:", tich_le)