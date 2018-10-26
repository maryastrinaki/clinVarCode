import json
file = open('skata.json')
data = json.load(file) # now the JSON object is represented as Python dict
output_file=open("output_filename.csv",'w')
pos=[]
data_line=""
header=["assembly","chr","start","stop","strand","clinical significance","condition(s)","GMAF","Allele frequency"]
header_line=','.join(header)
output_file.write(header_line)
output_file.write('\n')

#https://www.ncbi.nlm.nih.gov/clinvar/RCV000009462/ example for allele frequency exac


for d in data:

	if "single nucleotide variant" in d['variant type']:

		for z,assembly in enumerate(d["Assembly"]):

			if assembly=="GRCh37":
				print("assembly",z,assembly)
				pos.append(z)
				print(pos)
				for f,m in enumerate(pos):
					
					dataLine=d['Assembly'][m],d['chr'][m],d['start'][m],d['stop'][m],d['strand'][m],d['clinical significance'],d['condition(s)'],d['Global Allele Freguency '],d['GO_ESP']
					data_line=','.join(map(str, dataLine))
	output_file.write(data_line+'\n')
	
						



	


	
				

		

output_file.close() 
