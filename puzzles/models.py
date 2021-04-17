from django.db import models


class Puzzle(models.Model):
    starting_fen = models.TextField()
    moves = models.JSONField()
    COLORS = [
        ("W", "White"),
        ("B", "Black"),
    ]
    turn = models.CharField(max_length=1, choices=COLORS)
    piece_count = models.IntegerField()
    piece_count_without_pawns = models.IntegerField()
    white_pieces = models.JSONField()
    black_pieces = models.JSONField()
    rating = models.IntegerField()
    rating_deviation = models.IntegerField()
    popularity = models.IntegerField()
    themes = models.TextField()
    lichess_url = models.URLField()
    good_ratings = models.IntegerField(default=0)
    bad_ratings = models.IntegerField(default=0)

    class Meta:
        ordering = ["piece_count", "piece_count_without_pawns"]
        indexes = [
            models.Index(fields=["piece_count"]),
            models.Index(fields=["piece_count_without_pawns"]),
        ]


class PuzzleId(models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.RESTRICT)
