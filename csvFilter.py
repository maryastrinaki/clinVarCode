import json
file = open('test.json')
data = json.load(file) # now the JSON object is represented as Python dict
output_file=open("output.csv",'w')
pos=[]
data_line=""
header=["assembly","chr","start","stop","strand","clinical significance","condition(s)","GMAF","Allele frequency"]
header_line=','.join(header)
output_file.write(header_line)
output_file.write('\n')

#https://www.ncbi.nlm.nih.gov/clinvar/RCV000009462/ example for allele frequency exac


for d in data:
	try:

		if "single nucleotide variant" in d['variant type']:

			for z,assembly in enumerate(d["Assembly"]):

				if assembly=="GRCh37":
					pos.append(z)
					for f,m in enumerate(pos):

					
						dataLine=d['Assembly'][m],d['chr'][m],d['start'][m],d['stop'][m],d['strand'][m],d['clinical significance'],d['condition(s)'],d['Global Allele Freguency '],d['GO_ESP']
						data_line=','.join(map(str, dataLine))
		if d['start'][m]!=d['stop'][m]:
			raise ValueError("That is not a single nucleotide variant!")
		output_file.write(data_line+'\n')

	except ValueError as ve:
		print(ve)
	
print("finished")
						



	


	
				

		

output_file.close() 
