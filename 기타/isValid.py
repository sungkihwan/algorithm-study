s = "[[[([]){}]]]"
st = []
m = {"]": "[", "}": "{", ")": "("}
result = True

for i in s:
    if i == "]" or i == "}" or i == ")":
        if st.pop() != m[i]:
            result = False
            break
    else:
        st.append(i)

print(result)

