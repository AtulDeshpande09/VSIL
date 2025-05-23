# VSIL – Very Simple Interpreted Language

VSIL is a tiny interpreted language built as an educational project to explore the fundamentals of compilers, interpreters, and language design.

We created it over a couple of days — not to build something production-ready, but to understand **how languages work under the hood**.

---

## 🌟 Features

- `print` statement to output strings and expressions
- Basic arithmetic: `+`, `-` on integers
- String literals in double quotes
- Simple tokenization, parsing, and interpretation using clean Python modules

---

## 🧠 Why We Built It

This project was born out of curiosity — a way to **go deeper** into how high-level code gets understood and executed by a system. It was also a chance to appreciate the elegance and challenge of language design, even in its most minimal form.

> "*Creating your own language, even a simple one, changes the way you understand all others.*"

---

## 🧱 How It Works

### 🔹 1. Lexer (`lexer.py`)
Breaks source code into tokens using regex. It recognizes:
- Keywords: `print`
- Strings: `"hello"`
- Integers: `42`
- Operators: `+`, `-`

### 🔹 2. Parser (`parser.py`)
Converts tokens into an **AST (Abstract Syntax Tree)**:
- Expressions like `2 + 3`
- Statements like `print "hello"`

### 🔹 3. Interpreter (`interpreter.py`)
Walks the AST and evaluates expressions, printing results.

---

## 💡 Example Program (`test.vsil`)

```vsil
print "The result is:"
print 2 + 3
print "Bye!"
```
```bash
python main.py test.vsil
```

## 📦 Project Structure

vsil/
├── lexer.py         # Tokenizes input
├── parser.py        # Builds the AST
├── interpreter.py   # Evaluates AST
├── main.py          # Entry point
└── test.vsil        # Sample program
