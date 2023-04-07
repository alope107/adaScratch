from datetime import datetime

class Person:
    def __init__(self, birth_year, subscriptions=None):
        self.birth_year = birth_year
        current_year = datetime.now().year
        self.age = current_year - birth_year
        if subscriptions is None:
            subscriptions = []
        self.subscriptions = subscriptions

    def subscribe(self, subscription):
        self.subscriptions.append(subscription)

    def bill(self):
        total = 0.0
        for subscription in self.subscriptions:
            total += subscription.price
        return total