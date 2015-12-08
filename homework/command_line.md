# Command Line Practice Exercises

**Using chipotle.tsv in the data subdirectory:**

1. Look at the head and the tail, and think for a minute about how the data is structured.
    $ head chipotle.tsv
    $ tail chipotle.tsv
   a. What do you think each column means?
      Each column seems to represent an attribute of a single item that belongs to a food order transaction.
   b. What do you think each row means? Tell me!
      Each row seems to represent a single item that belongs to a food order transaction.

2. How many orders do there appear to be?
    $ cut -f2 chipotle.tsv | awk '{ SUM += $1} END { print SUM }'
   There are 4972 orders in chipotle.tsv

3. How many lines are in the file?
    $ wc -l chipotle.tsv
   There are 4623 lines in chipotle.tsv

4. Which burrito is more popular, steak or chicken?

5. Do chicken burritos more often have black beans or pinto beans?

6. Make a list of all of the CSV or TSV files in the DAT7 repo (using a single command). Think about how wildcard characters can help you with this task.

7. Count the number of occurrences of the word 'dictionary' (regardless of case) across all files in the DAT7 repo.

> Optional: Use the the command line to discover something "interesting" about the Chipotle data.  
The advanced commands below may be helpful to you!