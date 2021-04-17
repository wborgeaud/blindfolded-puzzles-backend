from django.core.management.base import BaseCommand
from tqdm import tqdm
from puzzles.models import Puzzle, PuzzleId


class Command(BaseCommand):
    help = 'Populate the puzzles ids'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        ids = Puzzle.objects.values_list('id')
        puzzle_ids = [PuzzleId(puzzle_id=i[0]) for i in tqdm(ids)]
        PuzzleId.objects.bulk_create(puzzle_ids)
