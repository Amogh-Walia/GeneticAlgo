# GeneticAlgo
This program is written based on Evolution theory/survival of the fittest.
This function will find the maximum possible value of any given function between the range of -2^n to 2^n where n is the bitcount.
Main.py is the main file and doesnt require any other library to be imported


The code works by converting randomly generated floats into "Chromosome" objects which have an array (represnting the float as binary number) and then taking this "Gene" array
and performing the Fitness Function onto them. The top performing objects are taken and their "Gene" arrays undergo "Single point CrossOver" and mutation after which the top performing
objects are taken and the process is repeated.

The loop ends when the top performer is the same for 3 consecutive "generations" meaning that the best value has been reached and further iterations are not required.
