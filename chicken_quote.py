#! /usr/bin/python

import sys

g_quote = "------------------------------------------------"
g_chicken = (
	"                   \\\n"
	"                    \\  /\\__/\\\n"
	"                     \\ \\    /\n"
	"                       |   0 >>\n"
	"                       |    |\n"
	"                       |____|\n"
	"              ____((__<|    |\n"
	"              (             |\n"
	"              (             |\n"
	"              (_____________/\n"
	"                    |  |\n"
	"                    |  |\n"
	"                   /\ /\\\n"
)

if len(sys.argv) < 2:
	print("Please pass a quote")
	sys.exit(0)

print(g_quote)
print("    >> " + sys.argv[1])
print(g_quote)
print(g_chicken)
