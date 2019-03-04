'''
Reads an obj file and generates DWscript. Kinda messy.
To use, direct the output to a file:
`python objparse.py > script`
'''

FILENAME = "thanos.obj"

vertices = []

def draw_face(vs):
    print("line")
    print(' '.join(vertices[vs[0] - 1]) + ' ' + ' '.join(vertices[vs[1] - 1]))
    print("line")
    print(' '.join(vertices[vs[1] - 1]) + ' ' + ' '.join(vertices[vs[2] - 1]))
    print("line")
    print(' '.join(vertices[vs[2] - 1]) + ' ' + ' '.join(vertices[vs[0] - 1]))

with open(FILENAME, 'r') as obj:
    lines = obj.readlines()
    for line in lines:
        if line.startswith('v '):
            vertices.append(line.strip("v ").split())
    for line in lines:
        if line.startswith('f '):
            line = [int(v.split('/')[0]) for v in line.strip("f \n").split()]
            draw_face(line)

# Edit the rest of the script here
print('''
display

ident
scale
6 6 6 
translate
250 0 0
apply
display

ident
translate
-250 -250 0
rotate
x 30
rotate
y 20
translate
250 250 0
apply
display

ident
translate
-250 -250 0
rotate
y 145
rotate
z 10
translate
250 250 0

apply
display
save
thanos.png''')
