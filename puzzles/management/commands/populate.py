from django.core.management.base import BaseCommand, CommandError
import chess
import csv
from tqdm import tqdm
from puzzles.models import Puzzle

PIECES = [
    chess.KING, chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT, chess.PAWN
]


def get_puzzles(fp):
    with open(fp, newline='') as f:
        r = csv.reader(f)
        puzzles = list(r)
    return puzzles


def get_pieces(board):
    white_pieces = {}
    black_pieces = {}
    for piece in PIECES:
        ps = board.pieces(piece, chess.WHITE)
        squares = [chess.square_name(s) for s in ps]
        white_pieces[piece] = squares
        ps = board.pieces(piece, chess.BLACK)
        squares = [chess.square_name(s) for s in ps]
        black_pieces[piece] = squares

    return white_pieces, black_pieces


def get_piece_count(white_pieces, black_pieces):
    return sum(len(s) for s in white_pieces.values()) + sum(
        len(s) for s in black_pieces.values())


def get_piece_count_without_pawns(white_pieces, black_pieces):
    return sum(len(s)
               for p, s in white_pieces.items() if p != chess.PAWN) + sum(
                   len(s) for p, s in black_pieces.items() if p != chess.PAWN)


def get_san_moves(board, uci_moves):
    san_moves = []
    for m in uci_moves:
        mm = board.parse_uci(m)
        san_moves.append(board.san(mm))
        board.push(mm)
    return san_moves


def to_piece_symbol(pieces):
    nd = {}
    for p, s in pieces.items():
        nd[chess.piece_symbol(p)] = s
    return nd


class Command(BaseCommand):
    help = 'Populate the DB with puzzles'

    def add_arguments(self, parser):
        parser.add_argument('fp', type=str)

    def handle(self, *args, **options):
        puzzles = get_puzzles(options['fp'])
        puzzle_objects = []
        MAX_SIZE = 10**5
        for puzzle in tqdm(puzzles):
            board = chess.Board(puzzle[1])
            uci_moves = puzzle[2].split()
            board.push_uci(uci_moves.pop(0))
            starting_fen = board.fen()
            turn = "W" if board.turn == chess.WHITE else "B"
            white_pieces, black_pieces = get_pieces(board)
            moves = get_san_moves(board, uci_moves)
            piece_count = get_piece_count(white_pieces, black_pieces)
            piece_count_without_pawns = get_piece_count_without_pawns(
                white_pieces, black_pieces)
            rating = int(puzzle[3])
            rating_deviation = int(puzzle[4])
            popularity = int(puzzle[5])
            themes = puzzle[7]
            lichess_url = puzzle[8]

            puzzle_objects.append(
                Puzzle(starting_fen=starting_fen,
                       moves=moves,
                       turn=turn,
                       piece_count=piece_count,
                       piece_count_without_pawns=piece_count_without_pawns,
                       white_pieces=to_piece_symbol(white_pieces),
                       black_pieces=to_piece_symbol(black_pieces),
                       rating=rating,
                       rating_deviation=rating_deviation,
                       popularity=popularity,
                       themes=themes,
                       lichess_url=lichess_url))
            if len(puzzle_objects) >= MAX_SIZE:
                Puzzle.objects.bulk_create(puzzle_objects)
                puzzle_objects = []
