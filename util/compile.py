#!/usr/bin/env python3
import os
import yaml
file_dir = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(file_dir, "template")
project_dir = os.path.join(file_dir, "../")
readme_dir = os.path.join(project_dir, "README.md")
problems_dir = os.path.join(project_dir, "problems")
def main():
    header = "|Platform | Problem | Tags | Difficulty | URL |"
    formatting = "| --- | --- | --- | --- | --- |"
    lines = [header, formatting]

    problems = Problem.get_all()
    for problem in problems:
        formatted_tags = ", ".join(
                ["`{}`".format(tag) for tag in problem.tags()])
        line = "| {} | {} | {} | {} | {} |".format(
                problem.platform(), 
                problem.name(), 
                formatted_tags, 
                problem.difficulty(),
                problem.url())
        lines += [line]
    table = "\n".join(lines)

    template = ''.join([line for line in open(template_dir)])
    open(readme_dir, "w").write(template.format(table))


class Problem: 
    path = ""
    meta = None

    @staticmethod
    def get_all():
        problems = []
        for problem_name in os.listdir(problems_dir):
            problem = Problem(os.path.join(problems_dir, problem_name))
            problems += [problem]
        return problems

    @staticmethod
    def get(name):
        return Problem(os.path.join(problems_dir, name))

    def name(self):
        return self.meta.get("name")

    def tags(self):
        return self.meta.get("public_tags") + self.meta.get("private_tags")

    def platform(self):
        return self.meta.get("platform")

    def difficulty(self):
        return self.meta.get("difficulty")

    def url(self):
        return self.meta.get("url")

    def __init__(self, path):
        self.path = path
        with open(os.path.join(self.path, "meta.yml")) as f:
            self.meta = yaml.safe_load(f)

    def __str__(self):
        return self.name()

    def __repr__(self):
        return "<Problem {}>".format(self.__str__())


if __name__ == "__main__":
    main()
