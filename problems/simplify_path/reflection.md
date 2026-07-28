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
1. How do you solve this with a stack? -> the idea is not to introduce unnecessary complexity by pushing every character into the stack and focus only on storing the individual file names, because you have the rules to reconstruct the simplified path from just the file names.
2. Can I solve this problem without using .split? -> Yes, simply traverse the string and ignore characters like extra slashes. Note that since flush pushes to the queue depend on seeing a '/', an extra slash must be added to the string being traversed to ensure the last file name gets pushed.
3. Can we do better than O(n) time and space? Why? -> No, because you must at the very least visit each character once. I'm not quite sure why we can't do better than O(n) space at the moment. 

And of course, when I finished those I returned to my original question: what properties of this question make a stack a good choice? I think the answer is that a stack is a data structure that gives you the ability to backtrack due to its LIFO property. Whenever elements you have already visited are unable to be completely destroyed, or you need some notion of history, a stack (or queue depending on the constraint) might be a good choice. Let me know if my thought needs any correction! 

When I went back and fixed my code, I ran into a bug that occurred because originally, I wrote a conditional branch that checked for "flush == '..' and len(new_path) > 0", which meant that for an input like "/../", I would roll over to the elif and else blocks where I push the flush into the stack, even though I shouldn't in this case. I figured this out through a series of print statements and then fixed it by separating the conditions, at the expense of a little bit messier code. If I were to redo this, I would look at how I can simplify the control flow somehow. 
