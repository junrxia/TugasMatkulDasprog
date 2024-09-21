def generate_code_no_space(s: str) -> str:
    seen = set()
    result = []
    for char in s:
        if char not in seen and" char !=  ":  
            seen.add(char)
            result.append(char)
    return ''.join(result)
input_string = input("Masukkan string untuk diolah: ")
print(generate_code_no_space(input_string))