from common.constants import StatusCode, OrderConstants

from order.models import Order

class OrderListService:
    def get_all(self):
        return Order.objects.exclude(order_status__in=[StatusCode.ORDER_FAILED, StatusCode.PAYMENT_PENDING, StatusCode.PAYMENT_FAILED])
    
    def get_new_list(self, orders):
        return orders.filter(order_status=StatusCode.ORDER_PENDING)