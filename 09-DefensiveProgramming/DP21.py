def iloczyn_zbiorow(zbior1, zbior2):
    assert type(zbior1) == set and type(zbior2) == set
    return zbior1 & zbior2

print(iloczyn_zbiorow({1,2,3},{2,3,4,5}))    