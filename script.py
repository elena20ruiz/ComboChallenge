import json
import datetime

with open('./api/src/data/template_input_person.json') as json_file:
    data = json.load(json_file)

    for s in data: 
        print(s)
        sala = data[s]
        i = 0

        for p in sala:
            algo = sala[p]
            for idk in algo:
                first = datetime.datetime.strptime(idk['ini'],'%H:%M:%S')
                second = datetime.datetime.strptime(idk['fi'],'%H:%M:%S')
                for p2 in sala:
                    if p != p2:
                        algo2 = sala[p2]  
                        for idk2 in algo2:
                            print(p + ' vs ' + p2)
                            print(idk)
                            print (idk2)
                            first2 = datetime.datetime.strptime(idk2['ini'],'%H:%M:%S')
                            second2 = datetime.datetime.strptime(idk2['fi'],'%H:%M:%S')
                            if (first >= first2 and second2 <= second) or (first <= first2 and second2 >= second):
                                print('yey esta tot be jeje')
            