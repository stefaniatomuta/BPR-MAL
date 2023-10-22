from Commands.CommandModel import Command
import re
# finds matches in the csproj of the target frameworks
class FrameworkCommand(Command):
    def execute(self, file_name: str) -> dict:
        patterns = [r'<TargetFramework>(.*?)</TargetFramework>', r'<TargetFrameworkVersion>(.*?)</TargetFrameworkVersion>']
        file_matches = {}
        if file_name.endswith('.csproj'):
            with open(file_name, 'r') as f: #TODO: refactor to only take file and not use os.path.join, it's not necessary to pass the root just for this and helps to avoid extra operations
                code = f.read()
                for pattern in patterns:
                    matches = re.findall(pattern, code)
                    for match in matches:
                        file_matches[file_name] = match
        return file_matches