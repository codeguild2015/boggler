"""
Boggle board
Author: Michal Young
Revisions:    Initial version  26 Oct 2012 for CIS 210 at U. Oregon
              Feb 2013, reorganized as a class BoggleBoard
              October 2014, minor clean up of documentation

The BoggleBoard is a square matrix of tiles
where each tile represents a character
(except "qu" is a single tile).  In addition
to the character(s), each tile can be in
available or not.

The BoggleBoard also maintains a graphical depiction,
including color to show which tiles are currently
in use. 

Limitations:
    Board must be square.  Any num of chars can be passed into the function
    but the resulting board must be square or an error will be presented to 
    the user.  

    The graphics code is tangled into maintenance of the
    board ("model" mixed with "view"); we will learn how
    to factor it out in a later project. 
"""
import grid

class BoggleBoard(object):
   """
   The BoggleBoard is a square matrix of tiles
   where each tile represents a character
   (except "qu" is a single tile).  In addition
   to the character(s), each tile can be in
   available or not.
   """

   def __init__(self,  tiles):
       """
       Create a boggle board and its graphical depiction
       from a string of characters.
       Args:
        self:  the board (to be initialized)
        tiles: A string of characters, each
               representing one tile.  Most characters
               represent a tile containing that character,
               but 'q' represents the pair 'qu' on a tile.
        Returns:  Nothing.  The board is encapsulated in this module.
        """
       # To maintain desired functionality from the command line the board must 
       # square.  To ensure this and do math on the board square root is used
       # frequently.  
       assert(len(tiles)**.5 == int(len(tiles)**.5)) # To ensure board is quare.  
       self.content = [ ]
       self.in_use = [ ]
       self.board_height = int(len(tiles)**.5) 
       self.board_width = int(len(tiles)**.5)
       grid.make(self.board_height,self.board_width,500,500)     # Hack alert! 
       for row in range(self.board_height):
           self.content.append([ ])
           self.in_use.append([ ])
           for col in range(self.board_width):
               char = tiles[int(len(tiles)**.5)*row + col]
               if char == "q" :
                   char = "qu"
               self.content[row].append(char)
               self.in_use[row].append( False )
               grid.fill_cell(row,col,grid.white)  # Hack alert! 
               grid.label_cell(row,col,char)       # Hack alert!  

   def get_char(self, row, col):
       """
       Returns the character at (row,col)
       Args:
           self: this board
           row: row of board, 0..n
           col: col of board, 0..n
       Returns:
           the string labeling the tile at board[row,col]
       Requires:
           the position (row, col) should not be in use when get_char is called.
           (Proper order is to get_char(row,col), then mark_taken(row,col), then
            unmark_taken(row,col) )
       """
       assert row >= 0 and row < len(self.content)
       assert col >= 0 and col < len(self.content[0])
       assert not self.in_use[row][col] 
       return self.content[row][col]

   def available(self, row, col):
       """Check whether we can take a tile at row, col.
       Args:
          self: this board
          row: row of board (may be outside board)
          col: col of board (may be outside board)
       Returns:
           boolean True iff (row,col) is a tile position on
           the board and that tile is not currently marked as
           in use.
       """
       if row < 0 or row >= len(self.content):
           return False
       if col < 0 or col >= len(self.content[0]):
           return False
       return not self.in_use[row][col]

   def mark_taken(self, row, col):
       """
       Marks the tile at row,col as currently in use
       Args:
          self: this board
          row: row of board, 0..n
          col: col of board, 0..n
       Returns:
          nothing
       Requires:
          Tile must not already be in use.  mark_taken and unmark_taken must
          strictly alternate.  Proper sequence is
              - check position for availability
              - get character
              - mark taken
                 - further exploration from this position
              - unmark taken
       """
       assert row >= 0 and row < len(self.content)
       assert col >= 0 and col < len(self.content[0])
       assert not self.in_use[row][col] 
       self.in_use[row][col] = True
       grid.fill_cell(row,col,grid.green)
       grid.label_cell(row,col,self.content[row][col])

   def unmark_taken(self, row, col):
       """
       Marks the tile at row,col as no longer in use. 
       Tile at row,col must be in use when this function is called.
       Args:
          self: this board
          row: row of board, 0..n
          col: col of board, 0..n
       Returns:
          nothing
       Requires:
          Tile must be marked in use.  mark_taken and unmark_taken must
          strictly alternate.  Proper sequence is
              - check position for availability
              - get character
              - mark taken
                 - further exploration from this position
              - unmark taken
          
       """
       assert row >= 0 and row < len(self.content)
       assert col >= 0 and col < len(self.content[0])
       assert self.in_use[row][col] 
       self.in_use[row][col] = False
       grid.fill_cell(row,col,grid.white)               # Hack alert! 
       grid.label_cell(row,col,self.content[row][col])  # Hack alert! 


   def dump(self):
       """For debugging: Print representation of board
          Args: 
            self:  this board       
          Returns: nothing
       """
       print(self.content)

   def __str__(self):
       """For debugging: Return string representation of board.
          The __str__ method is called implicitly when the board is 
          printed or when it is coerced into a string. 
          
          Args: 
            self:  this board
       """
       rep = ""
       for row in self.content :
           rep += "".join( row ) + "\n"
       return rep
    

    



    
