'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from decimal import Decimal

MAX_ORDER_AMOUNT = 1000000

def validorder(order: Order):
    total_product = Decimal('0')
    total_payment = Decimal('0')

    for item in order.items:
        if item.type == 'payment':

            if item.amount < 0:
                return "Invalid payment amount"

            total_payment += Decimal(str(item.amount))

        elif item.type == 'product':

            if item.amount < 0 or item.quantity < 0:
                return "Invalid product amount"

            total_product += Decimal(str(item.amount)) * Decimal(str(item.quantity))

        else:
            return "Invalid item type: %s" % item.type

    if total_product > MAX_ORDER_AMOUNT or total_payment > MAX_ORDER_AMOUNT:
        return "Total amount payable for an order exceeded"

    if total_payment == total_product:
        return "Order ID: %s - Full payment received!" % order.id
    else:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (
            order.id, total_payment - total_product)
