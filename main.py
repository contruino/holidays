import holidays as hd

for ptr in hd.UnitedKingdom(years=2023).items():
    print(ptr)
    print('----------')
    print(hd.UnitedKingdom().country)
    print('----------')
    print(hd.UnitedKingdom().get('01-01-2023'))
