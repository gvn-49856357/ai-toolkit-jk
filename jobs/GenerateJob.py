from jobs import BaseJob
from collections import OrderedDict
from typing import List
from jobs.process import GenerateProcess
from toolkit.paths import REPOS_ROOT

import sys

sys.path.append(REPOS_ROOT)

process_dict = {
    'to_folder': 'GenerateProcess',
}


class GenerateJob(BaseJob):
    process: List[GenerateProcess]

    def __init__(self, config: OrderedDict):
        super().__init__(config)
        self.device = self.get_conf('device', 'cpu')

        # loads the processes from the config
        self.load_processes(process_dict)

    def run(self):
        super().run()
        print("")
        print(f"Running  {len(self.process)} process{'' if len(self.process) == 1 else 'es'}")

        for process in self.process:
            process.run()
