
#import asyncio
import json
import xml.sax


def pprint(d):
    print (json.dumps(d, indent=4))

#@asyncio.coroutine
def consumer():
    '''
    Do whatever you want
    '''

    while True:
        content = (yield)
        #print (content['ClinVarSet'][0]['Title'][0]['TEXT'])
        


class ClinVarHandler( xml.sax.ContentHandler ):
    def __init__(self, consumer):
        self.content = {}
        self.path = []
        self.root_counter = 0
        self.consumer = consumer
        self.consumer.send(None)

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
                pprint(cvs)
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


if __name__ == '__main__':

    '''
<ClinVarSet ID="18522034">
  <RecordStatus>current</RecordStatus>
  <Title>NC_000006.10:g.(160991083_161362841)_(170663087_170899992)del AND multiple conditions</Title>
  <ReferenceClinVarAssertion DateCreated="2014-06-13" DateLastUpdated="2017-04-05" ID="286872">
    <ClinVarAccession Acc="RCV000122723" Version="1" Type="RCV" DateUpdated="2017-04-05"/>


    '''

    filename = '/home/maryastr/clinVar/clinVarCode/ClinVarFullRelease_2018-07.xml'
    parser = xml.sax.make_parser()
    Handler = ClinVarHandler(consumer())

    parser.setContentHandler( Handler )

    parser.parse(filename)

