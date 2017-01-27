import os
import click
from click.testing import CliRunner
from egasub.cli import init
from egasub.cli import main
import yaml

def test_init_function():    
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main,['init','--ega_submitter_account','test_account','--ega_submitter_password','test_password','--icgc_id_service_token','test_token','--icgc_project_code','test_code'])
        assert not result.exception
        assert os.path.isdir('.egasub')
        assert os.path.isdir('.egasub/policy')
        assert os.path.exists('.egasub/policy/ICGC_Policy.xml')
        
        yaml_config_file = '.egasub/config.yaml'
        assert os.path.exists(yaml_config_file)
        
        yaml_config = yaml.load(file(yaml_config_file,'r'))
        assert yaml_config['ega_submitter_account'] == "test_account"
        assert yaml_config['ega_submitter_password'] == "test_password"
        assert yaml_config['icgc_id_service_token'] == "test_token"
        assert yaml_config['icgc_project_code'] == "test_code"