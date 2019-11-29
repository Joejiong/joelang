# -*- coding: utf-8 -*-
from joe_compiler.joe_compiler_repo.utils.strings_with_arrows import *

import string
import os
import math

from joe_compiler.joe_compiler_repo.component.lexer import Lexer
from joe_compiler.joe_compiler_repo.component.interpreter import Interpreter
from joe_compiler.joe_compiler_repo.component.parser import Parser
from joe_compiler.joe_compiler_repo.context import Context

#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS



def run(fn, text):
  # Generate tokens
  lexer = Lexer(fn, text)
  tokens, error = lexer.make_tokens()
  if error: return None, error
  
  # Generate AST
  parser = Parser(tokens)
  ast = parser.parse()
  if ast.error: return None, ast.error

  # Run program
  interpreter = Interpreter()
  context = Context('<program>')
  context.symbol_table = global_symbol_table
  result = interpreter.visit(ast.node, context)

  return result.value, result.error
