from gorod import Address
from pochta import Mailing

adres1 = Address('445000', 'Тольятти', 'Ленина', '25', '47')
adres2 = Address('440000', 'Пенза', 'Кленовый б-р', '31', '5')

to_address = adres1
from_address = adres2

pochta = Mailing(to_address, from_address)
pochta.track('DF3546', 4583)
