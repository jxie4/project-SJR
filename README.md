# Homework 4: Pandas and Primes

The homework focusses on Pandas, but maintains some level of 'basic python' work.

You may accept the assignment [here](https://classroom.github.com/assignment-invitations/829adc8487082580d8510e309105e51b).

It is due October 26 at 1:30am.

## Pandas

In this homework, you'll use the same chicago crime file that you downloaded for the first homework.
(Download it again if need be.)

1. Which primary type of crime resulted in the most arrests?  Use `df.groupby(..).count(..)`.
2. Which primary type most reliably (fractionally) resulted in an arrest? Use `df.groupby(..).mean()`.
3. Which ward saw the most crime of any type?
4. Regress number of weapons violations per ward against number of homicides per ward.  What is the slope?  What is its error?  Use [scipy.stats.linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html).
   * N.B., you may find that not all wards have crimes or homicides, when you count by ward.  If so, you may need to use `fillna(0, inplace = True)` to specify that there weren't.  Make sure you have 50 wards!
5. Use the school data from class, compare public schools with charters (they have a "C" in their ID).
   Drop the schools that are missing data at the end (`df.dropna(inplace = True)`).
   How do the charters do?  Compare the medians (the 50% points) for the PARCC proficiency (%) and college ready (%).
   (You can call median() on a set.)
   Do they serve comparable fractions of low income students to the public schools?
   * I am asking for a subjective interpretation of the numbers; you can write it as a comment.
6. Merge the school data with one other Census parameter of your choice, using the function from class.  
   Plot them, save the figure as q6.pdf, and make any observations.  You can save plots with 
   ```
   ax = df.plot()
   ax.get_figure().savefig('q6.pdf')
   ```
   I've filled in the format for this question; hope it helps.  Treat it as extra credit.

7. Plot and save (`q7.pdf`) the Chicago region unemployment rate from the BLS file provided.

Please fill in solutions as you go.  Each question should go in one of the provided files.
I would suggest doing your exploration in jupyter, first, and then copying the small code over.

## Python

Please also complete the single (!) python-focussed problem:

Circular primes have the property that all rotations of their digits are also prime numbers.  For instance, 19937, 37199, 71993, 93719, 99371, are all circular primes.  Below 100, there are thirteen such primes: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.  How many circular primes are there below one million?

You should start by figuring out 'the' efficient algorithm for calculating a list of primes.
(Hint from lectures: Eratosthenes.)

There are then two methods: either you do floor division, mods and multiplication, 
  or you could swap parts of strings.

This should be _very_ fast.  (Second hint: when making your list of candidate circular primes, with the sieve, what property of circular primes can you exploit to dramatically reduce the size of that list.)

The assignment is due October 26 at 1:30am.

