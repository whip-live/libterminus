from functools import reduce


class Pipeline:
    """
    Class to build and run our pipeline
    """
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        """
        Add a step to steps list
        """
        self.steps.append(step)

    def plumber(self, func):
        """
        Concatenate steps

        Assuming that we have a foo_list = [foo(), bar()]
        What plumber function does with this list is:
         - bar(foo())

        This solution is taken from
        http://stackoverflow.com/questions/38755702/pythonic-way-to-chain-python-generator-function-to-form-a-pipeline
        """
        return lambda x: reduce(lambda f, g: g(f), func, x)

    def run(self, data=None):
        """
        Data are processed through pipeline steps
        """
        chain = self.plumber(self.steps)
        return chain(data)
