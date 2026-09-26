import os
from typing import List, Dict, Any

class RepoParser:
    def __init__(self, config: dict):
        self.max_files = config['github']['max_files_to_read']
        self.ignored_exts = set(config['github']['ignored_extensions'])
        self.ignored_dirs = set(config['github']['ignored_directories'])

    def filter_tree(self, tree: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        filtered = []
        for item in tree:
            path = item.get("path", "")
            parts = path.split("/")
            
            # Skip ignored directories
            if any(part in self.ignored_dirs for part in parts):
                continue
                
            # Skip ignored file extensions
            ext = os.path.splitext(path)[1].lower()
            if ext in self.ignored_exts:
                continue
                
            if item.get("type") == "blob":  # It's a file
                filtered.append(item)
                
            if len(filtered) >= self.max_files:
                break
                
        return filtered

    def build_tree_summary(self, tree: List[Dict[str, Any]]) -> str:
        paths = [item["path"] for item in tree if item.get("type") == "blob"]
        return "\n".join(paths)