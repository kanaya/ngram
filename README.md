ngram
=====

N-gram maker.

How to use
----------

    cat input.txt | gawk -f ngram.awk | sort | uniq -c | sort -nr > output.txt
