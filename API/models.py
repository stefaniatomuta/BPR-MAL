class Violation:
    def __init__(self, name, description, severity, type, code, rule):
        self.name = name
        self.description = description
        self.severity = severity
        self.type = type
        self.code = code
        self.rule = rule

    def __str__(self):
        return f"Name: {self.name} \nDescription: {self.description} \nSeverity: {self.severity} \nType: {self.type}\nCode: {self.code} \nRule: {self.rule}"


class Result:
    def __init__(self, score, violations=None):
        self.score = score
        self.violations = violations or []

    def __str__(self):
        return f"\nScore: {self.score}".join(
            [f"Description: {v.description}, Severity: {v.severity}" for v in self.violations])


class Rule:
    def __init__(self, name, description, enabled):
        self.name = name
        self.description = description
        self.enabled = enabled

    def __str__(self):
        return f"Name: {self.name} \nDescription: {self.description} \nEnabled: {self.enabled}"
