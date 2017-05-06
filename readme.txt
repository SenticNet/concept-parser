Kindly copy ‘stanford-corenlp-3.4.1-models.jar’ from https://stanfordnlp.github.io/CoreNLP/
And place under /stanford-corenlp-python-final\stanford-corenlp-full-2014-08-27

2 files to run:
1) concept_parser_line2.py -> This is for single line input 
2) concept_parser.py -> This is for file input
Instructions:
1. For the single line input file: 
Method 1:
Enter in this form in the terminal.
>> python
>> import concept_parser_line2
>> concept_parser_line2.main()
This method makes the Java modules load once and then the concept_parser_line2.main() can be used to enter the sentences continuously without loading the models again.
Method 2:
python concept_parser_line2.py
This will make the modules load once and only a single sentence can be entered.
The entire folder should be kept in order to run these files as the CoreNLP packages are within them.
It can be uploaded.

