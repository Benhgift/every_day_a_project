#ZODB test

I looked into ZODB and found that the python and database community generally looks down on ZODB due to lacking good migration support and good data integrity support (not sure what this means in this context). Here's my main reference: https://www.reddit.com/r/Python/comments/2e5gfh/zodb_should_i_use_it/

But it seems to me that ZODB would be nice for a small, well encapsulated project that won't grow too big. It's easier to get started with it than a normal SQL db, and it's far better than just pickle-ing objects. 
