# **Conway's Game of Life**
## A Cellular Automata

![Example Image](https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Game_of_life_Simkin_glider_gun.svg/749px-Game_of_life_Simkin_glider_gun.svg.png)

[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a zero-player game commonly used for the demonstration of cellular automation. 

Interesting Properties of the game:
- Zero Player Game (_Friends not required_)
- Turing Complete (_Nobody knows what the end state is going to be. So you could use it as coin toss. Don't ask me about the probability tho. May the odds be ever in your favor_)

Rules:
- Any alive cell that is touching less than two alive neighbouring dies. 
- Any alive cell that is touching less than two alive neighbours dies.
- Any alive cell touching four or more alive neighbours dies.
- Any alive cell touching two or three alive neighbours does nothing.
- Any dead cell touching exactly three alive neighbours becomes alive.

As a virtue of it's turing completeness, you could come up with some interesting stuff such as [turing machines running in the game of life](https://youtu.be/HeQX2HjkcNo?t=1774). 
