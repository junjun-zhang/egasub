from egasub.submission.submit import submittable_status, submit_dataset, perform_submission
from egasub.ega.entities.ega_enums import EgaEnums
import pytest
import os

def test_submittable_status():
    assert submittable_status("fail") == None
    assert submittable_status("tests/submission/test_submit.py") == ['']

def test_submit_dataset(ctx, mock_server):
    with pytest.raises(AttributeError):
        submit_dataset(ctx)

    ctx.obj['SETTINGS']['ega_submitter_account'] = 'test_account'
    ctx.obj['SETTINGS']['ega_submitter_password'] = 'test_password'
    ctx.obj['SETTINGS']['ega_policy_id'] = 'test_id'
    ctx.obj['CURRENT_DIR'] = os.path.join(os.getcwd(), 'tests/data/workspace/variation.20170119')
    ctx.obj['EGA_ENUMS'] = EgaEnums()
    #ctx.obj['EGA_ENUMS']['_enums'] = ''
    with pytest.raises(AttributeError):
        submit_dataset(ctx)




def test_perform_submission(ctx, mock_server):
    perform_submission(ctx, '///')

    ctx.obj['SETTINGS']['ega_submitter_account'] = None
    ctx.obj['SETTINGS']['ega_submitter_password'] = None



