# Welcome to Joelang!!!

Hi! here is **"joelang"**, which is a simple ***interpreter language*** written in python. If you want to play with compiler or interpreter, I think this is a good place to start your journey. Once you have understand the project, you can create your own component such as lexer, parser, you own interpreter and maybe your customised symbol set by modifying corresponding files in different project folder. 

The object of the project is to support basic syntax and expressions like **variable assignment** , **arithmetic operation**, **comparison-if-else statement**, **loop operation** and **function call** usage within the language **joelang**. 

And later probably include some **objective oriented programming/functional programming** features.


# Project Structure

The following is the project structure, and I will explain with the typical compiler/interpreter along with the project folder. Usually a compiler/interpreter consist with:

 1. lexer: convert the input to tokens, which associate each element in the input with its predefined types, like NLP tokenizer for those of you come from AI.
 2. parser: parse the token-list into AST, syntax tree based on the several predefined grammar rules.
 3. interpreter(evaluate): evaluate the the AST to get the result of it.

Following the basic component of a compiler/interpreter and the consideration of software architecture, I will form the project folder as follows.

 - component (this is the simple component, you can also find other implementations of each components)
	 - lexer.py: transfer the programme file into token list with respective types.
	 - parser.py: the parser transfer the tokens into astree nodes.
	 - interpreter.py: implement the visitor pattern to do certain node operation in order to, e,g, evaluate the astree.
 - context: used for traceback the function errors
 - lexer
 - parser
 - interpreter
 - errors
 - utils
 - grammar.txt: *grammar rules* to our recursive-descent parser 
 - position: keep track the position of the give input programme
 - nodes: compiler basically is consisted of tree of nodes.
 - values: a collection of different values types, float|int, variable
 
 # tranditional text book topics that covered 
 
 - Nested procedures and functions
 - Procedure and function calls
 - Semantic analysis (type checking, making sure variables are declared before they are used, and basically checking if a  -program makes sense)
 - Control flow elements (like IF statements)
 - Aggregate data types (Records)
 - More built-in types
 - Source-level debugger
 - Miscellanea (All the other goodness not mentioned above :)

 - tokens
 - shell.py (function entry)

