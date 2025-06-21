from decimal import Decimal, ROUND_HALF_UP


def round_decimal(value, places):
    return float(Decimal(value).quantize(Decimal(10) ** -places, rounding=ROUND_HALF_UP))


def get_key_from_value(dct, value):
    for k, v in dct.items():
        if v == value:
            return k
    return None


def find_path(details):
    while True:
        max_val = max(details.values())
        min_val = min(details.values())

        if round_decimal(max_val, 2) == round_decimal(min_val, 2):
            break

        max_key = get_key_from_value(details, max_val)
        min_key = get_key_from_value(details, min_val)

        result = round_decimal(max_val + min_val, 1)

        if result >= 0.0:
            print(f"{min_key} needs to pay {max_key}: {round_decimal(abs(min_val), 2)}")
            details[max_key] = result
            details[min_key] = 0.0
        else:
            print(f"{min_key} needs to pay {max_key}: {round_decimal(abs(max_val), 2)}")
            details[max_key] = 0.0
            details[min_key] = result


if __name__ == "__main__":
    balances = {
        "A": -5.0,
        "B": 25.0,
        "C": -20.0,
        "D": 25.0,
        "E": -20.0,
        "F": -5.0
    }

    find_path(balances)
