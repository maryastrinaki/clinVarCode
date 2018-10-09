import xml.sax

import gzip
import xml.sax.saxutils as saxutils
import json


class ClinVarHandler( xml.sax.ContentHandler):

  def __init__(self,output_filename):

    self.CurrentData=""
    self.ClinaVarsetID=""
    self.data_line=[]
    self.Title=[]
    self.childlist_title=""
    self.childlist_titleForException=[]
    self.RCV=[]
    self.RecordStatus=""
    self.Refparentflag=False
    self.RecordStatuschild=[]
   
    self.output_file=open(output_filename,'w')


  def startElement(self,tag,attributes):

    self.CurrentData=tag

    if tag=="ClinVarSet":
      self.Title=[]
      self.RCV=[]
      self.childlist_titleForException=[]
      self.RecordStatuschild=[]
      self.RecordStatus=""
      self.ClinaVarsetID=attributes.get('ID')

    if tag=="ClinVarAccession" and attributes.get("Type")=="RCV":

      if len(self.RCV)==0:

        self.RCV.append(attributes.get('Acc'))

      else:
        raise xml.sax.SAXException("Ooopss more than one RCV!!")


    if tag=="ReferenceClinVarAssertion":

      self.Refparentflag=True



    


      

      

      




  

  def endElement (self,tag):

    if self.CurrentData=="Title":

      self.childlist_title = ''.join(map(str,self.Title))
      if len(self.childlist_titleForException)==0:
        self.childlist_titleForException.append(self.childlist_title)
      else:
        raise xml.sax.SAXException("Ooopss more than one Titles!!")

    if self.CurrentData=="RecordStatus" and self.Refparentflag==True:
      if len(self.RecordStatuschild)==0:

        self.RecordStatuschild.append(self.RecordStatus)
      else:
        raise xml.sax.SAXException("Ooopss more than one Record status!!")

    if tag=="ReferenceClinVarAssertion":
      self.Refparentflag=False

    if tag=="ClinVarSet":
      print("record status",self.RecordStatuschild)
      
      self.data_line.append({"ID clinVar":self.ClinaVarsetID,"Title":self.childlist_titleForException,"Accession(clinVar)":self.RCV,"record status":self.RecordStatuschild})

    self.CurrentData=""

  def __del__(self):
    json.dump(self.data_line, self.output_file, indent=2)
    

  def characters(self,content):
    if self.CurrentData=="Title":

      self.Title.append(saxutils.unescape(content))

    if self.CurrentData=="RecordStatus":

      self.RecordStatus=content



if( __name__ =="__main__"):

  
  parser = xml.sax.make_parser()
  # turn off namepsaces
  parser.setFeature(xml.sax.handler.feature_namespaces,0)
  Handler=ClinVarHandler("finalmitsos.json")
  parser.setContentHandler(Handler)
  f=gzip.open("/home/maryastr/clinVar/clinVarCode/ClinVarFullRelease_2018-07.xml.gz")
  parser.parse(f)
  f.close()

