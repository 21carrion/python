from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "ул. Ленина", "10", "25")
from_addr = Address("654321", "Санкт-Петербург", "Невский пр.", "5", "12")

my_mailing = Mailing(to_addr, from_addr, 350, "TR123456789")

print(
    f"Отправление {my_mailing.track} "
    f"из {my_mailing.from_address.index}, {my_mailing.from_address.city}, "
    f"{my_mailing.from_address.street}, {my_mailing.from_address.house} - "
    f"{my_mailing.from_address.apartment} "
    f"в {my_mailing.to_address.index}, {my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, {my_mailing.to_address.house} - "
    f"{my_mailing.to_address.apartment}. "
    f"Стоимость {my_mailing.cost} рублей."
)
