## Simplify Path Reflection
### Date completed: 07.28.2026

### Rough Work Thought Process:
I started by trying to understand the problem. In my notebook, I wrote '/' signals the start of the file. Alone and at the start, it means the root. 
Some path must be converted to a simplified canonical path. This is a constraint.

Then I tried to outline the constraints, namely that when I encounter multiple '/'s I should compress them somehow. There were more I should have written
but I got distracted by a question - what properties of this question make a stack a good choice? 

I wrote down that I needed a way to know if I have seen '/, and how many I have seen so far. Later on I would find out I actually don't need this information.

So afterwards, I tried mapping out the phases. At any point, I could be in a '/' phase, a '/./' detection phase, or a '/../' detection phase. 

At the 30 minute time stamp, I stopped working and looked at the solution. I asked the following questions while reading:
1. How do you solve this with a stack?
2. Can I solve this problem without using .split?
3. Can we do better than O(n) time and space? Why?

And of course, when I finished those I returned to my original question: what properties of this question make a stack a good choice?

When I went back and fixed my code, I ran into a bug that occurred because originally, I wrote a conditional branch that checked for "
