from django.core.management import BaseCommand

from safka.models import Location, Genre, Product, LocationProduct, User

INITIAL_DATA = [
    {
        'name': 'Jabon Shop',
        'city': 'Turku',
        'genres': ['Japanese', 'Thai'],
        'products': ['Ramune', 'Nissin Noodle Super Ultra Hot', 'Kikkoman'],
    },
    {
        'name': 'Thai Shop',
        'city': 'Helsinki',
        'genres': ['Thai'],
        'products': ['Cocos Milk', 'Thai Cube', 'Kikkoman'],
    },
]


class Command(BaseCommand):
    def handle(self, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(username='admin', password='admin', email='')
            self.stdout.write('Created superuser (admin/admin)')
        for info in INITIAL_DATA:
            location, created = Location.objects.get_or_create(name=info['name'], city=info['city'])
            for genre_name in info.get('genres', ()):
                genre, _ = Genre.objects.get_or_create(name=genre_name)
                location.genres.add(genre)
            for product_name in info.get('products', ()):
                product, _ = Product.objects.get_or_create(name=product_name)
                LocationProduct.objects.get_or_create(location=location, product=product)
            if created:
                self.stdout.write(f'Created {location} ({location.n_products} products)')
