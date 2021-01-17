from .models import Transaction


class UtilTransaction:

    @staticmethod
    def conditional_transaction_filter(user, account_id, category_id):
        transaction_list = []
        if(account_id is not None and category_id is not None):
            transaction_list = Transaction.objects.filter(
                user=user,
                dompet__account_id=account_id,
                category__category_id=category_id
            )
        elif(account_id is not None and category_id is None):
            transaction_list = Transaction.objects.filter(
                user=user,
                dompet__account_id=account_id
            )
        elif(account_id is None and category_id is not None):
            transaction_list = Transaction.objects.filter(
                user=user,
                category__category_id=category_id
            )
        else:
            transaction_list = Transaction.objects.filter(
                user=user
            )
        return transaction_list
