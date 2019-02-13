# read in the vectors.txt file
# create a  list of vectors
# scale the first and last vector by 3
# add them all together and find
# that new vector
# find the norm of the final vector
# also find the dot product between the 2nd and 3rd vector

from vector import Vector

with open('vectors.txt') as f:
    vec_list = []
    for line in f:
        vec = list(map(int, line.strip().split(',')))
        vec_list.append(Vector(*vec))

vec1_scale3 = vec_list[0].scale(3)
vec_last_scale3 = vec_list[-1].scale(3)

vec_list.append(vec1_scale3)
vec_list.append(vec_last_scale3)

new_vec = vec_list[0]

for i in range(1, len(vec_list)):
    new_vec = new_vec + vec_list[i]

final_norm = new_vec.length()
print(final_norm)
print(vec_list[1].dot(vec_list[2]))
