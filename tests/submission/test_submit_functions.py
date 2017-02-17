import os, yaml
from egasub.ega.services import login,logout,prepare_submission, object_submission, query_by_id, api_url, query_by_type, delete_obj, _obj_type_to_endpoint
import pytest
import requests
from egasub.ega.entities.submission_subset_data import SubmissionSubsetData
from egasub.ega.entities.submission import Submission
from egasub.ega.entities.study import Study
from egasub.exceptions import CredentialsError
from egasub.ega.entities.sample import Sample
from egasub.ega.entities.dataset import Dataset
from egasub.ega.entities.policy import Policy


def test_login_function(ctx, mock_server):
    with pytest.raises(CredentialsError):
        login(ctx)

    ctx.obj['SETTINGS']['ega_submitter_account'] = 'test_account'

    with pytest.raises(CredentialsError):
        login(ctx)
        
    ctx.obj['SETTINGS']['ega_submitter_password'] = 'test_password'
    
    login(ctx)
    assert not ctx.obj['SUBMISSION']['sessionToken'] == None
    assert ctx.obj['SUBMISSION']['sessionToken'] == "abcdefg"

def test_prepare_submission(ctx):
    response = requests.post("%ssubmissions" % (ctx.obj['SETTINGS']['apiUrl']))
    
    subset = SubmissionSubsetData([2,3],[5,2],[4,34],[54,1],[88,7],[1,3],[44,11],[2,11])
    submission = Submission('a title', 'a description', subset)
    
    prepare_submission(ctx,submission)
    assert ctx.obj['SUBMISSION']['id'] == "12345"
    
def test_api_url(ctx):
    assert api_url(ctx) == "http://example.com/"
    del ctx.obj['SETTINGS']['apiUrl']
    assert api_url(ctx) == "https://ega.crg.eu/submitterportal/v1/"
    ctx.obj['SETTINGS']['apiUrl'] = "http://example.com/"
        
def test_object_submission(ctx,mock_server):
    sample = Sample('alias','title','description','case_or_control','gender','organism_part','cell_line','region','phenotype','subject_id','anonymized_name','bio_sample_id','sample_age',
                    'sample_detail',[],'id',None)
    
    study = Study('test_alias','study_type_id','short_name','title','study_abstract','own_term','pub_med_ids',[],'id')
        
    policy = Policy('policy_alias','dac_id','title','policy_text','url')
        
def test_query_by_id(ctx, mock_server):
    result = query_by_id(ctx,'sample','sample_alias','ALIAS')
    assert result[0].get('id') == '12345'
    
    result = query_by_id(ctx,'study','test_alias','ALIAS')
    assert result[0].get('id') == '12345'
    
    result = query_by_id(ctx,'dataset','dataset_alias','ALIAS')
    assert result[0].get('id') == '12345'
    
    result = query_by_id(ctx,'policy','policy_alias','ALIAS')
    assert result[0].get('id') == '12345'
    
def test_query_by_type(ctx, mock_server):
    result = query_by_type(ctx, 'sample', "SUBMITTED")
    assert result[0].get('id') == '12345'
    
    result = query_by_type(ctx, 'study', "SUBMITTED")
    assert result[0].get('id') == '12345'
    
    result = query_by_type(ctx, 'dataset', "SUBMITTED")
    assert result[0].get('id') == '12345'
    
    result = query_by_type(ctx, 'policy', "SUBMITTED")
    assert result[0].get('id') == '12345'
    
def test_obj_type_to_endpoint():
    _obj_type_to_endpoint("dataset") == "datasets"
    _obj_type_to_endpoint("sample") == "samples"
    _obj_type_to_endpoint("policy") == "policies"
    
    with pytest.raises(Exception):
        _obj_type_to_endpoint("test")

def test_logout_function(ctx):
    logout(ctx)
    
    with pytest.raises(KeyError):
        logout(ctx)
        
    assert not 'sessionToken' in ctx.obj['SUBMISSION']