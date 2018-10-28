#import asyncio
import json
import xml.sax
import itertools



def pprint(ofile,d):
#def pprint(d):


    #print (json.dumps(d, indent=4))
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
    chromosome=[]
    assembly=[]
    variantLength=[]
    v_type=[]
    n_change=[]
    prefered_name=[]
    condition=[]
    identifier=[]
    globalalleleFreq=[]
    GO_ESP=[]
    proteinChange=[]
    skata=[]
    skatoules=[]
    MolecularConsequence=[]
    f_consequence=[]
    pos=[]
    links=[]
    citation=[]
    Frequencies=[]
    
    ofile = open('euterpi.json','w')




    '''
    Do whatever you want
    '''

    while True:
        try:
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
            chromosome=[]
            assembly=[]
            variantLength=[]
            v_type=[]
            n_change=[]
            prefered_name=[]
            condition=[]
            identifier=[]
            globalalleleFreq=[]
            GO_ESP=[]
            proteinChange=[]
            skata=[]
            skatoules=[]
            MolecularConsequence=[]
            f_consequence=[]
            pos=[]
            links=[]
            citation=[]
            Frequencies=[]
        #recordList=[]
            content = (yield)

#NOT all sequence location https://www.ncbi.nlm.nih.gov/clinvar/RCV000001859/
#Not all HGVS https://www.ncbi.nlm.nih.gov/clinvar/RCV000003355/

            if "TraitSet" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]:

                for x in range(len( content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["TraitSet"][0]["Trait"])):

                    if "XRef" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["TraitSet"][0]["Trait"][x]:

                        for l in range(len(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["TraitSet"][0]["Trait"][x]["XRef"])):

                            identifier.append({"DB":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["TraitSet"][0]["Trait"][x]["XRef"][l]["attrs"]["DB"],"ID":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["TraitSet"][0]["Trait"][x]["XRef"][l]["attrs"]["ID"]})

                for x in range(len( content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["TraitSet"][0]["Trait"])):
                    condition.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["TraitSet"][0]["Trait"][x]["Name"][0]["ElementValue"][0]["TEXT"])
                    
            elif "TraitSet" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]:

                condition.append("Nan")
                identifier.append("Nan")

            if "MeasureSet" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]:

                if "ObservedIn" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]:
                    if "ObservedData" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["ObservedIn"][0]:
                        if "Citation" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["ObservedIn"][0]["ObservedData"][0]:
                            for z in range(len(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["ObservedIn"][0]["ObservedData"][0]["Citation"])):
                                if "ID" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["ObservedIn"][0]["ObservedData"][0]["Citation"][z]:
                                    citation.append({"source":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["ObservedIn"][0]["ObservedData"][0]["Citation"][z]["ID"][0]['attrs']['Source'],"id":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]["ObservedIn"][0]["ObservedData"][0]["Citation"][z]["ID"][0]['TEXT']})
                
                elif  "ObservedIn" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]:
                    citation.append("nan")

                if "Name" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]:
                    prefered_name.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]["Name"][0]["ElementValue"][0]["TEXT"])
                elif  "Name" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]:
                    prefered_name.append("Nan")



                if "SequenceLocation" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]:
                    


                    for i in range(len(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'])):
                        chromosome.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['Chr'])

                        assembly.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['Assembly'])

                        if "variantLength" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                            variantLength.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['variantLength'])
                        elif "variantLength" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                            variantLength.append("Nan")

                        if "outerStart" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                            outerstart.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['outerStart'])
                        elif "outerStart" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                            outerstart.append("Nan")

                        if "outerStop" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                            outerstop.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['outerStop'])
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
                        if "start" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                            start.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['start'])
                        elif "start" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                            start.append('Nan')
                        if "stop" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                            stop.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['stop'])
                        elif "stop" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                            stop.append('Nan')
                        if "strand" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                            strand.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']['strand'])
                        elif "strand" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][i]['attrs']:
                            strand.append("Nan")
                elif  "SequenceLocation" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]:
                    innerstart.append("Nan")
                    innerstop.append("Nan")
                    displaystart.append("Nan")
                    displaystop.append("Nan")
                    start.append("Nan")
                    stop.append("Nan")
                    strand.append("Nan")
                    assembly.append("Nan")
                    chromosome.append("Nan")
                    variantLength.append("Nan")

                if "XRef" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]:
                    for d in range(len(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]["XRef"])):
                        if "ID" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]["XRef"][d]["attrs"]:
                            links.append({"ID":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]["XRef"][d]["attrs"]["ID"], "DB":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]["XRef"][d]["attrs"]["DB"]})
                            
                if "AttributeSet" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]:

                    for i in range(len( content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'])):
                        if "HGVS" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['attrs']['Type']:
                            HGVS.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['TEXT'])
                
                        if "GlobalMinorAlleleFrequency" == content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['attrs']['Type']:
                            globalalleleFreq.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['TEXT'])
                        if 'AlleleFrequency' in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['attrs']['Type']:
                            if 'XRef' in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]:
                                for bases in range(len(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['XRef'])):
                                    Frequencies.append({"frequency":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['TEXT'],"Bases":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['XRef'][bases]['attrs']['DB']})
                        #if "AlleleFrequency"== content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['attrs']['Type']:
                         #   GO_ESP.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['TEXT'])
                        if "ProteinChange" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]["attrs"]["Type"]:
                            proteinChange.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]["TEXT"])
                       
                           

                        if "MolecularConsequence" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['attrs']['Type']:
                        #if "regulatory region ablation"  not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][x]['Attribute'][0]['TEXT']:

                            pos.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['TEXT'])
                            if "XRef" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]:
                                for z,l in enumerate(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['XRef']):
                                    if "RefSeq" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['XRef'][z]['attrs']['DB']:
                                    
                                        skata.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['XRef'][z]['attrs']['ID'])
                                 
                                    if "Sequence Ontology"  in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['XRef'][z]['attrs']['DB']:
                                        skatoules.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['XRef'][z]['attrs']['ID'])
                                    
                                    elif "RefSeq" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['XRef'][z]['attrs']['DB']:
                                        skata.append(" ")
                                    
                                    elif "Sequence Ontology"  not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['XRef'][z]['attrs']['DB']:
                                        skatoules.append(" ")

                            elif "XRef" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]:
                                  
                                    skata.append(" ")
                                    skatoules.append(" ") 
                                    
                        elif "MolecularConsequence" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['attrs']['Type']:
                            MolecularConsequence.append(" ")  
                
                    if len(pos)>0:
                        for k in range(len(pos)):
          



                            MolecularConsequence.append(skata[k] +" "+pos[k]+" "+skatoules[k])
                    elif len(pos)==0:
                        MolecularConsequence.append("nan")

                   


                    if "FunctionalConsequence" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][0]['Attribute'][0]['attrs']['Type']:
                        f_consequence.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][0]['Attribute'][0]['TEXT']) 
                   

                    if "nucleotide change" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['attrs']['Type']:
                        n_change.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['TEXT'])

                    elif "nucleotide change" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['AttributeSet'][i]['Attribute'][0]['attrs']['Type']:
                        n_change.append("Nan")
                elif "AttributeSet" not  in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]:
                    HGVS.append("Nan")
                    globalalleleFreq.append("nan")
                    #GO_ESP.append("nan")
                    proteinChange.append("nan")
                    MolecularConsequence.append("nan")
                    f_consequence.append("nan")
                    n_change.append("Nan")
                    Frequencies.append("Nan")
                    


        
                if "CytogeneticLocation" in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]:
                    Cytogenic_Loc.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]["CytogeneticLocation"][0]["TEXT"])
                elif "CytogeneticLocation" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]:
                    Cytogenic_Loc.append("Nan")

                

                for i in range(len(content['ClinVarSet'][0]['ClinVarAssertion']) ):
                    submitter.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinVarSubmissionID'][0]['attrs']['submitter'])
                    if "submitterDate" in content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinVarSubmissionID'][0]['attrs']:
                        submitterDate.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinVarSubmissionID'][0]['attrs']['submitterDate'])
                    elif "submitterDate" not in content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinVarSubmissionID'][0]['attrs']:
                        submitterDate.append("nan")

                    Acc.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinVarAccession'][0]['attrs']['Acc'])
                    Assertion_RecordStatus.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['RecordStatus'][0]['TEXT'])
                    if "DateLastEvaluated" in content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinicalSignificance'][0]['attrs']:
                        DateEvaluated.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinicalSignificance'][0]['attrs']['DateLastEvaluated'])
                    elif "DateLastEvaluated" not in content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinicalSignificance'][0]['attrs']:
                        DateEvaluated.append('Nan')
                    AssertionReviewStatus.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinicalSignificance'][0]['ReviewStatus'][0]['TEXT'])
                    if "Description" in content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinicalSignificance'][0]:
                        AssertionDescription.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinicalSignificance'][0]['Description'][0]['TEXT'])
                    elif "Description" not in content['ClinVarSet'][0]['ClinVarAssertion'][i]['ClinicalSignificance'][0]:
                        AssertionDescription.append("nan")
                    origin.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]['ObservedIn'][0]['Sample'][0]['Origin'][0]['TEXT'])
                    AssertionMethod.append(content['ClinVarSet'][0]['ClinVarAssertion'][0]['ObservedIn'][0]['Method'][0]['MethodType'][0]['TEXT'])

                    if "Assertion" in content['ClinVarSet'][0]['ClinVarAssertion'][i]:

                        assertion.append(content['ClinVarSet'][0]['ClinVarAssertion'][i]["Assertion"][0]["attrs"]["Type"])

                    elif "Assertion" not in content['ClinVarSet'][0]['ClinVarAssertion'][i]:
                        assertion.append("nan")

                v_type.append(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['attrs']['Type'])


            elif "MeasureSet" not in content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]:
                v_type.append("Nan")
                Cytogenic_Loc.append("Nan")
                HGVS.append("Nan")
                chromosome.append("nan")
                assembly.append("nan")
                variantLength.append("nan")
                innerstart.append("Nan")
                innerstop.append("Nan")
                displaystart.append("Nan")
                displaystop.append("Nan")
                start.append("Nan")
                stop.append("Nan")
                strand.append("Nan")
                assembly.append("Nan")
                chromosome.append("Nan")
                variantLength.append("Nan")

            if "Citation" in content['ClinVarSet'][0]['ClinVarAssertion'][0]:

                if "ID" in content['ClinVarSet'][0]['ClinVarAssertion'][0]['Citation'][0]:
                    citation.append({"source":content['ClinVarSet'][0]['ClinVarAssertion'][0]['Citation'][0]['ID'][0]['attrs']['Source'],"id":content['ClinVarSet'][0]['ClinVarAssertion'][0]['Citation'][0]['ID'][0]['TEXT']})

            





        
        #pprint(content['ClinVarSet'][0]['ClinVarAssertion'][0]['ClinVarSubmissionID'][0]['attrs']['submitterDate'])
        #pprint(content['ClinVarSet'][0]['ClinVarAssertion'][0]['ClinVarAccession'][0]['attrs']['Acc'])
        #pprint(content['ClinVarSet'][0]['ClinVarAssertion'][0]['RecordStatus'][0]['TEXT'])

  

       
            if " " in MolecularConsequence:
                MolecularConsequence=list((filter(str.strip, MolecularConsequence)))
                

            recordList.append({"ClinVar Id":content['ClinVarSet'][0]['attrs']['ID'],"Record status":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['RecordStatus'][0]['TEXT'],"Title":content['ClinVarSet'][0]['Title'][0]['TEXT'],"Review status":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['ClinicalSignificance'][0]['ReviewStatus'][0]['TEXT'],"clinical significance":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['ClinicalSignificance'][0]['Description'][0]['TEXT'],"Accession":content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['ClinVarAccession'][0]['attrs']['Acc'],"variant type":v_type,

                "Assembly":assembly,"chr":chromosome,"outerstart": outerstart,"innerstart":innerstart,
                "innerstop":innerstop,"outerstop":outerstop,"displaystart":displaystart,"displaystop":displaystop,"start":start,"stop":stop,"variantLength":variantLength,
                "strand":strand,"prefered name":prefered_name,"HGVS":HGVS,"Links":links,"Cytogenetic Location":Cytogenic_Loc,"nucleotide change":n_change,"Protein Change":proteinChange,"condition(s)":condition,"Identifier":identifier,"Molecular Consequence":MolecularConsequence,
                "Functional Consequence":f_consequence,"Global Allele Freguency ":globalalleleFreq,"Frequencies":Frequencies,"submitter(assertion)":submitter,"submission date(assertion)":submitterDate,"record status(assertion)":Assertion_RecordStatus,'Date Last Evaluate(assertion)':DateEvaluated,'review status(assertion)':AssertionReviewStatus,'Description(Assertion)':AssertionDescription,"Origin(Assertion)":origin,"Method(Assertion)":AssertionMethod,"Assertion":assertion,"citation":citation

                })

            

           
            



            
            
            
            #pprint(recordList)
            #print(links)

            #pprint (content)

     

        
    #pprint(recordList)


    

     


        #xrec = recordList.copy()
    #return recordList
        except GeneratorExit:
        #finally:
            pprint(ofile, recordList)




      #  pprint(content['ClinVarSet'][0]['ReferenceClinVarAssertion'][0]['MeasureSet'][0]['Measure'][0]['SequenceLocation'][0]['attrs']['Strand'])

      

      

    
        
        



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

    filename = '/home/maryastr/clinVar/clinVarCode/final/ClinVarFullRelease_2018-07.xml'
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
