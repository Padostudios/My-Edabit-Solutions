"""
A game of table tennis almost always sounds like Ping! followed by Pong! Therefore, you know that Player 2 has won if you hear Pong! as the last sound (since Player 1 didn't return the ball back).

Given a list of Ping!, create a function that inserts Pong! in between each element. Also:

If win equals True, end the list with Pong!.
If win equals False, end with Ping! instead.

Notes
You will always return the ball (i.e. the Pongs are yours).
Player 1 serves the ball and makes Ping!.
Return a list of strings.

"""

def ping_pong(lst, win):
	a = ["Ping!","Pong!"]*len(lst)
	return a if win else a[:-1]