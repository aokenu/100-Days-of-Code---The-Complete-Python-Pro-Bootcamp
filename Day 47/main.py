from item_price import PriceTag
from notifier import SendMail

# creating an instance of PriceTag
item_price = PriceTag()

# calling the get_price method from the PriceTag class
price = item_price.get_price()

# creating an object from the SendMail class
notify = SendMail(price)
notify.push_notification()