

class Run(object):
    def __init__(self,alias,sample_id,run_file_type_id,experiment_id,files,id):
        self.alias = alias
        self.sample_id = sample_id
        self.run_file_type_id = run_file_type_id
        self.experiment_id = experiment_id
        self.files = files
        self.id = id

        
    def to_dict(self):
        return {
            'alias' : self.alias,
            'sampleId' : self.sample_id,
            'runFileTypeId' : self.run_file_type_id,
            'experimentId' : self.experiment_id,
            'files' : map(lambda file: file.to_dict(), self.files),
            'id' : self.id
            }


    def to_xml(self):
        pass