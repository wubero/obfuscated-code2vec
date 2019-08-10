import subprocess

class ClassPreprocessor:
    def __init__(self, jar_path, obfuscate):
        self.jar_path = jar_path
        self.obfuscate = obfuscate

    def get_methods(self, file_path):
        command = ['java', '-jar', self.jar_path, file_path, str(self.obfuscate)]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        try:
            return result.stdout.decode('utf-8').split("_METHOD_SPLIT_")
        except:
            print("ERROR DECODING METHODS IN FILE:", file_path)
            return []


# cp = ClassPreprocessor('ClassPreprocess.jar', True)
# for method in cp.get_methods('/Users/rhyscompton/Downloads/java-small/test/hadoop/AppLogAggregatorImpl.java'):
#     print("New method")
#     print(method)
