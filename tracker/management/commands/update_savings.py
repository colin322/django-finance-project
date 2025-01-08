from django.core.management.base import BaseCommand
from tracker.utils import update_savings_balance

class Command(BaseCommand):
    help = 'Update savings balance for all users at the end of the month'

    def handle(self, *args, **kwargs):
        update_savings_balance()
        self.stdout.write(self.style.SUCCESS('Savings balances have been updated successfully.'))
