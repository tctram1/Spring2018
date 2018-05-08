class Order:
    #class attribute
    orders = []

    #instance attribute
    orderid = 0
    shipping_address = ''
    expedited = False
    shipped = False
    customer = None

    @staticmethod
    def test_expedited(order):
        return order.expedited

    @staticmethod
    def get_filtered_orders_customer_names(predicate):
        output = []
        for order in Order.orders:
            if predicate(order):
                output.append(order.customer.name)
        return output

    @staticmethod
    def get_customer_name(order):
        return order.customer.name

    @staticmethod
    def get_expedited_orders_customer_names():
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_customer_name
        )

    @staticmethod
    def get_filtered_info(predicate, func):
        output = []
        for order in Order.orders:
            if predicate(order):
                output.append(func(order))
        return output

    @staticmethod
    def get_expedited_orders_customer_names():
        return Order.get_filtered_orders_customer_names(Order.test_expedited)
    
    @staticmethod
    def _get_expedited_orders_customer_names():
        output = []
        for order in Order.orders:
            if order.expedited:
                output.append(order.customer.name)
        return output

    @staticmethod
    def get_expedited_orders_customer_addresses():
        output = []
        for order in Order.orders:
            if order.expedited:
                output.append(order.customer.address)
        return output
    
    @staticmethod
    def get_expedited_orders_shipping_addresses():
        output = []
        for order in Order.orders:
            if order.expedited:
                output.append(order.shipping_address)
        return output