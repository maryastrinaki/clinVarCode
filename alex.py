
import json
import xml.sax


def pprint(d):
    print (json.dumps(d, indent=4))



class ClinVarHandler( xml.sax.ContentHandler ):
    def __init__(self,):
        self.content = {}
        self.path = []
        self.root_counter = 0


    def test_1(self, cvs):
        t = 'ClinVarSet' in cvs

        if not t:
            pprint(cvs)
            a=1/0

        t = 'ReferenceClinVarAssertion' in cvs['ClinVarSet']
        if not t:
            pprint(cvs)
            a=1/0

        t = len(cvs['ClinVarSet']['ReferenceClinVarAssertion']['elements']) == 1
        if not t:
            pprint(cvs)
            a=1/0

        t = 'ClinVarAssertion' in cvs['ClinVarSet']
        if not t:
            pprint(cvs)
            a=1/0

        t = len(cvs['ClinVarSet']['ClinVarAssertion']['elements']) == 1
        if not t:
            pprint(cvs)
            a=1/0


    def ClinVarSet_starts(self, attrs):
        self.content['##'] = 'ClinVarSet'
        self.content['attrs'] = attrs

 
    def ClinVarSet_ends(self, ):
        pprint(self.content)
        a=1/0


    def my_element_starts(self, element_name, attrs):
        current = self.content
        for x in self.path:
            current = current[x]
        
        #print (current)
        if not element_name in current:
            current[element_name] = {
                'elements': []
            }

        current[element_name]['elements'].append({
            '##': element_name,
            'attrs': attrs,
        })

        self.path.append(element_name)

    def my_element_ends(self,):
        self.path.pop()

    def root_entry_ends(self,):
        #pprint(self.content)
        #a=1/0

        self.root_counter += 1
        if self.root_counter % 1000 == 0:
            print ('ClinVarSet entities parsed:', self.root_counter)
        self.test_1(self.content)

        self.content = {}
        self.path = []

    def ReferenceClinVarAssertion_starts(self, attrs):

        self.current = self.content
        for x in self.path:
            self.current = self.current[x]
        
        if not 'ReferenceClinVarAssertion' in self.current:
            self.current['ReferenceClinVarAssertion'] = []

        self.current['ReferenceClinVarAssertion'].append({
            '##': 'ReferenceClinVarAssertion',
            'attrs': attrs,
        })

        self.path.append('ReferenceClinVarAssertion')


    def ReferenceClinVarAssertion_ends(self,):
        self.path.pop()


    def startElement(self, tag, attributes):

        ## TODO FIXME AAAAAAAA THIS HAS VALUABLE INFORMAITON THAT WE DISCARD!
        if tag == 'ReleaseSet':
            return 

        attrs = dict(attributes)

#        if tag in ['ClinVarSet', 'ReferenceClinVarAssertion']:
#            self.my_element_starts(tag, attrs)

        self.my_element_starts(tag, attrs)

#        if tag == 'ClinVarSet':
#            self.ClinVarSet_starts(attrs)
#        elif tag == 'ReferenceClinVarAssertion':
#            self.ReferenceClinVarAssertion_starts(attrs)


    # Call when an elements ends
    def endElement(self, tag):

        if tag == 'ReleaseSet':
            return

#        if tag in ['ClinVarSet', 'ReferenceClinVarAssertion']:
#            self.my_element_ends()
        
        self.my_element_ends()

        if tag == 'ClinVarSet':
            self.root_entry_ends()

#        if tag == 'ClinVarSet':
#            self.ClinVarSet_ends()
#
#        elif tag == 'ReferenceClinVarAssertion':
#            self.ReferenceClinVarAssertion_ends()

    def characters(self, content):
        current = self.content
        for x in self.path:
            current = current[x]


        if content.strip():

            current_text = ''
            if 'TEXT' in current['elements'][-1]:
                current_text = current['elements'][-1]['TEXT']

            current['elements'][-1]['TEXT'] = current_text + content.strip()


if __name__ == '__main__':
    filename = '/home/maryastr/clinVar/clinVarCode/ClinVarFullRelease_2018-07.xml'
    parser = xml.sax.make_parser()
    Handler = ClinVarHandler()

    parser.setContentHandler( Handler )

    parser.parse(filename)

