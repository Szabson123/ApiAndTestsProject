from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        attempt_count = 0

        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError) as error:
                self.stdout.write(f'Database is not ready yet,'
                                  f' waiting 1 second... Error: {error}')
                time.sleep(1)
                attempt_count += 1

        self.stdout.write(self.style.SUCCESS(f'Database ready after'
                                             f' {attempt_count} attempts!'))
