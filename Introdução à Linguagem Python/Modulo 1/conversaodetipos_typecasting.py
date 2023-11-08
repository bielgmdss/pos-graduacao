
# Para fazer a conversão, basta utilizar o nome do tipo e, entre parentes. passar o valor ou variavel que deseja converter

# Conversões para string 

bool_string = str(True)
bool_string2 = str(False)
int_string = str(5)
float_string = str(3.14159)

print(bool_string)
print(bool_string2)
print(int_string)
print(float_string)

# Conversões para int

string_int = int("2019")
bool_int = int(True) # qualquer valor se não for 0 ( zero ) é consideravel TRUE
bool_int2 = int(False) # apenas o valor 0 ( zero ) é consideravel FALSE
float_int = int(3.14169)
string_int2 = int("101", 2)
string_int3 = int("F0A23B", 16)

print(string_int)
print(bool_int)
print(bool_int2)
print(float_int)
print(string_int2)
print(string_int3)

# Conversões para float

string_float = float("3.14159")
string_float2 = float("3")
bool_float = float(True)
bool_float2 = float(False)
int_float = float(15)

print(string_float)
print(string_float2)
print(bool_float)
print(bool_float2)
print(int_float)

# Conversões para bool

string_bool = bool("Python")
string_bool2 = bool("True")
string_bool3 = bool("False")
int_bool = bool(17)
int_bool2 = bool(0)
float_bool = bool(3.14)
float_bool2 = bool(0.0)

print(string_bool)
print(string_bool2)
print(string_bool3)
print(int_bool)
print(int_bool2)
print(float_bool)
print(float_bool2)

