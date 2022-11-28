test = 'a'
print(type(test))

test = 1
print(type(test))

#comment

test1, test2, test3 = 1,2,3
print(test1)
print(test2)
print(test3)


testA = 5
testa = 10
print("testA is ",testA," and testa is ",testa)

testA = testB = testC = 'Focus'
print(testA)
print(testB)
print(testC)

testTuple = { 'TestA ','TestB ', 'TestC '}
TestA , TestB , TestC = testTuple
print(TestA,TestB,TestC)

testZ=9
a = float(testZ)
print(a)
print(type(a))
a = str(testZ)
print(a)
print(type(a))

a = 'test'
b = 1
print(a+str(b))

testHelp = """
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
print(testHelp)
