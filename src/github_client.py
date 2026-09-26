import httpx
from typing import Dict, Any, List

class GitHubClient:
    def __init__(self, token: str = None):
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        # Only attach Authorization header if token exists and is not empty
        if token and token.strip():
            self.headers["Authorization"] = f"Bearer {token.strip()}"
            
    async def fetch_repo_structure(self, owner: str, repo: str) -> List[Dict[str, Any]]:
        url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/main?recursive=1"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            if response.status_code == 404:
                # Fallback to master branch if main branch isn't used
                url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/master?recursive=1"
                response = await client.get(url, headers=self.headers)
            
            response.raise_for_status()
            return response.json().get("tree", [])