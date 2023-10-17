class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if not set(self.card_num).issubset(set(" 1234567890")):
            return False

        card_num = "".join(self.card_num.split(" "))

        if len(card_num) <= 1:
            return False

        total = 0
        for n in card_num[-2::-2]:
            to_add = 2 * int(n)
            if to_add > 9:
                to_add -= 9
            total += to_add

        for n in card_num[-1::-2]:
            total += int(n)

        if total % 10 != 0:
            return False

        return True
