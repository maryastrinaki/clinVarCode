#import asyncio
import json
import xml.sax


def pprint(ofile,d):


    print (json.dumps(d, indent=4))
    ofile.write(json.dumps(d, indent=4))

#@asyncio.coroutine
def consumer():

    recordList=[]
    outerstart=[]
    outerstop=[]
    strand=[]
    innerstart=[]
    innerstop=[]
    displaystart=[]
    displaystop=[]
    start=[]
    stop=[]
    strand=[]
    HGVS=[]
    Cytogenic_Loc=[]
    submitter=[]
    submitterDate=[]
    Acc=[]
    Assertion_RecordStatus=[]
    DateEvaluated=[]
    AssertionReviewStatus=[]
    AssertionDescription=[]
    origin=[]
    AssertionMethod=[]
    assertion=[]
    ofile = open('patata.json','w')



    '''
    Do whatever you want
    '''

    while True:
        outerstart=[]
        outerstop=[]
        strand=[]
        innerstart=[]
        innerstop=[]
        displaystart=[]
        displaystop=[]
        start=[]
        stop=[]
        strand=[]
        HGVS=[]
        submitter=[]
        submitterDate=[]
        Acc=[]
        Assertion_RecordStatus=[]
        DateEvaluated=[]
        AssertionReviewStatus=[]
        AssertionDescription=[]
        origin=[]
        AssertionMethod=[]
        assertion=[]
        Cytogenic_Loc=[]
        content = (yield)

        for i in range(len(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'])):

            if "outerStart" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                outerstart.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['outerStart'])
            elif "outerStart" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                outerstart.append("Nan")

            if "outerStop" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                outerstop.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['outerStart'])
            elif "outerStop" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                outerstop.append("Nan")

            if "innerStart" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                innerstart.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['innerStart'])
            elif "innerStart" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                innerstart.append("Nan")
            if "innerStop" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                innerstop.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['innerStop'])
            elif "innerStop" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                innerstop.append('Nan')
            if "display_start" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                displaystart.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['display_start'])
            elif "display_start" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                displaystart.append('Nan')
            if "display_stop" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                displaystop.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['display_stop'])
            elif "display_stop" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                displaystop.append('Nan')
            if "start" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']:
                start.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']['start'])
            elif "start" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']:
                start.append('Nan')
            if "stop" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']:
                stop.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']['stop'])
            elif "stop" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']:
                stop.append('Nan')
            if "strand" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']:
                strand.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']['strand'])
            elif "strand" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']:
                strand.append("Nan")

        for i in range(len( content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'])):
          if "HGVS" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['attrs']['Type']:
            HGVS.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['TEXT'])
        if "CytogeneticLocation" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]:
            Cytogenic_Loc.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]["CytogeneticLocation"][0]["TEXT"])
        elif "CytogeneticLocation" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]:
            Cytogenic_Loc.append("Nan")
            
        for i in range(len(content['ClinVarSet'][0]['ClinVarAssertion']) ):
            submitter.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinVarSubmissionID'][0]['attrs']['submitter'])
            submitterDate.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinVarSubmissionID'][0]['attrs']['submitterDate'])
            Acc.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinVarAccession'][0]['attrs']['Acc'])
            Assertion_RecordStatus.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['RecordStatus'][0]['TEXT'])
            if "DateLastEvaluated" in content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinicalSignificance'][0]['attrs']:
                DateEvaluated.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinicalSignificance'][0]['attrs']['DateLastEvaluated'])
            elif "DateLastEvaluated" not in content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinicalSignificance'][0]['attrs']:
                DateEvaluated.append('Nan')
            AssertionReviewStatus.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinicalSignificance'][0]['ReviewStatus'][0]['TEXT'])
            AssertionDescription.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinicalSignificance'][0]['Description'][0]['TEXT'])
            origin.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ObservedIn'][0]['Sample'][0]['Origin'][0]['TEXT'])
            AssertionMethod.append(content['ClinVarSet'][0]['ClinVarAssertion'][0]['ObservedIn'][0]['Method'][0]['MethodType'][0]['TEXT'])

            if "Assertion" in content['ClinVarSet'][0]['ClinVarAssertion'][i]:

                assertion.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]["Assertion"][0]["attrs"]["Type"])

            elif "Assertion" not in content['ClinVarSet'][0]['ClinVarAssertion'][i]:
                assertion.append("nan")
      


        
        #pprint(content['ClinVarSet'][0]['ClinVarAssertion'][0]['ClinVarSubmissionID'][0]['attrs']['submitterDate'])
        #pprint(content['ClinVarSet'][0]['ClinVarAssertion'][0]['ClinVarAccession'][0]['attrs']['Acc'])
        #pprint(content['ClinVarSet'][0]['ClinVarAssertion'][0]['RecordStatus'][0]['TEXT'])


            








        

       

            
       

       

        recordList.append({"ClinVar Id":content['ClinVarSet'][0]['attrs']['ID'],"Record status":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['RecordStatus'][0]['TEXT'],"Title":content['ClinVarSet'][0]['Title'][0]['TEXT'],"Review status":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['ClinicalSignificance'][0]['ReviewStatus'][0]['TEXT'],"clinical significance":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['ClinicalSignificance'][0]['Description'][0]['TEXT'],"Accession":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['ClinVarAccession'][0]['attrs']['Acc'],"variant type":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['attrs']['Type'],

            "Assembly":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']['Assembly'],"chr":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']['Chr'],"outerstart": outerstart,"innerstart":innerstart,
            "innerstop":innerstop,"outerstop":outerstop,"displaystart":displaystart,"displaystop":displaystop,"start":start,"stop":stop,"variantLength":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']['variantLength'],
            "strand":strand,"HGVS":HGVS,"Cytogenetic Location":Cytogenic_Loc,"submitter(assertion)":submitter,"submission date(assertion)":submitterDate,"record status(assertion)":Assertion_RecordStatus,'Date Last Evaluate(assertion)':DateEvaluated,'review status(assertion)':AssertionReviewStatus,'Description(Assertion)':AssertionDescription,"Origin(Assertion)":origin,"Method(Assertion)":AssertionMethod,"Assertion":assertion

            })


        pprint(ofile, recordList)



      #  pprint(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']['Strand'])

       # pprint (content)

      
        


class ClinVarHandler( xml.sax.ContentHandler ):
    def __init__(self, consumer):
        self.content = {}
        self.path = []
        self.root_counter = 0
        self.consumer = consumer
        self.consumer.send(None)
        #self.ofile = open('patata','w')
       
   

    def build_url(self, entry):
        Acc =  entry['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['ClinVarAccession'][0]['attrs']['Acc']

        url_format = 'https://www.ncbi.nlm.nih.gov/clinvar/{Acc}/'

        return url_format.format(Acc=Acc)

    def build_variation_url(self, entry):

        measure_set_id = entry['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['attrs']['ID']
        url_format = 'https://www.ncbi.nlm.nih.gov/clinvar/variation/{measure_set_id}/'

        return url_format.format(measure_set_id=measure_set_id)


    def test_1(self, cvs):
        '''
        '''

        tests = [
            "'ClinVarSet' in cvs",
            "len(cvs['ClinVarSet']) == 1",
            "'ReferenceClinVarAssertion' in cvs['ClinVarSet'][0]",
            "len(cvs['ClinVarSet'][0]['ReferenceClinVarAssertion']) == 1",
            "'ClinVarAssertion' in cvs['ClinVarSet'][0]",
            #"len(cvs['ClinVarSet'][0]['ClinVarAssertion']) == 1",  # A ClinVarSet can have MANY ClinVarAssertions. For example: https://www.ncbi.nlm.nih.gov/clinvar/RCV000146116/ has 3 accessions
        ]

        for test in tests:
            if not eval(test):
                message = 'This test failed:\n{}\n'.format(test)
                pprint(ofile, cvs)
                raise Exception(message)

    def get_current(self,):
        current = self.content
        for p in self.path:
            current = current[p[0]][p[1]]

        return current

    def my_element_starts(self, element_name, attrs):
        '''
        {a: {   'attrs': [],
                'element_1': [],
                'element_2': [{}, {}, {
                            'fff_5': []
                }],
                'element_3': [],
                
            }
        }
        '''

        current = self.get_current()


        if not element_name in current:
            current[element_name] = []

        current[element_name].append({
            'attrs': attrs
        })

        self.path.append((element_name, len(current[element_name])-1))

        #pprint (self.content)

        #a=1/0

    def my_element_ends(self,):
        self.path.pop()

    def root_entry_ends(self,):
        #pprint(self.content)

        if False:
            print ('ClinVarSet URL:', self.build_url(self.content))
            print ('Variation URL:', self.build_variation_url(self.content))

        self.root_counter += 1
        if self.root_counter % 1000 == 0:
            print ('ClinVarSet entities parsed:', self.root_counter)

        self.test_1(self.content)

        self.consumer.send(self.content)

        self.content = {}
        self.path = []

    def startElement(self, tag, attributes):

        ## TODO FIXME AAAAAAAA THIS HAS VALUABLE INFORMAITON THAT WE DISCARD!
        if tag == 'ReleaseSet':
            return 

        attrs = dict(attributes)
        self.my_element_starts(tag, attrs)




      
    def endElement(self, tag):
        '''
        Call when an elements ends
        '''

        if tag == 'ReleaseSet':
            return
        
        self.my_element_ends()

        if tag == 'ClinVarSet':
            self.root_entry_ends()
            


    def characters(self, content):
        current = self.get_current()

        if content.strip():
            current_text = current.get('TEXT', '')
            current['TEXT'] = current_text + content.strip()


if( __name__ =="__main__"):

    filename = '/home/maryastr/clinVar/clinVarCode/test.xml'
    parser = xml.sax.make_parser()
    Handler = ClinVarHandler(consumer())
    parser.setContentHandler( Handler )
    parser.parse(filename)


#if __name__ == '__main__':

    '''
<ClinVarSet ID="18522034">
  <RecordStatus>current</RecordStatus>
  <Title>NC_000006.10:g.(160991083_161362841)_(170663087_170899992)del AND multiple conditions</Title>
  <ReferenceClinVarAssertion DateCreated="2014-06-13" DateLastUpdated="2017-04-05" ID="286872">
    <ClinVarAccession Acc="RCV000122723" Version="1" Type="RCV" DateUpdated="2017-04-05"/>
    '''

   # filename = '/home/maryastr/clinVar/clinVarCode/ClinVarFullRelease_2018-07.xml'
   # parser = xml.sax.make_parser()
   # Handler = ClinVarHandler(consumer())

    #parser.setContentHandler( Handler )
    #parser.parse(filename)
