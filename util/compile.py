#!/usr/bin/env python3
import os
file_dir = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(file_dir, "template")
project_dir = os.path.join(file_dir, "../")
readme_dir = os.path.join(project_dir, "README.md")
problems_dir = os.path.join(project_dir, "problems")

def main():
    header = "| Problem | Tags |"
    formatting = "| --- | --- |"
    lines = [header, formatting]

    problems = Problem.get_all()
    for problem in problems:
        formatted_tags = ", ".join(
                ["`{}`".format(tag) for tag in problem.tags()])
        line = "| {} | {} |".format(problem.name, formatted_tags)
        lines += [line]
    table = "\n".join(lines)

    template = ''.join([line for line in open(template_dir)])
    open(readme_dir, "w").write(template.format(table))


class Problem: 
    problems_dir = os.path.join(project_dir, "problems")
    name = ""
    path = ""
    @staticmethod
    def get_all():
        problems = []
        for problem_name in os.listdir(problems_dir):
            problem = Problem(
                    problem_name, 
                    os.path.join(problems_dir, problem_name))
            problems += [problem]
        return problems

    @staticmethod
    def get(name):
        return Problem(name, os.path.join(problems_dir, name))

    def tags(self):
        tag_file = os.path.join(self.path, "tags")
        return [line.strip() for line in open(tag_file) if line.strip()]

    def __init__(self, name, path):
        self.name, self.path = name, path

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Problem {}>".format(self.__str__())

if __name__ == "__main__":
    main()
