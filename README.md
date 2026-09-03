# PinExtractor

This project extracts secret codes from poems based on the length of specific words in each line.

Some intermediate Python concepts applied in this project include:

- *`enumerate()`*: Getting the index and value while iterating through lines.
- *String Splitting*: Using `split()` to separate poems into lines and words.
- *Dynamic Indexing*: Using the line index to select a specific word from each line.
- *Nested Iteration*: Processing poems, lines, and words through multiple iterations.
- *Defensive Validation*: Checking whether the required word exists before accessing it.

The program follows these steps:

- **Split the poem into lines** using `\n`.
- **Iterate through each line** with `enumerate()` to get its index.
- **Split each line into words**.
- **Select a word** based on the current line index.
- **Get the length of the selected word** and add it to the secret code.
- If the required word does not exist, **add `0`** instead.
- **Return the generated secret codes** for all poems.
