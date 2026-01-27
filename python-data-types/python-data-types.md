[PYTHON-BUILD-IN-DATA-TYPES] 

- In programming, data type is an important concept.

- Variables can store data of different types, and different types can do different things.

- Python has the following data types built-in by default, in these categories:

1. Text Type:	str
2. Numeric Types:	int, float, complex
3. Sequence Types:	list, tuple, range
4. Mapping Type:	dict
5. Set Types:	set, frozenset
6. Boolean Type:	bool
7. Binary Types:	bytes, bytearray, memoryview
8. None Type:	NoneType

[GETTING-THE-DATA-TYPE]

- You can get the data type of any object by using the type() function:

Print the data type of the variable x:

>>>x = 5
>>>print(type(x))

[SETTING-THE-DATA-TYPE]

- In python, the data type is set when you assign a value to a variable:

Examples

>>>x = "Hello World"  | Data Type: str	
>>>x = 20 | Data Type: int	
>>>x = 20.5	| Data Type: float	
>>>x = 1j | Data Type: complex	
>>>x = ["apple", "banana", "cherry"] | Data Type: list	
>>>x = ("apple", "banana", "cherry") | Data Type: tuple	
>>>x = range(6)	| Data Type: range	
>>>x = {"name" : "John", "age" : 36} | Data Type: dict	
>>>x = {"apple", "banana", "cherry"} | Data Type: set	
>>>x = frozenset({"apple", "banana", "cherry"})	| Data Type: frozenset	
>>>x = True	| Data Type: bool	
>>>x = b"Hello"	| Data Type: bytes	
>>>x = bytearray(5)	| Data Type: bytearray	
>>>x = memoryview(bytes(5))	| Data Type: memoryview	
>>>x = None	| Data Type: NoneType

[SETTING-THE-SPECIFI-DATA-TYPE]

- If you want to specify the data type, you can use the following constructor functions:

Examples

>>>x = str("Hello World")	
>>>x = int(20)		
>>>x = float(20.5)		
>>>x = complex(1j)	
>>>x = list(("apple", "banana", "cherry"))		
>>>x = tuple(("apple", "banana", "cherry"))	
>>>x = range(6)	
>>>x = dict(name="John", age=36)	
>>>x = set(("apple", "banana", "cherry"))		
>>>x = frozenset(("apple", "banana", "cherry"))		
>>>x = bool(5)		
>>>x = bytes(5)		
>>>x = bytearray(5)		
>>>x = memoryview(bytes(5))	

