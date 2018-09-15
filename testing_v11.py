import xml.sax
from pandas import read_csv
import datetime
import gzip
import csv

'''
Very well done!
Keep on!
'''

class ClinVarHandler( xml.sax.ContentHandler):


	

	def __init__(self,output_filename):

		self.CurrentData=""
		self.Title=""
		self.XRef =""
		self.SequenceLocation=""
		self.ReviewStatus=""
		self.Description=""
		self.TraitSet=""
		self.Trait=""
		self.Citation=""
		self.ID=""
		self.ClinVarSubmissionID =""
		self.ClinicalSignificance=""
		self.parentflag = False
		self.parentflag2=False
		self.childlist=""
		self.childlist2=""
		self.childReviewStatus=[]
		self.text=""
		self.childlist_title=""

		self.id_XRef=""
		self.db_XRef=""
		self.DateLastEvaluatedSignificance=""
		self.TraitSetType=""
		self.TraiSetTypeId=""
		self.TraitType=""
		self.TraitId=""
		self.Origin=""
		self.childlist_Origin=""
		self.childlist_MethodType=""
		self.MethodType=""
		self.ClinVarAccession=""
		self.Strand=""
		self.assemblyStatus=""
		self.variantLength=""
		self.MeasureSet=""
		self.MeasureType=""
		self.MeasureId=""
		self.Measure=""
		self.variationType=""
		self.variationId=""
		self.RecordStatus=""
		self.RecordStatuschild=[]
		self.MeasureChild=""
		self.CytogeneticLocation=""
		self.CytogeneticLocationchild=""
		self.localKeySub=""
		self.submitterSub=""
		self.submitterDateSub=""
		self.titleSub=""
		self.attributeType=""
		self.specificattributeType=""
		self.MeasureRelationship=""
		self.MeasureRelationshipType=""
		self.parentflag3 = False
		self.childlist3=""
		self.ElementValue=""
		self.MeaureValue=""
		self.condition=""
		self.paraentflag4=False
		self.childHGVS=""
		self.Accession=""
		self.SubmissionAccession=""
		self.clinVarAccessionType=""
		self.ClinVarAccession1=""
		self.RCV=""
		self.SCV=[]
		self.clinvarexample=""
		self.ClinVarSet=""
		self.childlist4=""
		self.childChromosome=""
		self.childassembly=""
		self.childAssemblyStatus=""		
		self.childstrand=""
		self.childvariantLength=""
		self.childisplayStart=""
		self.childisplayStop=""
		self.childouterStart=""
		self.childouterStop=""
		self.childinnerstart=""
		self.childinnerstop=""
		self.childstart=""
		self.childstop=""
		self.childRCV=""
		self.childSCV=""
		self.childEvaluate=""
		self.abbrevCitation=""
		self.IDcitation=""
		self.citation_id=""
		self.childcitationid=""
		self.parentflag5=False
		self.child5=""
		self.childb=""
		self.i=0
		self.example=[]

		self.childReview=""
		self.exampleReview=[]
		self.exampleRecordStatus=[]
		self.exampleDate=[]
		self.exampleOrigin=[]
		self.examplesubmitterSub=[]
		self.examplesubmitterDateSub=[]
		self.exampleMethod=[]
		self.childattributeMconsequence=[]
		self.childattributeHGVS=[]
		self.childProteinChange=[]
		self.refAllele=""
		self.alterAllele=""
		self.positionAlleleVCF=""
		self.refAlleleVCF=""
		self.alterAlleleVCF=""
		self.childrefAllele=""
		self.childalterAllele=""
		self.childpositionAlleleVCF=""
		self.childrefAlleleVCF=""
		self.childalterAlleleVCF=""
		self.exampleElement=""
		self.parentflagExample=""
		self.text_content=[]
		self.inside_text_tag = False
		self.idXREFtrait=[]
		self.dbXREFtrait=[]
		self.exampleFuck=[]
		self.relations=[]
		self.parentnameflag=False
		self.XrefName=[]
		self.XrefNamedb=[]
		self.chiltrait=[]
		self.childlist3trait=[]
		self.Refparentflag=False
		self.parentflagclinical = False
		self.ClinVarparentflag=False
		self.RecordStatuschildclinvar=[]
		self.childReviewStatuclinvars=[]
		self.childDescriptionclinvars=[]
		self.RecordStatuschild=[]
		self.childReviewStatus=[]
		self.childDescription=[]
		self.originClinVarAssertion=[]
		self.childRefElement=[]
		self.clinMethod=[]
		self.clinSignificance=False
		
		
	
		
	



		
		
		self.ClinaVarsetID, self.ChromoSome0, self.ClinicalSign, self.assembly,self.Start,self.End,self.displayStart,self.displayStop,self.outerStart,self.outerStop,self.start,self.stop,self.innerstart,self.innerstop,self.clinicalSignificance="","","","","","","","","","","","","","",""

		self.output_file=open(output_filename,'w')
		
		
		header=["ID clinVar","Variant type","chromosome","Assembly","Assembly Status","Strand","variantLength","displayStart","displayStop","outerStart","outerStop","innerstart","innerstop","start","stop","referenceAllele","alternateAllele","positionVCF","referenceAlleleVCF","alternateAlleleVCF","Record Status(clinVar)","review status(clinVar)","clinical significance(clinvar)","Accession(clinVar)","Cytogenetic location","Protein change","HGVS","Mollecular Consequence","conditions-Identifier","conditions-Name","clinical assertion(Record Status)","clinical assertion(Review Status)","clinical assertion(clinical Significance)","clinical assertion(Origin)","clinical assertion(submitter infor_who)","clinical assertion(submitter infor_date)","clinical assertion(method)","clinical assertion(citations)","clinical assertion(conditions-Mode of inheritance)","submission Accession","Title"]
		header_line=','.join(header)
		self.output_file.write(header_line+'\n')


	def startElement(self,tag,attributes):





		#print ("Element start: %s (%d attribute(s))" % (tag, len( attributes)))

		
		
		self.CurrentData=tag

		if tag=="ClinVarSet":

			self.i=0
			self.example=[]
			self.exampleReview=[]
			self.exampleRecordStatus=[]
			self.exampleDate=[]
			self.exampleOrigin=[]
			self.SCV=[]
			self.examplesubmitterSub=[]
			self.examplesubmitterDateSub=[]
			self.exampleMethod=[]
			self.childattributeHGVS=[]
			self.childattributeMconsequence=[]
			self.childProteinChange=[]
			self.Inheritance=[]
			self.text_content=[]
			self.idXREFtrait=[]
			self.dbXREFtrait=[]
			self.relations=[]
			self.RecordStatuschildclinvar=[]
			self.childReviewStatuclinvars=[]
			self.childDescriptionclinvars=[]
			self.RecordStatuschild=[]
			self.childReviewStatus=[]
			self.childDescription=[]
			self.originClinVarAssertion=[]
			self.childlist_Origin=[]
			self.childRefElement=[]
			self.clinMethod=[]
			self.citation_id=[]




		


			self.ClinaVarsetID=attributes.get('ID')



		if tag=="Trait":
			self.parentflag=True

			self.parentnameflag=True



		if tag=="Name":
			self.id_XRef=""
			self.db_XRef=""



		if tag=="ReferenceClinVarAssertion":
			self.Refparentflag=True




		if tag=="ClinVarAssertion":

			self.ClinVarparentflag=True



















		





			


				




		if tag=="ClinicalSignificance":

			self.DateLastEvaluatedSignificance=attributes.get('DateLastEvaluated')

			


		if tag=="MeasureSet":
			self.MeasureType=attributes.get('Type')
			self.MeasureId=attributes.get('ID')
			self.condition=self.childlist3
			
			
		#	print(self.condition)


		

		if tag=="Measure":

			self.variationType= attributes.get('Type')
			self.variationId=attributes.get('ID')
			
			#print(self.variationType)







		if tag=="XRef":
			self.id_XRef= attributes.get("ID")
			self.db_XRef=attributes.get("DB")

			


		

			
		
		
			



		if tag=="MeasureRelationship":

			


			if attributes.get("Type") is not None:

				self.MeasureRelationshipType=attributes.get("Type")

				



			elif attributes.get("Type") is None:

				self.MeasureRelationshipType='Nan'


			



	
			


			



			
		
		
	



		if tag=="SequenceLocation" :




				self.ChromoSome0=attributes.get("Chr")
				self.assembly=attributes.get("Assembly")
				


				if attributes.get("display_start") is None :
					self.displayStart='Nan'

				elif attributes.get("display_start") is not None :

					self.displayStart=attributes.get("display_start")

			


				if attributes.get("display_stop") is None:

					self.displayStop='Nan'

				elif attributes.get("display_stop") is not None:

					self.displayStop=attributes.get("display_stop")


				if attributes.get("outerStart") is None:

					self.outerStart='Nan'

				elif attributes.get("outerStart") is not  None:

					self.outerStart=attributes.get("outerStart")

				if attributes.get("outerStop") is None:

					self.outerStop='Nan'

				elif attributes.get("outerStop") is not None:

						self.outerStop=attributes.get("outerStop")

				if attributes.get("innerStart") is None:

					self.innerstart='Nan'

				elif attributes.get("innerStart") is not None:

					self.innerstart=attributes.get("innerStart")

				if attributes.get("innerStop") is None:
					self.innerstop='Nan'

				elif attributes.get("innerStop") is not None:

					self.innerstop=attributes.get("innerStop")

				if attributes.get("start") is  None:

					self.start='Nan'


				elif attributes.get("start") is not None:

					self.start=attributes.get("start")


				if attributes.get("stop") is  None:

					self.stop='Nan'


				elif attributes.get("stop") is not None:

					self.stop=attributes.get("stop")


				if attributes.get("AssemblyStatus") is None:
					self.AssemblyStatus='Nan'

				elif attributes.get("AssemblyStatus") is not None:
					self.AssemblyStatus=attributes.get("AssemblyStatus")


				if attributes.get("Strand") is None:

					self.strand='Nan'

				elif attributes.get("Strand") is not None:

					self.strand=attributes.get("Strand")


				if attributes.get("variantLength") is None :

					self.variantLength='Nan'

				elif attributes.get("variantLength") is not None :

					self.variantLength=attributes.get("variantLength")

				if attributes.get("referenceAllele") is None:

					self.refAllele='Nan'

				elif attributes.get("referenceAllele") is not None:

					self.refAllele=attributes.get("referenceAllele")

				if attributes.get("alternateAllele") is None:

					self.alterAllele='Nan'

				elif attributes.get("alternateAllele") is not None:

					self.alterAllele=attributes.get("alternateAllele")

				if attributes.get("positionVCF") is None:

					self.positionAlleleVCF='Nan'

				elif attributes.get("positionVCF") is not None:

					self.positionAlleleVCF=attributes.get("positionVCF")

				if attributes.get("referenceAlleleVCF") is None:

					self.refAlleleVCF='Nan'

				elif attributes.get("referenceAlleleVCF") is not None:

					self.refAlleleVCF=attributes.get("referenceAlleleVCF")

				if attributes.get("alternateAlleleVCF") is None:

					self.alterAlleleVCF='Nan'

				elif attributes.get("alternateAlleleVCF") is not None:

					self.alterAlleleVCF=attributes.get("alternateAlleleVCF")


		


		if tag=="TraitSet":



			self.TraitSetType= attributes.get('Type')




			if attributes.get('ID') is None :

				self.TraiSetTypeId= 'Nan'

			elif attributes.get('ID') is not None :

				self.TraiSetTypeId= attributes.get('ID')


			







		if tag=="Trait":

			self.TraitType=attributes.get('Type')

			if attributes.get('ID') is None :

				self.TraitId= 'Nan'

			elif attributes.get('ID') is not None :

				self.TraitId= attributes.get('ID')


			






			

			






			





			#print("Trait",TraitType)
					#Citations include published articles and URLs. If a database name and identifier are supplied, the full text is not required. Values include general, review, practice guideline, Position Statement, Translational/Evidence-based, Suggested Reading, and Recommendation

		if tag=="Citation" :

			self.Citation=attributes.get('Type')

			if attributes.get('Type') is None:

				self.Citation='Nan'

			if attributes.get('Abbrev') is not None:
				self.abbrevCitation=attributes.get('Abbrev')

			if attributes.get('Abbrev') is None:
				self.abbrevCitation='Nan'

			self.childcitationid=self.citation_id
			



		if tag=="ReferenceClinVarAssertion":

			self.Refparentflag=True


		if tag == "ClinicalSignificance":

			self.clinSignificance=True



			

			


			
			






		

		if tag=="ID":
			self.IDcitation=attributes.get('Source')

			#print("Source for Citation",a)


#Submitter of record (required)/other official submitters (optional)
		if tag=="ClinVarSubmissionID":
			self.localKeySub=attributes.get('localKey')
			self.submitterSub=attributes.get('submitter')
			self.submitterDateSub=attributes.get('submitterDate')








			
		
		


		
				




		

	















					
		if tag=="ClinVarAccession" and attributes.get("Type")=="RCV":

			
			self.RCV=attributes.get('Acc')


		if tag=="ClinVarAccession" and attributes.get("Type")=="SCV":

			
			self.SCV.append(attributes.get('Acc'))




		if tag=="Attribute":

			if attributes.get('Type')=="HGVS":

				self.childattributeHGVS.append(self.attribute)

			elif attributes.get('Type')=="MolecularConsequence":

				self.childattributeMconsequence.append(self.attribute)

			elif attributes.get('Type')=="ProteinChange1LetterCode":

				self.childProteinChange.append(self.attribute)

			elif attributes.get('Type')=="ProteinChange3LetterCode":

				self.childProteinChange.append(self.attribute)

			elif attributes.get('Type')=="ModeOfInheritance":

				self.Inheritance.append(self.attribute)




		if tag == 'Trait':
			self.inside_text_tag = True
			

			








			
			
			

			
		






		if tag=="ElementValue":

			if attributes.get('Type')=="Preferred":
				self.exampleElement=self.ElementValue




			
			
			


		








		






			









		#	self.attributeType=attributes.get('Type')

		#	if self.attributeType=="MolecularConsequence":

			#	self.childattribute=self.attribute

			#elif self.attributeType!="MolecularConsequence":

				#self.childattribute="Nan molecular consequence"

			#if self.attributeType=="HGVS":

				#self.childattributeHGVS=self.attribute

			

		#	print(self.ClinaVarsetID+' '+self.childattributeHGVS)






		


			#if  attributes.get("Type")=="SCV":

				#self.SCV=self.ClinVarAccession
				#self.SCV=attributes.get('Acc')

			#if  attributes.get("Type")=="RCV":

				#self.RCV=self.ClinVarAccession


				
				#self.RCV=attributes.get('Acc')

				#print("vrika to clinvarAccession",self.RCV + '#'+ self.ClinaVarsetID)


			#if  attributes.get("Type")=="SCV":

			#	self.SCV=self.ClinVarAccession

			#	print("vrika to clinvarAccession",self.SCV + '#'+ self.ClinaVarsetID+ '#'+self.RCV)


			

			
		



		#and attributes.get("Type")=="SCV" :

		#	self.ClinVarAccession=attributes.get('Acc')

		#	print(self.ClinVarAccession)

		#if tag=="ClinVarAccession" and  attributes.get("Type")=="RCV":

		#	self.ClinVarAccession1=attributes.get('Acc')

			#print(self.ClinVarAccession1)


			
	

			

			#if self.clinVarAccession=="SCV" and self.ClinVarAccession is not None:

			#	self.SubmissionAccession=self.ClinVarAccession
		

		
 

	def endElement (self,tag):

		if tag=="XRef" and self.parentflag==True and self.parentnameflag==False:

			self.id_XRef=self.id_XRef
			self.db_XRef=self.db_XRef

			self.relations.append((self.id_XRef,self.db_XRef))





		
			
		


		


		if tag=="Name":
			self.parentnameflag = False

			self.XrefName.append(self.id_XRef)
			self.XrefNamedb.append(self.db_XRef)

			#self.exampleName=self.id_XRef






		if tag == "Trait":


			self.parentflag = False

			#if self.id_XRef is not None:

			self.chiltrait.append(self.id_XRef)
			self.childlist3trait.append(self.db_XRef)

		#print ("Element end: %s" % tag)

		if tag == 'Trait':
			self.inside_text_tag = False


		if tag=="ElementValue" and self.parentflag==True and self.parentnameflag==True and self.Refparentflag==True:

			self.childRefElement.append(self.ElementValue)




		if tag=="ClinVarSubmissionID":
			self.localKeySub=self.localKeySub
			self.submitterSub=self.submitterSub
			self.submitterDateSub=self.submitterDateSub

			if self.submitterSub is not None:

				self.examplesubmitterSub.append(self.submitterSub)

			elif self.submitterSub is  None:

				self.examplesubmitterSub.append("no submitter Infor")


			if self.submitterDateSub is not None:

				self.examplesubmitterDateSub.append(self.submitterDateSub)

			elif self.submitterDateSub is None:

				self.examplesubmitterDateSub.append("no submiter Date ")


			
			

			




			

			

		
			
			

		






		if tag=="ReferenceClinVarAssertion":
			self.Refparentflag=False



		if tag=="ClinVarAssertion":

			self.ClinVarparentflag=True


		if tag=="Citation":

			 self.CitationExaple=True


		if tag=="ClinicalSignificance":

			self.clinSignificance=False


		if self.CurrentData=="RecordStatus" and self.ClinVarparentflag==True:
			self.RecordStatuschildclinvar.append(self.RecordStatus)
			


		if self.CurrentData=="ReviewStatus" and self.ClinVarparentflag==True :

			self.childReviewStatuclinvars.append(self.ReviewStatus)
			


		if tag == "ClinicalSignificance" and self.ClinVarparentflag==True:
			self.childDescriptionclinvars.append(self.Description)

		if self.CurrentData=="Origin" and self.ClinVarparentflag==True:
			
			self.childlist_Origin.append(self.Origin)
			



			



		if self.CurrentData=="RecordStatus" and self.Refparentflag==True:
			self.RecordStatuschild.append(self.RecordStatus)


		if self.CurrentData=="ReviewStatus" and self.Refparentflag==True :

			self.childReviewStatus.append(self.ReviewStatus)


		if tag == "ClinicalSignificance" and self.Refparentflag==True:
			self.childDescription.append(self.Description)


		
		


		





			
			





		if tag=="Name":
			self.exampleName=self.exampleElement
		






		if self.CurrentData=="Title":
			self.childlist_title=self.Title






		if self.CurrentData=="MethodType" and self.ClinVarparentflag==True:

			self.clinMethod.append(self.MethodType)




		if self.CurrentData=="Measure":
			self.MeasureChild=self.Measure

			






			
		if self.CurrentData=="CytogeneticLocation":

			self.CytogeneticLocationchild=self.CytogeneticLocation


		


		if self.CurrentData=="ID" and self.ClinVarparentflag==True and self.clinSignificance==True and self.CitationExaple==True:

			self.citation_id.append((self.IDcitation,self.ID))

	










		if tag=="SequenceLocation":

		

			

			self.childChromosome=self.ChromoSome0
			self.childassembly=self.assembly
			self.childAssemblyStatus=self.AssemblyStatus		
			self.childstrand=self.strand
			self.childvariantLength=self.variantLength
			self.childisplayStart=self.displayStart
			self.childisplayStop=self.displayStop
			self.childouterStart=self.outerStart
			self.childouterStop=self.outerStop
			self.childinnerstart=self.innerstart
			self.childinnerstop=self.innerstop
			self.childstart=self.start
			self.childstop=self.stop
			self.childrefAllele=self.refAllele
			self.childalterAllele=self.alterAllele
			self.childpositionAlleleVCF=self.positionAlleleVCF
			self.childrefAlleleVCF=self.refAlleleVCF
			self.childalterAlleleVCF=self.alterAlleleVCF

			


			
		
		
		
		


			#data =[self.ClinaVarsetID,self.variationType,self.childChromosome,self.childassembly,self.childAssemblyStatus,self.childstrand,self.childvariantLength,self.childisplayStart,self.childisplayStop,self.childouterStart,self.childouterStop,self.childinnerstart,self.childinnerstop,self.childstart,self.childstop]

			
			data =[','+self.ClinaVarsetID ,self.variationType,self.childChromosome,self.childassembly,self.childAssemblyStatus,self.childstrand,self.childvariantLength,self.childisplayStart,self.childisplayStop,self.childouterStart,self.childouterStop,self.childinnerstart,self.childinnerstop,self.childstart,self.childstop,self.childrefAllele,self.childalterAllele,self.childpositionAlleleVCF,self.childrefAlleleVCF,self.childalterAlleleVCF]
			data_line=','.join(map(str, data))


			


			self.output_file.write(data_line+',')	

			self.output_file.write('\n')
		




		










		


		
			




		if tag=="ClinVarSet":
			self.output_file.write("clinVar"+' '+str(self.RecordStatuschild)+',')
			self.output_file.write("clinVar"+' '+str(self.childReviewStatus)+',')
			self.output_file.write("clinVar"+' '+str(self.childDescription)+',')
			self.output_file.write(self.RCV+',')

			



			self.output_file.write(self.CytogeneticLocationchild+',')
			self.output_file.write(str(self.childProteinChange)+',')
			self.output_file.write(str(self.childattributeHGVS)+',')
			self.output_file.write(str(self.childattributeMconsequence)+',')
			self.output_file.write("identifier"+" "+str(self.relations)+',')
			self.output_file.write("condition-name"+" "+str(self.childRefElement)+',')


			self.output_file.write("clinical assertion"+" "+str(self.RecordStatuschildclinvar)+',')
			self.output_file.write("clinical assertion"+" "+ str(self.childReviewStatuclinvars)+',')
			self.output_file.write("clinical assertion"+" "+str(self.childDescriptionclinvars)+',')
			self.output_file.write("clinical assertion"+" " + str(self.childlist_Origin)+',')
			self.output_file.write("clinical assertion(submitter infor_who)"+" "+ str(self.examplesubmitterSub)+',')
			self.output_file.write("clinical assertion(submitter infor_date)"+" "+ str(self.examplesubmitterDateSub)+',')
			self.output_file.write("clinical assertion(method)"+" "+ str(self.clinMethod)+',')
			self.output_file.write("clinical assertion(citations)"+" "+ str(self.citation_id)+',')
			self.output_file.write("clinical assertion(conditions-Mode of inheritance)"+" "+ str(self.Inheritance)+',')

			self.output_file.write(str(self.SCV)+',')
		
		

			self.output_file.write(' ')


			data=[self.childlist_title]
			data_line=','.join(map(str, data))
			self.output_file.write(data_line+',')
			

			print("conditions",self.childRefElement)
			print("eimai to identifier",self.relations)
			print("method",self.clinMethod)
			print("citations",self.citation_id)

		







			



	


		




		

		



			

			

			



			



			


			


			




		self.CurrentData=""



		

		







	def characters(self,content):
		

		if self.CurrentData=="Title":

			self.Title =content

		if self.CurrentData=="XRef":

			self.XRef =content
			

		if self.CurrentData=="SequenceLocation":

			self.SequenceLocation =content

		if self.CurrentData=="ReviewStatus":

			self. ReviewStatus=content

		if self.CurrentData=="Description":

			self.Description=content

		if self.CurrentData=="TraitSet":
			self.TraitSet=content

		if self.CurrentData=="Trait":
			self.Trait=content



		if self.CurrentData=="Citation":
			self.Citation=content

		if self.CurrentData=="ID":
			self.ID=content

		if self.CurrentData=="ClinVarSubmissionID":

			self.ClinVarSubmissionID =content

		if self.CurrentData=="Origin":

			self.Origin=content

		if self.CurrentData=="MethodType":

			self.MethodType=content

		if self.CurrentData=="ClinVarAccession" :

			self.ClinVarAccession=content


		if self.CurrentData=='MeasureSet':
			self.MeasureSet=content


		if self.CurrentData=="RecordStatus":

			self.RecordStatus=content


		if self.CurrentData=="Measure":

			self.Measure =content



		if self.CurrentData=="CytogeneticLocation":

			self.CytogeneticLocation=content


		if self.CurrentData=="Attribute":

			self.attribute=content
		


		if self.CurrentData=="MeasureRelationship":

			self.MeasureRelationship=content
		


		if self.CurrentData=="ElementValue":

			self.ElementValue=content


		if self.inside_text_tag:
			self.text_content.append(content)

			
			



	

		



		
if( __name__ =="__main__"):

	
	parser = xml.sax.make_parser()
	# turn off namepsaces
	parser.setFeature(xml.sax.handler.feature_namespaces,0)
	Handler=ClinVarHandler("euterpi.csv")

	parser.setContentHandler(Handler)
	
	parser.parse("test2.xml")


	










	
	
	

	
	
	
