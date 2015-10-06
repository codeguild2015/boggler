<div class="content">

<div class="item">
  <h1> Boggle solver</h1>

<h1>Purpose</h1>
<p>
Purpose:  This project introduces Python modules as a way of breaking more 
complex Python programs into smaller, simpler and more reusable parts. game_dict.py
is a Python module that you must complete.  
The boggler project also 
provides more practice with recursive depth-first search. 
</p>

<p>In addition, this project gives a small introduction to object-oriented programming. 
boggle_board.py is a module that you 
don't have to modify, but you do need to read and understand. The boggle_board module
creates a BoggleBoard class.  Your boggler program will create and use a single
BoggleBoard object.  In the following project, you will create classes and objects 
yourself. 
</p>


<h1>Pair Assignment</h1>
  <p>Work together with one classmate.
  Make sure you both have a solid understanding of the core
  recursive algorithms in this program, including the way we
  manage marking tiles that are already in use on the current
  path.  (This is very typical of depth-first search algorithms.)
  </p>
</div>


<div class="item">
<h1>Boggle solver</h1>
  <p>Boggle is a popular word game in which players search for
  words that can be formed by the letters on a set of tiles
  in a 4x4 grid.  <a
  href="http://en.wikipedia.org/wiki/Boggle">Wikipedia has a brief
  description.</a></p>
  <img src="https://upload.wikimedia.org/wikipedia/commons/f/f4/Boggle.jpg" />

  <p>This program reads a boggle board
  and a dictionary of possible solutions, and prints
  all the dictionary words that can be formed for the board, following
  standard Boggle rules.  Words can be formed starting from any
  position, continuing horizontally, vertically, or diagonally,
  without using any tile twice in the same word. The list of found
  words is printed in alphabetical order. 
  </p>

  <h2>Requirements</h2>
  <p>The behavior of your program in a shell (command line) should be exactly like this.
  There is also a graphical display, which is not shown here, and is not graded.
  </p>
<code><pre>$ python3 boggler.py "ammaglxxxxpaxxxh" shortdict.txt 
alpha 2
gamma 2
Total score:  4
Press enter to end
</pre></code>

<code><pre>$ python3 boggler.py "ammaglxxxxpaxxxh" dict.txt
alp 1
alpha 2
gal 1
gamma 2
hap 1
lag 1
lam 1
mag 1
max 1
Total score:  11
Press enter to end
</pre></code>

  <h2>Starting materials</h2>
  <ul>
    <li><a href="/boggle/graphics.py">graphics.py</a> (don't change this)</li>
    <li><a href="/boggle/boggle_board.py">boggle_board.py</a> (don't change this)</li>
    <li><a href="/boggle/test_harness.py">test_harness.py</a> (for testing)</li>    
    <li><a href="/boggle/grid.py">grid.py</a> (for display, don't change this)</li>  
    <li><a href="/boggle/game_dict.py">game_dict.py</a> You must complete this and turn it in</li>  
    <li><a href="/boggle/boggler.py">boggler.py</a> You must complete this and turn it in</li>    
    <li><a href="/boggle/shortdict.txt">shortdict.txt</a> A short list of words, 
        useful for testing</li>
    <li><a href="/boggle/dict.txt">dict.txt</a> A more typical list of 
    approximately 40,000 common English words.  This is usually enough to beat 
    human boggle players. Serious players of Scrabble and crossword puzzles 
    use larger lists that include less common words.</li>
    </ul>
    </p>
    
    <h2>How to get started</h2>
    <p>Start with the game dictionary.  I have included a pretty good test suite so that 
    you can test it separately from the rest of the boggler program. Notice the funny
    code at the end of the file for testing whether the game_dict module is being 
    called as a main program.  This is so that you can test it like this: 
    </p>
<code><pre>
$ python3 game_dict.py shortdict.txt 
***FAILED***  First word in dictionar (alpha)  Expected: | 1 | but got | 0 |
***FAILED***  Last word in dictionary (omega)  Expected: | 1 | but got | 0 |
***FAILED***  Within dictionary (beta)  Expected: | 1 | but got | 0 |
***FAILED***  Within dictionary (delta)  Expected: | 1 | but got | 0 |
***FAILED***  Within dictionary (gamma)  Expected: | 1 | but got | 0 |
***FAILED***  Prefix of first word (al)  Expected: | 2 | but got | 0 |
***FAILED***  Prefix of last word (om)  Expected: | 2 | but got | 0 |
***FAILED***  Prefix of interior word (bet)  Expected: | 2 | but got | 0 |
***FAILED***  Prefix of interior word (gam)  Expected: | 2 | but got | 0 |
***FAILED***  Prefix of interior word (del)  Expected: | 2 | but got | 0 |
   Passed --  Before any word (aardvark)  result:  0
   Passed --  After all words (zephyr)  result:  0
   Passed --  Interior non-word (axe)  result:  0
   Passed --  Interior non-word (carrot)  result:  0
   Passed --  Interior non-word (hagiography)  result:  0
***FAILED***  First word in dictionar (alpha)  Expected: | 1 | but got | 0 |
***FAILED***  Last word in dictionary (omega)  Expected: | 1 | but got | 0 |
   Passed --  Short word omitted (beta)  result:  0
 </pre></code>
 <p>You will know you probably have a working game dictionary when you can pass these
 tests.  (Writing executable test cases before writing the code that passes them is part 
 of a practice called 
 &ldquo;test-driven development,&rdquo; and is common in the so-called &ldquo;agile&rdquo; software
 development methodologies that are popular today.) 
 </p>
 <p>I suggest writing the search function as a linear search first: Check each word 
 in order, using the Python built-in method <kbd>startswith</kbd> to check for a 
 prefix match. When you have a linear search function working, you can move on to 
 the rest of the program and come back later to make the search function faster
 with binary search.</p>
 <p>When you have your game_dict module working, move on to boggler.py.  Use the 
 game board module to represent the board.  (Duplicating any of the functionality of board.py 
 within your boggler.py source file will be considered an error.) The places you will 
 need to work on boggler.py are marked with FIXME comments.  The main one is the 
 recursive <kbd>find_words</kbd> function.  I have included several FIXME comments 
 to guide you.</p>
 <p>boggler.py includes a <kbd>dedup</kbd> function for putting a results list into 
 sorted order, without duplicate words.  Instead of keeping the original results 
 (with duplicates) in a list, you could use the Python set data structure.  If you do,
 you should put the words into the set from the <kbd>find_words</kbd> function, and 
 then <kbd>dedup</kbd> should be replaced with a function that extracts a sorted 
 list from the set.</p>
 <p><strong>Optional:</strong> When your boggler.py program is working satisfactorily is a good time to return to
 game_dict.py and change the linear search to a binary search.  This requires some careful
 thought:  If the binary search does not find an exact match, which dictionary word
 should you check to see if the word you were looking for could be a prefix of a word
 in the dictionary?  The included test suite will help you check whether you got it right. 
 It is better to turn in a working boggler program that uses linear search, than a 
 broken boggler program that uses binary search (especially if the binary search is 
 what is broken). 
 </p>
    
</div>
<div class="item">
  <h1>Grading rubric</h1>
  <table width="85%" border="0" cellpadding="2">
    <tr>
      <th colspan="2" scope="col">Functional correctness</th>
      <th width="8%" scope="col">&nbsp;</th>
      <th width="60%" scope="col">&nbsp;</th>
      <th width="1%" scope="col">&nbsp;</th>
      <th width="3%" scope="col">40</th>
    </tr>
    <tr>
      <td width="5%">&nbsp;</td>
      <td width="23%"><p>Exactly meets input/output spec</p>        </td>
      <td>10</td>
      <td>5 = minor discrepancy, 0 = ignored spec</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Correct results: Word finding</td>
      <td>25</td>
      <td><p>25 = works for all cases (finds all words, and nothing
	else), 18 = works for almost all cases, 12 = works for most
	cases (e.g., not when one word is a prefix of another), 5 = works for some cases</p></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Correct results: Scoring</td>
      <td>5</td>
      <td>5 points if all words of three or more letters are correctly
      scored, and the correct total is shown</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Other requirements</th>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>40</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><p>Header docstring</p>        </td>
      <td>10</td>
      <td>10 = as specified, 7 = minor issue, 5 = as #comment, 0 = missing</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Function header docstrings</td>
      <td>8</td>
      <td>8 = good docstrings in all functions, 6 = minor problems, 4 = incorrect or multiple missing, 0 = docstrings not provided</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Correct use of modules</td>
      <td>12</td>
      <td><p>12 = modules used correctly, no violation of abstraction,
	8 = decomposition has some issues, such as misuse of global
	variables, use of magic numbers instead of symbolic
	constants,  0 = failure to use modules</p></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Program style and readability</td>
      <td>10</td>
      <td><p>10 Good variable names, indentation, etc --- very readable code, 8 = minor issues, such as inconsistent indentation, 5 = major issues that interfere with readability of code, 0 = unreadable mess </p></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <th colspan="2">Total</th>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>80</td>
    </tr>
  </table>
  <p>I can't anticipate all issues that may be encountered in grading,
  so points may be deducted for other issues not listed in the
  rubric.    A program that does not compile and run (e.g., because of a syntax error) starts with 0 points for functional correctness, but I may award some partial credit. </p>
  <p>&nbsp;</p>
  </div>
