
#import asyncio
import json
import xml.sax
import gzip


def pprint(d):
    print (json.dumps(d, indent=4))
        


class ClinVarHandler( xml.sax.ContentHandler ):
    def __init__(self, ):
        self.content = {}
        self.path = []
        self.root_counter = 0

    def build_url(self, entry):
        Acc =  entry['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['ClinVarAccession'][0]['attrs']['Acc']

        url_format = 'https://www.ncbi.nlm.nih.gov/clinvar/{Acc}/'

        return url_format.format(Acc=Acc)

    def build_variation_url(self, entry=None):

        if entry is None:
            entry = self.content

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

    ### PROCESS CONTENET 
    def process_content(self, ):
        #print (self.content)
        #print (json.dumps(self.content, indent=4))

        assert (len(self.content)) == 1
        assert len(self.content['ClinVarSet'][0]['ReferenceClinVarAssertion']) == 1
        ReferenceClinVarAssertion = self.content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]

        assert len(ReferenceClinVarAssertion['MeasureSet']) == 1

        if not 'SequenceLocation' in ReferenceClinVarAssertion['MeasureSet'][0]['Measure'][0]:
            #print ('Not sequence location found. Return')
            return

        SequenceLocations = ReferenceClinVarAssertion['MeasureSet'][0]['Measure'][0]['SequenceLocation']
        normal_locations = []
        for SequenceLocation in SequenceLocations:
            attrs = SequenceLocation['attrs']
            if 'outerStart' in attrs and 'innerStart' in attrs and 'innerStop' in attrs and 'outerStop' in attrs:
                continue

            if not 'variantLength' in attrs:
                continue
            
            normal_locations.append(attrs)

        if not normal_locations:
            #print ('Not found normal location. Return')
            return

        length_ones = []

        for normal_location in normal_locations:
            if normal_location['variantLength'] == '1':
                #print (self.build_variation_url(self.content))
                length_ones.append(normal_location)

        if not length_ones:
            #print ('Could not find a variant of length one. Return')
            return

        length_one_grch47 = 0
        for length_one in length_ones:
            if length_one['Assembly'] != 'GRCh37':
                continue

            length_one_grch47 += 1

            if not 'positionVCF' in length_one:
                assert len(set([length_one['start'], length_one['stop'], length_one['display_start'], length_one['display_stop']])) == 1
                position_vcf = length_one['start']
            else:
                position_vcf = length_one['positionVCF']
            chromosome = length_one['Chr']

            reference = length_one.get('referenceAlleleVCF', 'UNKNOWN')
            alternative = length_one.get('alternateAlleleVCF', 'UNKNOWN')

        if length_one_grch47 == 0:
            #print ('Could not find in GRCh37. Return')
            return

        assert length_one_grch47 == 1
        #print (json.dumps(self.content, indent=4))
        #a=1/0

        assert len(ReferenceClinVarAssertion['ClinicalSignificance']) == 1
        assert len(ReferenceClinVarAssertion['ClinicalSignificance'][0]['ReviewStatus']) == 1
        ReviewStatus_0 = ReferenceClinVarAssertion['ClinicalSignificance'][0]['ReviewStatus'][0]['TEXT']

        #print (self.build_variation_url(self.content))

        ClinVarAssertion = self.content['ClinVarSet'][0]['ClinVarAssertion']
        assert len(ClinVarAssertion) == 1
        assert len(ClinVarAssertion[0]['ClinicalSignificance']) == 1
        assert len(ClinVarAssertion[0]['ClinicalSignificance'][0]['Description']) == 1
        Clinical_significance = ClinVarAssertion[0]['ClinicalSignificance'][0]['Description'][0]['TEXT']

        if not 'DateLastEvaluated' in ClinVarAssertion[0]['ClinicalSignificance'][0]['attrs']:
            #print (self.build_variation_url(self.content))
            #print (json.dumps(ClinVarAssertion[0]['ClinicalSignificance'], indent=4))
            #a=1/0
            DateLastEvaluated = 'Not provided'
        else:
            DateLastEvaluated = ClinVarAssertion[0]['ClinicalSignificance'][0]['attrs']['DateLastEvaluated']

        assert len(ClinVarAssertion[0]['ClinicalSignificance'][0]['ReviewStatus']) == 1
        review_status = ClinVarAssertion[0]['ClinicalSignificance'][0]['ReviewStatus'][0]['TEXT']

        if len(ClinVarAssertion[0]['ObservedIn']) != 1:
            print (len(ClinVarAssertion[0]['ObservedIn']))
            pprint(ClinVarAssertion[0]['ObservedIn'])
            print (self.build_variation_url())
            a=1/0

        assert len(ClinVarAssertion[0]['ObservedIn']) == 1
        assert len(ClinVarAssertion[0]['ObservedIn'][0]['Method']) == 1
        assert len(ClinVarAssertion[0]['ObservedIn'][0]['Method'][0]['MethodType']) == 1
        collection_method = ClinVarAssertion[0]['ObservedIn'][0]['Method'][0]['MethodType'][0]['TEXT']

        pubmed_ids = set()
        for ObservedData in ClinVarAssertion[0]['ObservedIn'][0]['ObservedData']:

            if not 'Citation' in ObservedData:
                #print (json.dumps(ObservedData, indent=4))
                #print (self.build_variation_url(self.content))
                #a=1/0
                continue

            for citation in ObservedData['Citation']:

                if not 'ID' in citation:
                    # Paper of 1966... 
                    # https://www.ncbi.nlm.nih.gov/clinvar/variation/5007/
                    continue

                assert len(citation['ID']) == 1
                if citation['ID'][0]['attrs']['Source'] != 'PubMed':
                    continue
                pubmed = citation['ID'][0]['TEXT']
                pubmed_ids.add(pubmed)

        assert len(ClinVarAssertion[0]['ObservedIn'][0]['Sample']) == 1
        assert len(ClinVarAssertion[0]['ObservedIn'][0]['Sample'][0]['Origin']) == 1
        origin = ClinVarAssertion[0]['ObservedIn'][0]['Sample'][0]['Origin'][0]['TEXT']

        assert len(ClinVarAssertion[0]['TraitSet']) == 1
        assert len(ClinVarAssertion[0]['TraitSet'][0]['Trait']) > 0
        conditions = []
        for trait in ClinVarAssertion[0]['TraitSet'][0]['Trait']:
            if not 'Name' in trait:
                #print (json.dumps(ClinVarAssertion[0]['TraitSet'], indent=4))
                #print (json.dumps(ClinVarAssertion[0]['TraitSet'][0]['Trait'], indent=4))
                #print (json.dumps(ClinVarAssertion, indent=4))
                #print (json.dumps(self.content, indent=4))
                #print (self.build_variation_url(self.content))
                #a=1/0

                #Access the MeasureSet from ReferenceClinVarAssertion
                assert len(ReferenceClinVarAssertion['TraitSet']) == 1
                assert len(ReferenceClinVarAssertion['TraitSet'][0]['Trait']) == 1
                assert len(ReferenceClinVarAssertion['TraitSet'][0]['Trait'][0]['Name']) == 1
                assert len(ReferenceClinVarAssertion['TraitSet'][0]['Trait'][0]['Name'][0]['ElementValue']) == 1
                Condition = ReferenceClinVarAssertion['TraitSet'][0]['Trait'][0]['Name'][0]['ElementValue'][0]['TEXT']

                if 'XRef' in ReferenceClinVarAssertion['TraitSet'][0]['Trait'][0]:
                    Condition += '[' + '|'.join(['{}({})'.format(XRef['attrs']['DB'], XRef['attrs']['ID']) for XRef in ReferenceClinVarAssertion['TraitSet'][0]['Trait'][0]['XRef']]) + ']'


            else:
                assert len(trait['Name']) == 1
                assert len(trait['Name'][0]['ElementValue']) == 1
                Condition = trait['Name'][0]['ElementValue'][0]['TEXT']

                if 'XRef' in trait:
                    Condition += '[' + '|'.join(['{}({})'.format(XRef['attrs']['DB'], XRef['attrs']['ID']) for XRef in trait['XRef']]) + ']'


            conditions.append(Condition)

        Condition = '|'.join(conditions)

        assert len(ClinVarAssertion[0]['ClinVarSubmissionID']) == 1
        submitter = ClinVarAssertion[0]['ClinVarSubmissionID'][0]['attrs']['submitter']

        assert len(ClinVarAssertion[0]['ClinVarAccession']) == 1
        ClinVarAccession = ClinVarAssertion[0]['ClinVarAccession'][0]['attrs']['Acc']
        ClinVarAccession_version = ClinVarAssertion[0]['ClinVarAccession'][0]['attrs']['Version']
        submission_accession = '{}.{}'.format(ClinVarAccession, ClinVarAccession_version)

        #print (json.dumps(ClinVarAssertion[0], indent=4))
        #print (ClinVarAssertion[0]['ClinicalSignificance'][0])

        stars = {
            'no assertion criteria provided': 0,
            'no assertion provided': 0,
            'no assertion for the individual variant': 0,
            'criteria provided, single submitter': 1,
            'criteria provided, conflicting interpretations': 1,
            'criteria provided, multiple submitters, no conflicts': 2,
            'reviewed by expert panel': 3,
            'practice guideline': 4,
        }
        stars_given = stars[ReviewStatus_0]


        # THESE ARE SIGNIGIFICANT FIELDS
        if False:
            print (Clinical_significance)
            print (DateLastEvaluated)
            print (review_status)
            print (collection_method)
            print (Condition)
            print (origin)
            print (pubmed_ids)
            print (submitter)
            print (submission_accession)
            print (ReviewStatus_0) # Convert to star
            print (stars_given)


        # https://www.ncbi.nlm.nih.gov/clinvar/docs/review_status/


        

        #END OF SIGNIFICANT FIELDS

        self.report(
            position_vcf = position_vcf,
            chromosome = chromosome,
            reference = reference,
            alternative = alternative,
            stars_given = stars_given,


        )

        #a=1/0

            #print (self.build_variation_url(self.content))
#            print (normal_location['variantLength'])

        #a=1/0


        #print (json.dumps(SequenceLocation, indent=4))

        #a=1/0

    def report(self, position_vcf, chromosome, reference, alternative, stars_given):
        print (chromosome, position_vcf, reference, alternative, stars_given)


    ### END OF PROCESS CONTENT

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

        self.process_content()

        
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

    #filename = '/home/maryastr/clinVar/clinVarCode/ClinVarFullRelease_2018-07.xml'
    filename = '/Users/antonakd/alekos/Astrinaki/ClinVarFullRelease_2018-07.xml.gz'
    file_gz = gzip.open(filename)
    parser = xml.sax.make_parser()
    Handler = ClinVarHandler()

    parser.setContentHandler( Handler )

    #parser.parse(filename)
    parser.parse(file_gz)
    file_gz.close()

