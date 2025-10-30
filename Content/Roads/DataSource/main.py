import math

def calculate_dot(p1,p2,p3):
    vector1 = [p2[0] - p1[0],p2[1] - p1[1],p2[2] - p1[2]]
    vector2 = [p3[0] - p2[0],p3[1] - p2[1],p3[2] - p2[2]]
    vector1_n = normalize_vector(vector1)
    vector2_n = normalize_vector(vector2)
    dot = vector2_n[0] * vector1_n[0] + vector2_n[1] * vector1_n[1] + vector2_n[2] * vector1_n[2]
    return dot

def normalize_vector(v):
    length = math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
    return [v[0]/length,v[1]/length,v[2]/length]

def output(points):
    # Outputfile
    f = open('out.csv', 'w')
    f.write("id,WKT\n")
    index = 0
    for line in points:
        wkt = "\""
        for p in line:
            wkt = wkt + str(p[0]) + " " + str(p[1]) + " " + str(p[2]) + ","
        f.write(str(index)+ "," + wkt+"\""+"\n")
        index+=1
    f.close()


with open('Kaufbeuren_main.csv','r') as csv:
    reader = csv.readlines()
    final_points = []
    for row in reader[1:]:
        line = row
        line = line.lstrip('0123456789,')
        line = line.replace("\"","")
        line = line.replace("MULTILINESTRING Z ((","")
        line = line.replace("))","")
        line_array = line.split("),(")
        print("Amount of lines:" + str(len(line_array)))
        for l in line_array:
            vectors = []
            vectors_cleaned = []
            point_array = l.split(",")
            for point in point_array:
                point_components = point.split(" ")
                vectors.append([float(point_components[0]),float(point_components[1]),float(point_components[2])])
                #vectors.append(point_components)
            vectors_cleaned.append(vectors[0])
            last_added = vectors[0]
            for i in range(2,len(vectors)):
                first = last_added
                second = vectors[i-1]
                current = vectors[i]
                dot = calculate_dot(first,second,current)
                #If angle big enough (like 30 degrees)
                if dot < math.cos(math.pi/6.0):
                    vectors_cleaned.append(second)
                    last_added = second
            vectors_cleaned.append(vectors[len(vectors)-1])
            final_points.append(vectors_cleaned)
    output(final_points)
