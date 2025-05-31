import tkinter as tk
from tkinter import scrolledtext, font
import random
import webbrowser

class ProgrammingTutor:
    def __init__(self, root):
        self.root = root
        self.root.title("Programming Concepts Tutor")
        self.root.geometry("900x700")
        self.root.configure(bg='#f5f5f5')
        
        self.concepts = {
            "Fundamentals": [
                {
                    "name": "Variables",
                    "definition": "Named storage locations that hold data which can be referenced and manipulated.",
                    "key_points": [
                        "Hold values that can change during program execution",
                        "Have a name, type, and value",
                        "Improve code readability and maintainability"
                    ],
                    "syntax": {
                        "Python": "variable_name = value",
                        "Java": "type variableName = value;",
                        "C++": "type variable_name = value;"
                    },
                    "example": "# Python\nage = 25\nname = \"Imasha\"\nprice = 19.99",
                    "common_uses": "Storing user input, calculation results, configuration values",
                    "questions": [
                        {
                            "text": "What are the key characteristics of variables?",
                            "answers": ["Name, type, value", "Mutable storage", "Memory allocation"]
                        }
                    ],
                    "references": [
                        {"text": "Python Variables (W3Schools)", "url": "https://www.w3schools.com/python/python_variables.asp"},
                        {"text": "Java Variables (Oracle)", "url": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html"},
                        {"text": "C++ Variables (GeeksforGeeks)", "url": "https://www.geeksforgeeks.org/variables-in-c/"}
                    ],
                    
                },
                {
                    "name": "Data Types",
                    "definition": "Classifications that specify which type of value a variable can hold.",
                    "key_points": [
                        "Primitive types: integers, floats, booleans, characters",
                        "Composite types: arrays, objects",
                        "Language-specific variations exist"
                    ],
                    "syntax": {
                        "Python": "# Dynamic typing\nx = 5  # integer\ny = \"Hello\"  # string",
                        "Java": "int x = 5;\nString y = \"Hello\";",
                        "C": "int x = 5;\nchar y[] = \"Hello\";"
                    },
                    "example": "# Type checking in Python\ntype(42)        # <class 'int'>\ntype(3.14)     # <class 'float'>\ntype(True)     # <class 'bool'>",
                    "common_uses": "Ensuring proper operations, memory allocation, type safety",
                    "questions": [
                        {
                            "text": "What's the difference between static and dynamic typing?",
                            "answers": ["Static: types checked at compile-time", "Dynamic: types checked at runtime"]
                        }
                    ],
                    "references": [
                        {"text": "Python Data Types (Real Python)", "url": "https://realpython.com/python-data-types/"},
                        {"text": "Java Data Types (Oracle)", "url": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html"},
                        {"text": "Data Types Explained (freeCodeCamp)", "url": "https://www.freecodecamp.org/news/data-types-in-programming/"}
                    ]
                }
            ],
            "Control Structures": [
                {
                    "name": "Conditionals",
                    "definition": "Statements that execute different code blocks based on boolean conditions.",
                    "key_points": [
                        "if, else if (elif), else structure",
                        "Ternary operators for concise conditions",
                        "Switch statements in some languages"
                    ],
                    "syntax": {
                        "Python": "if x > 0:\n    print(\"Positive\")\nelif x < 0:\n    print(\"Negative\")\nelse:\n    print(\"Zero\")",
                        "JavaScript": "if (x > 0) {\n    console.log(\"Positive\");\n} else if (x < 0) {\n    console.log(\"Negative\");\n} else {\n    console.log(\"Zero\");\n}"
                    },
                    "example": "# Grading system\ngrade = 85\nif grade >= 90:\n    print(\"A\")\nelif grade >= 80:\n    print(\"B\")\nelse:\n    print(\"C or below\")",
                    "common_uses": "Decision making, input validation, branching logic",
                    "questions": [
                        {
                            "text": "What's the difference between 'if' and 'switch' statements?",
                            "answers": ["if: handles complex conditions", "switch: matches single value against cases"]
                        }
                    ],
                    "references": [
                        {"text": "Python Conditionals (Real Python)", "url": "https://realpython.com/python-conditional-statements/"},
                        {"text": "JavaScript Conditionals (MDN)", "url": "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals"},
                        {"text": "Conditionals Explained (freeCodeCamp)", "url": "https://www.freecodecamp.org/news/conditional-statements-explained/"}
                    ]
                },
                {
                    "name": "Loops",
                    "definition": "Constructs that repeat a block of code until a condition is met.",
                    "key_points": [
                        "for loops: iterate a specific number of times",
                        "while loops: repeat while condition is true",
                        "break and continue for flow control"
                    ],
                    "syntax": {
                        "Python": "# for loop\nfor i in range(5):\n    print(i)\n\n# while loop\nwhile x < 10:\n    print(x)\n    x += 1",
                        "Java": "// for loop\nfor (int i = 0; i < 5; i++) {\n    System.out.println(i);\n}\n\n// while loop\nwhile (x < 10) {\n    System.out.println(x);\n    x++;\n}"
                    },
                    "example": "# Sum numbers from 1 to 10\ntotal = 0\nfor num in range(1, 11):\n    total += num\nprint(f\"Sum: {total}\")",
                    "common_uses": "Processing collections, repeated operations, polling",
                    "questions": [
                        {
                            "text": "When would you use a 'for' loop vs a 'while' loop?",
                            "answers": ["for: known iterations", "while: unknown number of iterations"]
                        }
                    ],
                    "references": [
                        {"text": "Python Loops (W3Schools)", "url": "https://www.w3schools.com/python/python_for_loops.asp"},
                        {"text": "Java Loops (Oracle)", "url": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/while.html"},
                        {"text": "Loops Guide (GeeksforGeeks)", "url": "https://www.geeksforgeeks.org/loops-in-programming/"}
                    ]
                }
            ],
            "Data Structures": [
                {
                    "name": "Arrays",
                    "definition": "Contiguous memory structures storing elements of the same type.",
                    "key_points": [
                        "Fixed size in many languages",
                        "O(1) access time for elements",
                        "Indexed starting from 0"
                    ],
                    "syntax": {
                        "Python": "# Lists are similar but more flexible\narr = [1, 2, 3]",
                        "Java": "int[] arr = {1, 2, 3};",
                        "C": "int arr[3] = {1, 2, 3};"
                    },
                    "example": "# Find maximum value\nnumbers = [34, 12, 89, 5]\nmax_num = numbers[0]\nfor num in numbers:\n    if num > max_num:\n        max_num = num\nprint(f\"Max: {max_num}\")",
                    "common_uses": "Storing collections, matrices, buffers",
                    "questions": [
                        {
                            "text": "What's the time complexity of accessing an array element?",
                            "answers": ["O(1)", "Constant time"]
                        }
                    ],
                    "references": [
                        {"text": "Python Lists (Real Python)", "url": "https://realpython.com/python-lists-tuples/"},
                        {"text": "Java Arrays (Oracle)", "url": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html"},
                        {"text": "Array Data Structure (GeeksforGeeks)", "url": "https://www.geeksforgeeks.org/array-data-structure/"}
                    ]
                },
                {
                    "name": "Linked Lists",
                    "definition": "Linear data structure where elements are linked via pointers.",
                    "key_points": [
                        "Dynamic size",
                        "Nodes contain data and pointer to next node",
                        "O(n) access time but efficient inserts/deletes"
                    ],
                    "syntax": {
                        "Python": "class Node:\n    def __init__(self, data):\n        self.data = data\n        self.next = None",
                        "Java": "class Node {\n    int data;\n    Node next;\n    \n    Node(int d) {\n        data = d;\n        next = null;\n    }\n}"
                    },
                    "example": "# Simple linked list in Python\nclass LinkedList:\n    def __init__(self):\n        self.head = None\n    \n    def append(self, data):\n        new_node = Node(data)\n        if not self.head:\n            self.head = new_node\n            return\n        last = self.head\n        while last.next:\n            last = last.next\n        last.next = new_node",
                    "common_uses": "Implementing stacks/queues, memory-efficient lists",
                    "questions": [
                        {
                            "text": "What's the advantage of linked lists over arrays?",
                            "answers": ["Dynamic size", "Efficient inserts/deletes", "No need for contiguous memory"]
                        }
                    ],
                    "references": [
                        {"text": "Linked Lists Explained (freeCodeCamp)", "url": "https://www.freecodecamp.org/news/implementing-a-linked-list-in-javascript/"},
                        {"text": "Python Linked List (GeeksforGeeks)", "url": "https://www.geeksforgeeks.org/linked-list-set-1-introduction/"},
                        {"text": "Linked List Data Structure (Programiz)", "url": "https://www.programiz.com/dsa/linked-list"}
                    ]
                }
            ],
            "Object-Oriented Programming": [
                {
                    "name": "Classes",
                    "definition": "Blueprints for creating objects that bundle data and functionality.",
                    "key_points": [
                        "Encapsulation: bundling data and methods",
                        "Inheritance: creating hierarchical relationships",
                        "Polymorphism: same interface for different types"
                    ],
                    "syntax": {
                        "Python": "class MyClass:\n    def __init__(self, param):\n        self.param = param\n    \n    def method(self):\n        return self.param",
                        "Java": "class MyClass {\n    private int param;\n    \n    public MyClass(int p) {\n        param = p;\n    }\n    \n    public int method() {\n        return param;\n    }\n}"
                    },
                    "example": "# Bank account class\nclass BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self.balance = balance\n    \n    def deposit(self, amount):\n        self.balance += amount\n    \n    def withdraw(self, amount):\n        if amount <= self.balance:\n            self.balance -= amount\n        else:\n            print(\"Insufficient funds\")",
                    "common_uses": "Modeling real-world entities, organizing complex code",
                    "questions": [
                        {
                            "text": "What are the four pillars of OOP?",
                            "answers": ["Encapsulation", "Abstraction", "Inheritance", "Polymorphism"]
                        }
                    ],
                    "references": [
                        {"text": "Python OOP (Real Python)", "url": "https://realpython.com/python3-object-oriented-programming/"},
                        {"text": "Java OOP (Oracle)", "url": "https://docs.oracle.com/javase/tutorial/java/concepts/"},
                        {"text": "OOP Principles (freeCodeCamp)", "url": "https://www.freecodecamp.org/news/object-oriented-programming-concepts/"}
                    ]
                },
                {
                    "name": "Inheritance",
                    "definition": "Mechanism where a class derives attributes and methods from a parent class.",
                    "key_points": [
                        "Promotes code reuse",
                        "Supports polymorphism",
                        "Can be single or multiple (language-dependent)"
                    ],
                    "syntax": {
                        "Python": "class ChildClass(ParentClass):\n    def __init__(self):\n        super().__init__()",
                        "Java": "class ChildClass extends ParentClass {\n    public ChildClass() {\n        super();\n    }\n}"
                    },
                    "example": "# Animal inheritance hierarchy\nclass Animal:\n    def __init__(self, name):\n        self.name = name\n    \n    def speak(self):\n        pass\n\nclass Dog(Animal):\n    def speak(self):\n        return \"Woof!\"\n\nclass Cat(Animal):\n    def speak(self):\n        return \"Meow!\"",
                    "common_uses": "Creating specialized versions of classes, implementing interfaces",
                    "questions": [
                        {
                            "text": "What's the difference between inheritance and composition?",
                            "answers": ["Inheritance: 'is-a' relationship", "Composition: 'has-a' relationship"]
                        }
                    ],
                    "references": [
                        {"text": "Python Inheritance (W3Schools)", "url": "https://www.w3schools.com/python/python_inheritance.asp"},
                        {"text": "Java Inheritance (Oracle)", "url": "https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html"},
                        {"text": "Inheritance vs Composition (Real Python)", "url": "https://realpython.com/inheritance-composition-python/"}
                    ]
                }
            ],
            "Algorithms": [
                {
                    "name": "Sorting",
                    "definition": "Process of arranging data in a particular order (ascending/descending).",
                    "key_points": [
                        "Comparison-based: Bubble, Quick, Merge sorts",
                        "Non-comparison: Counting, Radix sorts",
                        "Time complexity varies from O(n²) to O(n log n)"
                    ],
                    "syntax": {
                        "Python": "# Built-in sort\nsorted_list = sorted(unsorted)\n\n# List method\nunsorted.sort()",
                        "Java": "Arrays.sort(array);\nCollections.sort(list);"
                    },
                    "example": "# Quick sort implementation\ndef quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + middle + quicksort(right)",
                    "common_uses": "Data organization, search optimization, statistics",
                    "questions": [
                        {
                            "text": "What's the time complexity of merge sort?",
                            "answers": ["O(n log n)", "Linearithmic time"]
                        }
                    ],
                    "references": [
                        {"text": "Sorting Algorithms (GeeksforGeeks)", "url": "https://www.geeksforgeeks.org/sorting-algorithms/"},
                        {"text": "Python Sorting (Real Python)", "url": "https://realpython.com/sorting-algorithms-python/"},
                        {"text": "Sorting Visualized (VisuAlgo)", "url": "https://visualgo.net/en/sorting"}
                    ]
                },
                {
                    "name": "Searching",
                    "definition": "Process of finding a particular item in a collection of data.",
                    "key_points": [
                        "Linear search: O(n), checks each element",
                        "Binary search: O(log n), requires sorted data",
                        "Hash tables: O(1) average case"
                    ],
                    "syntax": {
                        "Python": "# Linear search\ndef linear_search(arr, target):\n    for i, item in enumerate(arr):\n        if item == target:\n            return i\n    return -1",
                        "Java": "// Binary search\nint index = Arrays.binarySearch(array, key);"
                    },
                    "example": "# Binary search implementation\ndef binary_search(arr, target):\n    low = 0\n    high = len(arr) - 1\n    \n    while low <= high:\n        mid = (low + high) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            low = mid + 1\n        else:\n            high = mid - 1\n    return -1",
                    "common_uses": "Databases, information retrieval, algorithms",
                    "questions": [
                        {
                            "text": "When would you use binary search over linear search?",
                            "answers": ["When data is sorted", "For large datasets", "When O(log n) is needed"]
                        }
                    ],
                    "references": [
                        {"text": "Search Algorithms (freeCodeCamp)", "url": "https://www.freecodecamp.org/news/search-algorithms-linear-and-binary-explained/"},
                        {"text": "Binary Search (Khan Academy)", "url": "https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search"},
                        {"text": "Searching Algorithms (GeeksforGeeks)", "url": "https://www.geeksforgeeks.org/searching-algorithms/"}
                    ]
                }
            ]
        }
        
        self.current_concept = None
        self.current_question = None
        self.user_progress = {}
        
        self.setup_ui()
        self.show_welcome_message()
    
    def setup_ui(self):
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=10)
        
        main_frame = tk.Frame(self.root, bg='#f5f5f5')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(
            main_frame, wrap=tk.WORD, width=80, height=25,
            font=('Segoe UI', 10), bg='white', padx=10, pady=10,
            insertbackground='black'
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        self.chat_display.config(state='disabled')
        
        self.chat_display.tag_config('bot', foreground='#0066cc', font=('Segoe UI', 10))
        self.chat_display.tag_config('user_label', foreground='#333333', font=('Segoe UI', 10, 'bold'))
        self.chat_display.tag_config('user_input', foreground='#d35400', font=('Segoe UI', 10, 'italic'))
        self.chat_display.tag_config('code', background='#f0f0f0', font=('Consolas', 9))
        self.chat_display.tag_config('highlight', background='#fffde7')
        self.chat_display.tag_config('link', foreground='#0645ad', underline=True)
        
        input_frame = tk.Frame(main_frame, bg='#f5f5f5')
        input_frame.pack(fill=tk.X, pady=(5, 0))
        
        self.user_input = tk.Entry(
            input_frame, font=('Segoe UI', 11), width=60,
            relief=tk.SOLID, borderwidth=1
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.user_input.bind('<Return>', lambda e: self.process_input())
        
        send_btn = tk.Button(
            input_frame, text="Send", command=self.process_input,
            font=('Segoe UI', 10), bg='#4CAF50', fg='white',
            relief=tk.FLAT, activebackground='#388E3C'
        )
        send_btn.pack(side=tk.LEFT)
        
        menu_frame = tk.Frame(main_frame, bg='#f5f5f5')
        menu_frame.pack(fill=tk.X, pady=(5, 0))
        
        tk.Button(
            menu_frame, text="Browse Concepts", command=self.show_concept_menu,
            font=('Segoe UI', 9), bg='#2196F3', fg='white',
            relief=tk.FLAT, activebackground='#1976D2'
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Button(
            menu_frame, text="Practice", command=self.start_practice,
            font=('Segoe UI', 9), bg='#FF9800', fg='white',
            relief=tk.FLAT, activebackground='#F57C00'
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Button(
            menu_frame, text="Clear Chat", command=self.clear_chat,
            font=('Segoe UI', 9), bg='#f44336', fg='white',
            relief=tk.FLAT, activebackground='#d32f2f'
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        # Add Exit button
        tk.Button(
            menu_frame, text="Exit", command=self.root.destroy,
            font=('Segoe UI', 9), bg='#607d8b', fg='white',
            relief=tk.FLAT, activebackground='#455a64'
        ).pack(side=tk.LEFT)
    
    def clear_chat(self):
        self.chat_display.config(state='normal')
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state='disabled')
        self.show_welcome_message()
    
    def show_welcome_message(self):
        welcome_msg = (
            "Welcome to Programming Concepts Tutor!\n\n"
            "I can explain programming concepts, provide code examples, "
            "and test your understanding.\n\n"
            "Try asking about:\n"
            "- Variables and data types\n"
            "- Control structures (loops, conditionals)\n"
            "- Data structures (arrays, linked lists)\n"
            "- Object-oriented programming\n"
            "- Algorithms (sorting, searching)\n\n"
            "Or click 'Browse Concepts' to see all available topics."
        )
        self.add_message("Tutor", welcome_msg, 'bot')
    
    def add_message(self, sender, message, sender_type='user'):
        self.chat_display.config(state='normal')
        
        if sender_type == 'user':
            self.chat_display.insert(tk.END, f"{sender}: ", 'user_label')
            self.chat_display.insert(tk.END, f"{message}\n\n", 'user_input')
        else:
            self.chat_display.insert(tk.END, f"{sender}: ", 'bot')
            
            lines = message.split('\n')
            for line in lines:
                if any(keyword in line.lower() for keyword in ['example:', 'syntax:']):
                    self.chat_display.insert(tk.END, line + '\n', 'highlight')
                elif line.strip().startswith(('#', '//', 'def ', 'class ')):
                    self.chat_display.insert(tk.END, line + '\n', 'code')
                else:
                    self.chat_display.insert(tk.END, line + '\n')
        
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)
    
    def add_reference_links(self, references):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, "\n📚 References:\n", 'bot')
        
        for ref in references:
            btn = tk.Button(
                self.chat_display, text=ref['text'], 
                command=lambda url=ref['url']: webbrowser.open_new(url),
                font=('Segoe UI', 9), relief=tk.FLAT,
                fg='#0645ad', cursor="hand2",
                activeforeground='#0b0080'
            )
            self.chat_display.window_create(tk.END, window=btn)
            self.chat_display.insert(tk.END, "\n")
        
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)
    
    def process_input(self):
        user_text = self.user_input.get().strip()
        if not user_text:
            return
        
        self.add_message("You", user_text)
        self.user_input.delete(0, tk.END)
        
        if self.current_question:
            self.check_answer(user_text)
        else:
            self.handle_query(user_text.lower())
    
    def handle_query(self, query):
        for category in self.concepts.values():
            for concept in category:
                if (concept['name'].lower() in query or 
                    any(keyword in query for keyword in concept.get('keywords', []))):
                    self.explain_concept(concept)
                    return
        
        if any(g in query for g in ["hello", "hi", "hey"]):
            self.add_message("Tutor", "Hello! What programming concept would you like to learn about?", 'bot')
        elif "thank" in query:
            self.add_message("Tutor", "You're welcome! Let me know if you have more questions.", 'bot')
        elif "yes" in query and self.current_concept:
            self.start_practice_with_current()
        elif "no" in query and self.current_concept:
            self.add_message("Tutor", "Okay, what would you like to learn about instead?", 'bot')
        elif any(w in query for w in ["what", "how", "explain", "?"]):
            self.add_message("Tutor", "I can explain programming concepts. Try being more specific, like 'explain variables' or 'how do loops work'.", 'bot')
        else:
            self.add_message("Tutor", "I'm not sure I understand. Try asking about a specific programming concept or click 'Browse Concepts'.", 'bot')
    
    def show_concept_menu(self):
        self.add_message("Tutor", "Available programming concepts:", 'bot')
        
        for category, concepts in self.concepts.items():
            self.chat_display.config(state='normal')
            self.chat_display.insert(tk.END, f"\n{category}:\n", 'bot')
            
            for concept in concepts:
                btn = tk.Button(
                    self.chat_display, text=concept['name'], 
                    command=lambda c=concept: self.explain_concept(c),
                    font=('Segoe UI', 9), relief=tk.FLAT,
                    bg='#e3f2fd', activebackground='#bbdefb'
                )
                self.chat_display.window_create(tk.END, window=btn)
                self.chat_display.insert(tk.END, "  ")
            
            self.chat_display.config(state='disabled')
        
        self.chat_display.see(tk.END)
    
    def explain_concept(self, concept):
        self.current_concept = concept
        
        response = (
            f"📚 {concept['name']}\n"
            f"{concept['definition']}\n\n"
            f"🔑 Key Points:\n"
        )
        
        for point in concept['key_points']:
            response += f"- {point}\n"
        
        response += "\n📝 Syntax Examples:\n"
        for lang, syntax in concept['syntax'].items():
            response += f"{lang}:\n{syntax}\n"
        
        response += "\n💻 Example Usage:\n"
        response += f"{concept['example']}\n\n"
        response += f"🏷️ Common Uses: {concept['common_uses']}\n\n"
        
        self.add_message("Tutor", response, 'bot')
        self.add_reference_links(concept['references'])
        self.add_message("Tutor", "\nWould you like to practice this concept? (yes/no)", 'bot')
    
    def start_practice_with_current(self):
        if self.current_concept and self.current_concept['questions']:
            self.current_question = random.choice(self.current_concept['questions'])
            self.add_message("Tutor", f"Question about {self.current_concept['name']}:\n{self.current_question['text']}", 'bot')
        else:
            self.add_message("Tutor", "There are no practice questions available for this concept yet.", 'bot')
    
    def check_answer(self, answer):
        correct = any(a.lower() == answer.lower() 
                     for a in self.current_question['answers'])
        
        if correct:
            response = "✅ Correct! " + random.choice([
                "Well done!",
                "You've got it!",
                "Excellent understanding!"
            ])
        else:
            response = "❌ Not quite. " + random.choice([
                "The correct answer is: " + self.current_question['answers'][0],
                "Remember that: " + self.current_question['answers'][0],
                "Let's review: " + self.current_question['answers'][0]
            ])
        
        self.add_message("Tutor", response, 'bot')
        self.current_question = None
        self.add_message("Tutor", "Would you like to learn about another concept?", 'bot')
    
    def start_practice(self):
        known_concepts = [c for cat in self.concepts.values() for c in cat 
                        if self.user_progress.get(c['name'])]
        
        if known_concepts:
            self.current_concept = random.choice(known_concepts)
            self.start_practice_with_current()
        else:
            self.add_message("Tutor", "First learn some concepts before practicing. Try browsing concepts!", 'bot')

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgrammingTutor(root)
    root.mainloop()