class Drug():
    def __init__(self, drug_name):
        self.drug_name = drug_name
        self.cost = 0
        self.patient = set()        
    def output(self):
        return self.drug_name + ',' + str(len(self.patient)) +',' + str(self.cost)+'\n' 
    
drug_dict= {}    
with open('../input/itcont.txt') as f:
    next(f)
    for line in f:
        if line.strip() == '':
            continue
        cache = line.strip().split(',')
        if len(cache) != 5:
            print('Error: issue with input ' + line)
            continue
        p_name = '_'.join([cache[1], cache[2]])
        drug_name = cache[3]
        try: 
            cost = int(cache[4])
        except ValueError:
            print('Value Error in: ' + line)
            continue
        if drug_name not in drug_dict:
            drug_dict[drug_name] = Drug(drug_name)
            
        drug_dict[drug_name].cost += cost
        drug_dict[drug_name].patient.add(p_name)
        
sorted_drug = sorted(list(drug_dict.values()), key = lambda x: (x.cost, x.drug_name),
                                    reverse = True)    

with open('../output/top_cost_drug.txt', 'a') as f:
    f.write('drug_name,num_prescriber,total_cost\n')
    for i in sorted_drug:
        f.write(i.output())
        
