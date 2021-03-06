# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    #assign index numbers to placeholders
   a=first_row[0]
   b=first_row[1]
   c=first_row[2]
   d=second_row[0]
   e=second_row[1]
   f=second_row[2]
   g=third_row[0]
   h=third_row[1]
   i=third_row[2]
   return """
%s  |  %s  |  %s
--------------
%s  |  %s  |  %s
--------------
%s  |  %s  |  %s
""" % (a,b,c,d,e,f,g,h,i)

   
   
   
def test_format_board():
    """
    This is the board used in this test:

        X  |  O  |  X
        --------------
        O  |  X  |  O
        --------------
        O  |  O  |  X

    """
    first_row = 'XOX'
    second_row = 'OXO'
    third_row = 'OOX'
    expected_board = """
X  |  O  |  X
--------------
O  |  X  |  O
--------------
O  |  O  |  X
"""
    board = format_tic_tac_toe_board(first_row, second_row, third_row)

    assert board == expected_board
