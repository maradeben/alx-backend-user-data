#!/usr/bin/env python3


def require_auth(path, excluded_paths):
    if path is None or excluded_paths is None or excluded_paths == []:
        return True
    # path += '/' if not path.endswith('/') else ''
    # return True if path is not part of the excluded
    # return path not in excluded_paths
    for ex_path in excluded_paths:
        if ex_path.endswith('*') and path.startswith(ex_path[:-1]):
            return False
    path += '/' if not path.endswith('/') else ''
    # return True if path is not part of the excluded
    return path not in excluded_paths


print(require_auth(None, None))
print(require_auth(None, []))
print(require_auth("/api/v1/status/", []))
print(require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(require_auth("/api/v1/status", ["/api/v1/status/"]))
print(require_auth("/api/v1/users", ["/api/v1/status/"]))
print(require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))
print(require_auth("/api/v1/users", ["/api/v1/stat*"]))
print(require_auth("/api/v1/status", ["/api/v1/stat*"]))
print(require_auth("/api/v1/stat", ["/api/v1/stat*"]))
