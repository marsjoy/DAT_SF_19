# Command Line Practice Exercises

**Using chipotle.tsv in the data subdirectory:**

**1. Look at the head and the tail, and think for a minute about how the data is structured.**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ head chipotle.tsv`   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ tail chipotle.tsv`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*a. What do you think each column means?*   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Each column seems to represent an attribute of a single item that belongs to a food order transaction.  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*b. What do you think each row means? Tell me!*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Each row seems to represent a single item that belongs to a food order transaction.

**2. How many orders do there appear to be?**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ cut -f2 chipotle.tsv | awk '{ SUM += $1} END { print SUM }'`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are 4972 orders in chipotle.tsv

**3. How many lines are in the file?**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ wc -l chipotle.tsv`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are 4623 lines in chipotle.tsv

**4. Which burrito is more popular, steak or chicken?**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ cat chipotle.tsv | grep 'chicken burrito' * | wc -l`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ > 24`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ cat chipotle.tsv | grep 'steak' * | wc -l`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ > 4`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chicken burritos are the most popular.


**5. Do chicken burritos more often have black beans or pinto beans?**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ cat chipotle.tsv | grep 'chicken burrito' * | grep 'black beans' | wc -l`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ > 6`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ cat chipotle.tsv | grep 'chicken burrito' * | grep 'pinto beans' | wc -l`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ > 0`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chicken burritos more often have black beans.

**6. Make a list of all of the CSV or TSV files in the DAT7 repo (using a single command). Think about how wildcard characters can help you with this task.**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ find . -name "*.tsv" & find . -name "*.csv"`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[1] 3770 `   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./chipotle.tsv`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./airlines.csv`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./drinks.csv`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./hitters.csv`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./housing-data.csv`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./imdb_1000.csv`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./titanic.csv `   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./ufo.csv`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./vehicles_test.csv`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./vehicles_train.csv`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`./yelp.csv`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`[1]+  Done                    find . -name "*.tsv"`

**7. Count the number of occurrences of the word 'dictionary' (regardless of case) across all files in the DAT7 repo.**  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ grep -r 'dictionary' ~/19_sf_data/ | wc -w`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ > 207`    
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are 207 occurrences.  

> Optional: Use the the command line to discover something "interesting" about the Chipotle data.  
The advanced commands below may be helpful to you!