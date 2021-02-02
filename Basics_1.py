#creating variables for datatypes

v_str = "abc"
v_int = 1
v_float = 1.2
v_complex = 1+1j
v_seq = [1,2,3,4]
v_tuple = [5,6,7,8]
v_range = range(1,2,1)
v_dict = {1:"a",2:"b" }
v_set = {1,2,3,4}
v_frz_set = frozenset(v_set)
v_true = True
v_false = False
v_binary = bin(2)
v_bytearray = bytearray(2)
v_mv = memoryview(v_bytearray)

print ("the datatype of v_str is", type(v_str))
print ("the datatype of v_int is", type(v_int))
print ("the datatype of v_float is", type(v_float))
print ("the datatype of v_complex is", type(v_complex))
print ("the datatype of v_seq is", type(v_seq))
print ("the datatype of v_tuple is", type(v_tuple))
print ("the datatype of v_range is", type(v_range))
print ("the datatype of v_dict is", type(v_dict))
print ("the datatype of v_set is", type(v_set))
print ("the datatype of v_frz_set is", type(v_frz_set))
print ("the datatype of v_true is", type(v_true))
print ("the datatype of v_false is", type(v_false))
print ("the datatype of v_binary is", type(v_binary))
print ("the datatype of v_bytearray is", type(v_bytearray))
print ("the datatype of v_mv is", type(v_mv))


