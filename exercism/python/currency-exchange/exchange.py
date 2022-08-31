def exchange_money(budget: float, exchange_rate: float)-> float:
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget/exchange_rate


def get_change(budget: float, exchanging_value: int) -> float:
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    
    return budget - exchanging_value

def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return int(number_of_bills*denomination)

def get_number_of_bills(budget: int, denomination: int) -> int:
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return int(budget/denomination)


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    exmoney = exchange_money(budget, exchange_rate)-spread
    num_bills = get_number_of_bills(exmoney,denomination)
    return get_value_of_bills(denomination,num_bills)



def non_exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    exmoney = exchange_money(budget, exchange_rate)-spread
    num_bills = get_number_of_bills(exmoney,denomination)
    exchangable = get_value_of_bills(denomination,num_bills)
    return int(exmoney - exchangable)

