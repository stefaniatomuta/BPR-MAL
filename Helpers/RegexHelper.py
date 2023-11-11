IF_PATTERN = r'if\s*\(.+?\)'
FOR_PATTERN = r'for\s*\(.+?\)'
WHILE_PATTERN = r'while\s*\(.+?\)'
FOREACH_PATTERN = r'foreach\s*\(.+?\)'
USINGS_PATTERN = r'^using\s+[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*;$'
CODELINES_PATTERN = r'^[^\n].*\S'
COMMENTS_PATTERN = r'^[^\n]*(?:(?:\/\/[^\n]*)|(?:\/\*[\s\S]*?\*\/)|\S.*(?:\/\/[^\n]*|\/\*[\s\S]*?\*\/))'
METHOD_PATTERN = r'\b(?:public|private|protected|internal|static|virtual|override|abstract|sealed|partial|async)?\s+\w+\s+\w+\s*\([^)]*\)\s*{[^}]*}'
CLASS_PATTERN = r'class (\w+)(?:\s*:\s*(\w+))?'
INTERFACE_PATTERN = r'public\s*interface\s+\w+\s*{[^}]*}'
INHERITANCE_PATTERN = r'\bclass\s+\w+\s*:\s*(?:\w+\s*,\s*)*\w+\b'
APICLIENT_PATTERN = r'\bHttpClient\b\s+(\w+)(?![\w)])'
CLASS_COUPLING = r'\b[A-Z][A-Za-z0-9_]*(?:<[A-Za-z][A-Za-z0-9_]*>)?(?!(?:\s*\{|;|\s*\=)|\s*\.|\s*\-|\s*\?|s*\+|\s*\(|\s*\,|\s*\:|\s*\}|\s*\)|\s*\\)\b'
CSPROJ_PACKAGE_REFERENCE = r'<PackageReference\s+Include="([^"]+)"'
TARGET_FRAMEWORK = r'<TargetFramework>(.*?)</TargetFramework>'
TARGET_FRAMEWORK_VERSION = r'<TargetFrameworkVersion>(.*?)</TargetFrameworkVersion>'
