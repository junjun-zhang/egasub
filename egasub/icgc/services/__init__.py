import requests
import json

ICGC_ID_SERVICE_URL_TEST = "http://hetl2-dcc.res.oicr.on.ca:8000"
ICGC_ID_SERVICE_URL_PROD = "http://hetl2-dcc.res.oicr.on.ca:8000"

ICGC_ID_SERVICE_ENDPOINTS = {
    "id": {
        "donor": {
            "path": "/donor/id",
            "params": ["submittedProjectId", "submittedDonorId"]
        },
        "specimen": {
            "path": "/specimen/id",
            "params": ["submittedProjectId", "submittedSpecimenId"]
        },
        "sample": {
            "path": "/sample/id",
            "params": ["submittedProjectId", "submittedSampleId"]
        }
    }
}


def id_service(ctx, type_, project_code, submitter_id, create=True, is_test=False):
    """
    ICGC ID Service
    """
    if not type_ in ('donor', 'specimen', 'sample'):
        raise Exception('Unsupported entity type: %s' % type_)

    url = ICGC_ID_SERVICE_URL_TEST if is_test else ICGC_ID_SERVICE_URL_PROD
    path = ICGC_ID_SERVICE_ENDPOINTS['id'][type_]['path']
    project_param = '='.join([
                                ICGC_ID_SERVICE_ENDPOINTS['id'][type_]['params'][0],
                                project_code
                            ])
    submitter_id_param = '='.join([
                                    ICGC_ID_SERVICE_ENDPOINTS['id'][type_]['params'][1],
                                    submitter_id
                                ])
    create_param = '='.join(['create', 'true' if create else 'false'])


    r = requests.get("%s/%s?%s&%s&%s" % (url, path, project_param,
                                            submitter_id_param, create_param),
                       headers={
                                'Content-Type': 'application/json',
                                'Authorization': 'Bearer %s' % ctx.obj['SETTINGS'].get('icgc_id_service_token')
                                }
                    )
    
    return r.text

    # TODO: parse response

