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
    $ cat chipotle.tsv | grep 'chicken burrito' * | wc -l
    $ > 24
    $ cat chipotle.tsv | grep 'steak' * | wc -l
    $ > 4
   Chicken burritos are the most popular.


5. Do chicken burritos more often have black beans or pinto beans?
    $ cat chipotle.tsv | grep 'chicken burrito' * | grep 'black beans' | wc -l
    $ > 6
    $ cat chipotle.tsv | grep 'chicken burrito' * | grep 'pinto beans' | wc -l
    $ > 0
   Chicken burritos more often have black beans.

6. Make a list of all of the CSV or TSV files in the DAT7 repo (using a single command). Think about how wildcard characters can help you with this task.
    $ find . -name "*.tsv" & find . -name "*.csv"

7. Count the number of occurrences of the word 'dictionary' (regardless of case) across all files in the DAT7 repo.
    $ grep -r 'dictionary' ~/19_sf_data/ | wc -w
    $ > 207
   There are 207 occurrences.

> Optional: Use the the command line to discover something "interesting" about the Chipotle data.  
The advanced commands below may be helpful to you!