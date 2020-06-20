import logging
from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from breathtaking.modules.ideas.models import IdeaComment, IdeaLike, IdeaOffer, Tag, Theme


loggger = logging.getLogger(__name__)
fake = Faker()


class Command(BaseCommand):
    help = 'The Zen of Python'

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete all ideas instance.',
        )

    def handle(self, *args, **options):
        if options['delete']:
            loggger.warning('Удаление записей')
            IdeaComment.objects.all().delete()
            IdeaOffer.objects.all().delete()
            Tag.objects.all().delete()
            Theme.objects.all().delete()
            IdeaLike.objects.all().delete()
        loggger.warning('Старт генерации Тем')
        themes = [Theme.objects.get_or_create(name=fake.name()) for _ in range(1, 20)]
        loggger.warning('Старт генерации Тэгов')
        _ = [Tag.objects.get_or_create(name=fake.name()) for _ in range(1, 20)]
        loggger.warning('Старт генерации Предложений идей')
        idea_offers = [IdeaOffer.objects.get_or_create(
            user_id=1,
            theme=fake.text(10),
            description=fake.text(),
            status=0
        ) for _ in range(1, 20)]
        loggger.warning('Старт присваивания тэгов идеям')
        _ = [
            idea.tags.set(
                Tag.objects.values_list('id', flat=True)[1:10:2]
            ) for idea, _ in idea_offers
        ]
        loggger.warning('Старт генерации тем к идеям')
        for idea, _ in idea_offers:
            idea.themes = themes[randint(0, 18)][0]
            idea.save()
        loggger.warning('Старт генерации комментариев к идеям')
        _ = [IdeaComment.objects.get_or_create(
            user_id=1,
            idea_id=idea.id,
            comment=fake.text()
        ) for idea, _ in idea_offers]
        loggger.warning('Успех!')
