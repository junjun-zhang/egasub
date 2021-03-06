from egasub.submission.submitter import Submitter
import os
import pytest
from egasub.submission.submittable import Unaligned, Alignment
from egasub.ega.entities.sample import Sample
from egasub.ega.entities.attribute import Attribute

def test_submitter(ctx, mock_server):
    initial_directory = os.getcwd()
    os.chdir('tests/data/workspace/submittable/')
    unaligned = Unaligned('test_u')
    alignment = Alignment('test_a')
    os.chdir(initial_directory)
    os.chdir('tests/data/workspace/unaligned.20170110/')
    ctx.obj['CURRENT_DIR_TYPE'] = 'unaligned'
    unaligned2 = Unaligned('ssample_y')
    os.chdir(initial_directory)


    submitter = Submitter(ctx)


    ctx.obj['SUBMISSION']['sessionToken'] = 'X-Token'
    ctx.obj['SETTINGS']['icgc_project_code'] = "abjdh"
    #ctx.obj['SETTINGS']['ega_study_id'] = "abjdh"
    ctx.obj['SUBMISSION']['id'] = "55"


    assert submitter.submit(unaligned2,True) is None

    #ctx.obj['SETTINGS']['ega_study_id'] = 'asdf'
    assert submitter.submit(unaligned, True) is None
    #ctx.obj['SETTINGS']['ega_study_id'] = None

    ctx.obj['CURRENT_DIR_TYPE'] = 'alignment'
    assert submitter.submit(alignment,True) is None


    attributes = [Attribute('tag1', 'value1'), Attribute('tag2', 'value2')]
    sample = Sample('alias',
                    'the title',
                    'the description',
                    123,
                    2,
                    'head',
                    'test line',
                    'test region',
                    'a phenotype',
                    33,
                    'anonymized name',
                    22,
                    10,
                    'some details',
                    attributes,
                    33)
    with pytest.raises(Exception):
        submitter.set_icgc_ids(sample, False)

    ctx.obj['SETTINGS']['_icgc_sample_id'] = "abjdhf"

    #with pytest.raises(Exception):
    ctx.obj['SETTINGS']['icgc_id_service_token'] = True
    assert submitter.set_icgc_ids(sample, True) is None
    ctx.obj['SETTINGS']['icgc_id_service_token'] = None





