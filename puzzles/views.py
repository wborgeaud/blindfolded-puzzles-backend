import random
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Puzzle


def random_puzzle(request):
    max_pieces = int(request.GET.get('max_pieces', 32))
    qs = Puzzle.objects.filter(piece_count__lte=max_pieces)
    count = qs.count()
    p = qs[random.randint(0, count - 1)]
    return JsonResponse(model_to_dict(p))


def rate(request):
    puzzle_id = request.GET.get('puzzle_id', None)
    if puzzle_id is None:
        return JsonResponse({"error": "Please provide a puzzle id."})
    rating = request.GET.get('rating', None)
    if rating is None:
        return JsonResponse({"error": "Please provide a rating."})

    puzzle = Puzzle.objects.get(pk=puzzle_id)
    if rating == "good":
        puzzle.good_ratings += +1
    elif rating == "bad":
        puzzle.bad_ratings += +1
    else:
        return JsonResponse(
            {"error": "Please provide a rating that is good or bad."})
    puzzle.save()
    return JsonResponse({"all": "good"})


def trial(request):
    x = request.session.get('counter', 0)
    request.session['counter'] = x + 1
    return JsonResponse({"counter": x + 1})
