def arabian_mate(board):
  """
  This function checks for the Arabian Mate move in the given chess board.

  Args:
    board: The chess board.

  Returns:
    True if the Arabian Mate move is possible, False otherwise.
  """

  # Check if the king is in the back rank.
  if board.get_piece_on_square("e8") == "K":

    # Check if there is a rook or queen on the seventh rank.
    if board.get_piece_on_square("h8") in ["R", "Q"]:

      # Check if the king is not in check.
      if not board.is_in_check("e8"):

        # Check if there is a pawn on the sixth rank.
        if board.get_piece_on_square("f7") == "P":

          # Check if the pawn can be captured by the rook or queen.
          if board.is_capture_possible("h8", "f7"):

            # Return True, indicating that the Arabian Mate move is possible.
            return True

  return False
