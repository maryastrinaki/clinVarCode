import json
#file = open('skata.json')
file = open('euterpi.json')
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
					pos=z
					print(d['Accession'])
					print(d['Assembly'][pos])
					print(d['chr'][pos])
					print(d['start'][pos])
					print(d['stop'][pos])
					print(d['strand'][pos])
					print(d['clinical significance'])
					print(d['condition(s)'])
					print(d['Global Allele Freguency '])
					print(d["Frequencies"],d["Accession"])
					if d['start'][pos]!=d['stop'][pos]:
						raise ValueError("That is not a single nucleotide variant!")
					dataLine=d['Assembly'][pos],d['chr'][pos],d['start'][pos],d['stop'][pos],d['strand'][pos],d['clinical significance'],d['condition(s)'],d['Global Allele Freguency '],d['Frequencies']
					data_line=','.join(map(str, dataLine))
					output_file.write(data_line+'\n')

	except ValueError as ve:
		print(ve)





	#except IndexError:
	#	pass

output_file.close() 
