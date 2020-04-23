def converter(input):
    # print(input.split())
    a = input.split()
    output = "def "+ a[0] + "(t):\n\t" + ''.join(a[2:]) + "\n\tt.value=(t.value,{'type':t.type})\n\treturn t\n\n"
    return output

# converter("t_php_IS_EQUAL_TO            = r'=='")

fi = open("converter_in.txt","r")
fo = open("converter_out.txt","w")
with fi as a_file:
  for line in a_file:
    stripped_line = line.strip()
    if(stripped_line==""):
        fo.write("\n")
    else:
        # print(stripped_line)
        fo.write(converter(stripped_line))