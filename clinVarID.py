import xml.sax
import gzip
import xml.sax.saxutils as saxutils
import json


class ClinVarHandler( xml.sax.ContentHandler):

	def __init__(self,output_filename):

		self.CurrentData=""
		self.ClinaVarsetID=""
		self.data_line=[]
		self.output_file=open(output_filename,'w')

	def startElement(self,tag,attributes):

		self.CurrentData=tag

		if tag=="ClinVarSet":
			self.ClinaVarsetID=attributes.get('ID')
	def endElement (self,tag):

		if tag=="ClinVarSet":
			print("ID clinVar",self.ClinaVarsetID)
			
		self.data_line.append({"ID clinVar":self.ClinaVarsetID})

		self.CurrentData=""

	def __del__(self):
		self.output_file.write(json.dumps(self.data_line,sort_keys=False, indent=2))

	def characters(self,content):
		pass
	



if( __name__ =="__main__"):

	
	parser = xml.sax.make_parser()
	# turn off namepsaces
	parser.setFeature(xml.sax.handler.feature_namespaces,0)
	Handler=ClinVarHandler("finalmitsos.json")
	parser.setContentHandler(Handler)
	f=gzip.open("/home/maryastr/clinVar/clinVarCode/ClinVarFullRelease_2018-07.xml.gz")
	parser.parse(f)
	f.close()
