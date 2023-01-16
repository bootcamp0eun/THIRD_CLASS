# 5.4
letter = '''\tDear {salutaion} {name},
\n\tThank you for your letter. We are sorry that our {product} {verbed} \
in your {room}. Please note that it should never be used in a {room}, \
especially near any {animals}.
\n\tSend us your receipt and {amount} for shipping and handling. \
We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.\
\n\n\tThank you for your suopport.
\tSincerely,
\t{spokesman}
\t{job_title}
'''

# 5.5

# 5.6
print("5.6")
list = ["duck", "gourd", "spitz"]
for i in range(0,len(list)):
    print("%sy Mc%sface" % (list[i].title(), list[i].title()))

# 5.7
print("\n5.7")
list = ["duck", "gourd", "spitz"]
for i in range(0,len(list)):
    print("{0}y Mc{0}face".format(list[i].title()))

# 5.8
print("\n5.8")
list = ["duck", "gourd", "spitz"]
for i in range(0,len(list)):
    print(f"{list[i].title()}y Mc{list[i].title()}face")