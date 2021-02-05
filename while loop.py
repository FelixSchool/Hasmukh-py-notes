v_str = "123"
v_int = 12
v_float = 1.2
v_complex = 1+1j
v_seq = [1,2,3,4]
v_tuple = (5,6,7,8)
v_range = range(1,2,1)
v_dict = {1:"a",2:"b" }
v_set = set([1,2,3,4])
v_frz_set = frozenset(v_set)
v_true = True
v_false = False
v_binary = bin(2)
v_bytearray = bytearray(2)
v_mv = memoryview(v_bytearray)

i = int()
i = 0
datatype = [v_str,v_int,v_float,v_complex,v_seq,v_tuple,v_range,v_dict,v_set,v_frz_set,v_true,v_binary,v_bytearray,v_mv]

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

while i<=13:
    print("for",datatype[i])
    try:
        v1 = int(datatype[i])
        print("datatype for v1 is", type(v1))
    except Exception:
        print("cannot be converted")
    try:
        v2 = str(datatype[i])
        print("datatype for v2 is", type(v2))
    except Exception:
        print("cannot be converted")
    try:
        v3 = float(datatype[i])
        print("datatype for v3 is", type(v3))
    except Exception:
        print("cannot be converted")
    try:
        v4 = complex(datatype[i])
        print("datatype for v4 is", type(v4))
    except Exception:
        print("cannot be converted")
    try:
        v5 = [datatype[i]]
        print("datatype for v1 is", type(v5))
    except Exception:
        print("cannot be converted")
    try:
        v6 = (datatype[i])
        print("datatype for v1 is", type(v6))
    except Exception:
        print("cannot be converted")
    try:
        v7 = range(datatype[i])
        print("datatype for v1 is",type(v7))
    except Exception:
        print("cannot be converted")
    try:
        v8 = {1:datatype[i]}
        print("datatype for v1 is",type(v8))
    except Exception:
        print("cannot be converted")
    try:
        v9 = set(datatype[i])
        print("datatype for v1 is",type(v9))
    except Exception:
        print("cannot be converted")
    try:
        v10 = frozenset(datatype[i])
        print("datatype for v1 is",type(v10))
    except Exception:
        print("cannot be converted")
    try:
        v11 = bool(datatype[i])
        print("datatype for v1 is",type(v11))
    except Exception:
        print("cannot be converted")
    try:
        v12 = bin(datatype[i])
        print("datatype for v1 is",type(v12))
    except Exception:
        print("cannot be converted")
    try:
        v13 = bytearray(datatype[i])
        print("datatype for v1 is",type(v13))
    except Exception:
        print("cannot be converted")
    try:
        v14 = memoryview(datatype[i])
        print("datatype for v1 is",type(v14))
    except Exception:
        print("cannot be converted")
    i = i+1
