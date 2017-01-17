import pytest
from sample import Sample
from attribute import Attribute

attributes = [Attribute('tag1','value1'),Attribute('tag2','value2')]
sample = Sample('the title','the description',123,2,'head','test line','test region','a phenotype',33,'anonymized name',22,10,'some details',attributes)

def test_title():
    assert 'the title' == sample.title
    
def test_description():
    assert 'the description' == sample.description
    
def test_case_or_control_id():
    assert 123 == sample.case_or_control_id
    
def test_gender_id():
    assert 2 == sample.gender_id
    
def test_organism_part():
    assert 'head' == sample.organism_part
    
def test_cell_line():
    assert 'test line' == sample.cell_line
    
def test_region():
    assert 'test region' == sample.region
    
def test_phenotype():
    assert 'a phenotype' == sample.phenotype
    
def test_subject_id():
    assert 33 == sample.subject_id
    
def test_anonymized_name():
    assert 'anonymized name' == sample.anonymized_name
    
def test_biosample_id():
    assert 22 == sample.biosample_id
    
def test_sample_age():
    assert 10 == sample.sample_age
    
def test_sample_detail():
    assert 'some details' == sample.sample_detail
    
def test_attributes():
    assert attributes == sample.attributes
    
def test_to_dict():
        assert cmp(
        {
            'title' : 'the title',
            'description':'the description',
            'caseOrControlId':123,
            'genderId' : 2,
            'organismPart' : 'head',
            'cellLine' : 'test line',
            'region' : 'test region',
            'phenotype' : 'a phenotype',
            'subjectId' : 33,
            'anonymizedName' : 'anonymized name',
            'biosampleId' : 22,
            'sampleAge' : 10,
            'sampleDetail' : 'some details',
            'attributes' : map(lambda attribute: attribute.to_dict(), attributes)
        }, sample.to_dict()) == 0
        
        